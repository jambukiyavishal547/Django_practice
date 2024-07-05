from enum import IntEnum
from faker import Faker
fake = Faker()
from .models import *
import random

class FakeData:
    def __init__(self) -> None:
        pass
    def add_colors(self):
        Colors.objects.get_or_create(color_code =fake.color())


    def add_people(self):
        for i in range(100):
            obj = People.objects.create(name = fake.name(), about = fake.text(),age=random.randint(15,99))
            for i in range(0, random.randint(0, 30)):
                c, _=Colors.objects.get_or_create(color_code =fake.color())
                obj.colors.add(c)
                PeopleAddress.objects.create(people = obj, address = fake.address())