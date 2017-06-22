from django.contrib import admin
from django.contrib.admin.utils import flatten_fieldsets

from .models import Car, Color, Slot

class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class SlotAdmin(admin.ModelAdmin):
    readonly_fields = ("slot_number", "car")

admin.site.register(Car, CarAdmin)
admin.site.register(Color)
admin.site.register(Slot, SlotAdmin)
