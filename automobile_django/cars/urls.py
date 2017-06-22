from django.conf.urls import url, include

from .views import (
    Index,
    move_car,
    move_up,
    move_down,
    get_all_colors,
    get_all_cars,
    get_cars_by_color,
)

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^api/colors/$', get_all_colors, name="all_colors"),
    url(r'^api/colors/car/$', get_cars_by_color, name="cars_by_color"),
    url(r'^api/cars/$', get_all_cars, name="all_cars"),
    url(r'^api/cars/move/$', move_car, name="move_car"),
    url(r'^api/cars/move-up/$', move_up, name="move_up"),
    url(r'^api/cars/move-down/$', move_down, name="move_down"),
]
