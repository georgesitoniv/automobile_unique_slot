import uuid
from django.db import models
from .helpers.slot_number_helper import (
    create_slot_number,
    get_higher_slot_number,
    get_lower_slot_number
)

def get_slot_number():
    return (Car.objects.count() + 1)

class Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Slot(models.Model):
    car = models.OneToOneField('Car', on_delete=models.CASCADE)
    slot_number = models.TextField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            last_slot = Slot.objects.all().last()
            if last_slot:
                self.slot_number = create_slot_number(last_slot.slot_number)
            else:
                self.slot_number = create_slot_number(None)
        super(Slot, self).save(*args, *kwargs)

    def move_up(self, reference_slot_number):
        self.slot_number = get_lower_slot_number(reference_slot_number)
        self.save()

    def move_down(self, reference_slot_number):
        self.slot_number = get_higher_slot_number(reference_slot_number)
        self.save()

    def __str__(self):
        return self.car.name

class Car(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    color = models.ForeignKey(Color, related_name="cars")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id is None:
            self.id = uuid.uuid4()
            slot = Slot(car=self)
            slot.save()
        super(Car, self).save(*args, *kwargs)
