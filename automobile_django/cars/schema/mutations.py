import graphene
from .types import CarType, ColorType
from cars.models import Car, Color

class MoveCarSlot(graphene.Mutation):
    """
    Moves car slot number up or down. Requires the id of the car being moved
    and the direction of the movement. The direction must be a postive or a
    negative integer.
    """
    class Input:
        id = graphene.ID()
        direction = graphene.Int()
    car = graphene.Field(CarType)

    @staticmethod
    def mutate(root, args, context, info):
        id = args.get('id')
        direction = args.get('direction')

        car = Car.objects.get(id=id)
        movement_slot_number = car.slot_number + direction
        if isValid(car, direction):
            car_partner = Car.objects.get(slot_number=movement_slot_number)
            car_partner.slot_number = car.slot_number
            car.slot_number = movement_slot_number
            car_partner.save()
            car.save()
        return MoveCarSlot(car=car)

class MoveCarSlotExplicit(graphene.Mutation):
    """
    Moves car at a scpecific slot number. Requires the id of the car being moved
    and the desired slot number.
    """
    class Input:
        id = graphene.ID()
        slot_number = graphene.Int()

    car = graphene.Field(CarType)
    validation_error = graphene.String()

    @staticmethod
    def mutate(root, args, context, info):
        id = args.get('id')
        slot_number = args.get('slot_number')

        car = Car.objects.get(id=id)
        if slot_number > 0:
            if slot_number <= Car.objects.count():
                car_partner = Car.objects.get(slot_number=slot_number)
                car_partner.slot_number = car.slot_number
                car.slot_number = slot_number
                car_partner.save()
                car.save()
                return MoveCarSlotExplicit(car=car)
            else:
                return MoveCarSlotExplicit(
                    validation_error=
                        "Desired slot number execeeded current slot numbers"
                        )
        else:
            return MoveCarSlotExplicit(
                validation_error="Slot number must be greater than zero"
                )

def isValid(car, slot_number):
    if slot_number < 0:
        if car.slot_number > 1:
            return True
        else:
            return False
    elif slot_number > 0:
        car_count = Car.objects.count()
        if car.slot_number < car_count:
            return True
        else:
            return False
