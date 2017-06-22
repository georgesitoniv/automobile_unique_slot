from django.core.wsgi import get_wsgi_application
import os
import sys
from random import randrange

os.environ['DJANGO_SETTINGS_MODULE'] = 'cars.settings'
application = get_wsgi_application()

def populate_color_table():
    name_list = ["Black", "Red", "White", "Blue", "Yellow", "Silver"]
    hex_code_list = [
        "#000000", "#FF0000", "#FFFFFF", "0000FF", "FFFF00", "C0C0C0"
        ]
    for i in range(0, len(name_list)):
        color = Color(name=name_list[i], hex_code=hex_code_list[i])
        color.save()

def populate_car_table():
    
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cars.settings')
    from cars.models import Car, Color, Slot
