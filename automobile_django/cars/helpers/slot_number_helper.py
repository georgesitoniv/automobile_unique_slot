from random import randrange


DEFAULT_BEFORE_SLOT = "9999999999999999"
DEFAULT_AFTER_SLOT = "0000000000000000"
DEFAULT_FRONT_SLOT = "0000000000000000"
DEFAULT_MIDDLE_SLOT = "0000000000000000"
DEFAULT_SLOT = "{}-{}-{}-{}".format(
    DEFAULT_FRONT_SLOT,
    DEFAULT_BEFORE_SLOT,
    DEFAULT_MIDDLE_SLOT,
    DEFAULT_AFTER_SLOT
    )

MAX_SLOT = 1000000000000000
TOTAL_SLOT = 16


def get_higher_rank(slot_number):
    higher_slot = int(slot_number) + 1
    higher_slot_str = str(higher_slot)
    for i in range(0, TOTAL_SLOT - len(higher_slot_str)):
        higher_slot_str = "0" + higher_slot_str
    return higher_slot_str

def get_lower_rank(slot_number):
    return int(slot_number) - 1

def create_slot_number(higher_slot):
    if higher_slot:
        higher_slot_split = higher_slot.split('-')
        if int(higher_slot_split[2]) < (MAX_SLOT):
            front_slot = higher_slot_split[0]
            middle_slot = get_higher_rank(higher_slot_split[2])
        else:
            front_slot = get_higher_rank(higher_slot_split[0])
            middle_slot = higher_slot_split[2]
        return "{}-{}-{}-{}".format(
            front_slot, DEFAULT_BEFORE_SLOT, middle_slot, DEFAULT_AFTER_SLOT
            )
    return DEFAULT_SLOT

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
