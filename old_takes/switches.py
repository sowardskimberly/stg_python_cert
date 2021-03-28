# rear = 0
# front = 0
# minor = 0
# undercarriage = 0
# misc = 0
#
# def switch(list):
#     for item in list:
#
#         def rear_end(rear):
#             rear = rear + 1
#             return rear
#
#         def front_end(front):
#             front = front + 1
#             return front
#
#         def minor_damage(minor):
#             minor = minor + 1
#             return minor
#
#         def undercarriages(undercarriage):
#             undercarriage = undercarriage + 1
#             return(undercarriage + 1)
#
#         def miscel(misc):
#             misc = misc + 1
#             return misc
#
#         def my_switch_func(item):
#             switcher = {
#                 'REAR END': rear_end(rear),
#                 'FRONT END': front_end(front),
#                 'MINOR DENT / SCRATCHES': minor_damage(minor),
#                 'UNDERCARRIAGE': undercarriages(undercarriage)
#         }
#             return switcher.get(item, miscel(misc))
#
#         banana = my_switch_func(list)
#
#     return [rear, front, minor, undercarriage, misc]



# def switchero(rear, front, minor, undercarriage, misc):
#     return {
#         'REAR END': rear + 1,
#         'FRONT END': front + 1,
#         'MINOR DENT / SCRATCHES': minor + 1,
#         'UNDERCARRIAGE': undercarriage+1
#         }.get(lambda: print(misc+1))()
#
#         # 'FRONT END': rear - front+1,
#         # 'MINOR DENT / SCRATCHES': minor+1
#         # UNDERCARRIAGE""Sure
#         # MISC:
#     switcher = {
#         # 'REAR END': rear_end,

#    }


def rear_end():
    rear_change = 1
    return rear_change


def front_end():
    front_change = 1
    return front_change


def minor_damage():
    minor_change = 1
    return minor_change


def undercarriages():
    undercarriage_change = 1
    return undercarriage_change


def miscel():
    misc_change = 1
    return misc_change


def my_switch_func(item):
    car_damages = {
        'REAR END': 0,
        'FRONT END': 0,
        'MINOR DENT / SCRATCHES': 0,
        'UNDERCARRIAGE': 0
    }