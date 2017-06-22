import graphene

from .types import CarType, ColorType
from .mutations import MoveCarSlot, MoveCarSlotExplicit
from cars.models import Car, Color

class Mutation(graphene.AbstractType):
    move_car_slot = MoveCarSlot.Field()
    move_car_slot_explicit = MoveCarSlotExplicit.Field()

class Query(graphene.AbstractType):
    all_cars = graphene.List(CarType)
    all_colors = graphene.List(ColorType)
    car =  graphene.Field(
        CarType,
        id=graphene.ID()
    )
    color = graphene.Field(
        ColorType,
        id=graphene.ID()
    )
    car_by_color = graphene.List(
        CarType,
        color_id=graphene.ID()
    )

    def resolve_all_cars(self, args, context, info):
        return Car.objects.select_related("color").order_by('slot_number').all()

    def resolve_all_colors(self, args, context, info):
        return Color.objects.prefetch_related("cars").all()

    def resolve_car(self, args, context, info):
        id = args.get('id')

        if id is not None:
            return Car.objects.select_related('color').get(id=id)
        return None

    def resolve_color(self, args, context, info):
        id = args.get('id')

        if id is not None:
            return Color.objects.prefetch_related('cars').get(id=id)
        return None

    def resolve_car_by_color(self, args, context, info):
        color_id = args.get('color_id')

        if color_id is not None:
            if color_id.lower() != "all" and color_id != "":
                try:
                    color = Color.objects.prefetch_related("cars").\
                        get(id=color_id)
                    return color.cars.order_by('slot_number').all()
                except:
                    pass
        return Car.objects.select_related("color").order_by('slot_number').all()
