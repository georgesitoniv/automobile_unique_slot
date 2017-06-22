from random import randrange

default_before_slot = "9999999999999999"
default_after_slot = "0000000000000000"

default_front_slot = "0000000000000000"
default_middle_slot = "0000000000000000"

max_slot = 1000000000000000
min_slot = 48
total_slot = 16

slot_numbers = [
    "0000000000000000-0000000000000002-0000000000000001-9999999999999999",
    "0000000000000000-0000000000000002-0000000000000002-9999999999999999",
    "0000000000000000-0000000000000002-0000000000000003-9999999999999999",
    "0000000000000000-0000000000000002-0000000000000004-9999999999999999",
]

lower_slot_numbers = []
higher_slot_numbers = []


def get_higher_rank(slot_number):
    higher_slot = int(slot_number) + 1
    higher_slot_str = str(higher_slot)
    for i in range(0, total_slot - len(higher_slot_str)):
        higher_slot_str = "0" + higher_slot_str
    return higher_slot_str

def get_lower_rank(slot_number):
    return int(slot_number) - 1

def create_slot_number(higher_slot):
    higher_slot_split = higher_slot.split('-')
    if int(higher_slot_split[2]) < (max_slot):
        front_slot = higher_slot_split[0]
        middle_slot = get_higher_rank(higher_slot_split[2])
    else:
        front_slot = get_higher_rank(higher_slot_split[0])
        middle_slot = higher_slot_split[2]
    return "{}-{}-{}-{}".format(
        front_slot, default_before_slot, middle_slot, default_after_slot
        )

def get_lower_slot_number(slot_number_reference):
    slot_number_reference_split = slot_number_reference.split("-")
    front_slot = slot_number_reference_split[0]
    middle_slot = slot_number_reference_split[2]
    after_slot = slot_number_reference_split[3]
    before_slot = get_lower_rank(slot_number_reference_split[1])
    return "{}-{}-{}-{}".format(
        front_slot, before_slot, middle_slot, after_slot
        )

def get_higher_slot_number(slot_number_reference):
    slot_number_reference_split = slot_number_reference.split("-")
    front_slot = slot_number_reference_split[0]
    middle_slot = slot_number_reference_split[2]
    after_slot = get_higher_rank(slot_number_reference_split[3])
    before_slot = slot_number_reference_split[1]
    return "{}-{}-{}-{}".format(
        front_slot, before_slot, middle_slot, after_slot
        )

slot_numbers.sort()
print(slot_numbers)
