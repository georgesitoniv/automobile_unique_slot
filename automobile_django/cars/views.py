from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import Car, Color

class Index(TemplateView):
    template_name = "cars/index.html";

def get_all_colors(request):
    colors = Color.objects.all()
    context = []
    for color in colors:
        context.append({
            u"id": color.id,
            u"name": color.name,
        })
    return JsonResponse(context, safe=False)

def get_all_cars(request):
    context = all_car_list()
    return JsonResponse(context, safe=False)

def get_cars_by_color(request):
    id = request.GET.get('id')
    all_cars = all_car_list()
    context = []
    for car in all_cars:
        if str(car['color_id']) == str(id):
            context.append(car)
    return JsonResponse(context, safe=False)

def move_car(request):
    id = request.GET.get('id')
    direction = int(request.GET.get('direction'))
    car = Car.objects.get(id=id)
    slot_number = int(car.slot_number + direction)
    if isValid(car, direction):
        car_partner = Car.objects.get(slot_number=slot_number)
        car_partner.slot_number = car.slot_number
        car.slot_number = slot_number
        car_partner.save()
        car.save()
    return JsonResponse({}, safe=False)

def move_up(request):
    id = request.GET.get('id')
    reference_slot_number = request.GET.get('reference_slot_number')
    car = Car.objects.select_related('slot').get(id=id)
    car.slot.move_up(reference_slot_number)
    return JsonResponse({}, safe=False)

def move_down(request):
    id = request.GET.get('id')
    reference_slot_number = request.GET.get('reference_slot_number')
    car = Car.objects.select_related('slot').get(id=id)
    car.slot.move_down(reference_slot_number)
    return JsonResponse({}, safe=False)

def all_car_list():
    cars = Car.objects.select_related('color', 'slot')\
        .order_by('slot__slot_number')
    car_list = []
    for index, car in enumerate(cars):
        previous_car, next_car = None, None
        if index > 0:
            previous_car = cars[index - 1]
        if index < (cars.count()  - 1):
            next_car = cars[index + 1]
        car_list.append({
            u"index": index + 1,
            u"id":car.id,
            u"name": car.name,
            u"color_name": car.color.name,
            u"color_id": car.color.id,
            u"slot_number": car.slot.slot_number,
            u"previous_slot": previous_car.slot.slot_number \
                if previous_car else None,
            u"next_slot": next_car.slot.slot_number if next_car else None
        })
    return car_list

def isValid(car, direction):
    if direction < 0:
        if car.slot_number > 1:
            return True
        else:
            return False
    elif direction > 0:
        car_count = Car.objects.count()
        if car.slot_number < car_count:
            return True
        else:
            return False
