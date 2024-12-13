transform move_x(x, speed = 0.5):
    yalign 1.0
    linear speed xalign x

transform move_x_from(f, x, speed = 0.5):
    yalign 1.0
    xalign f
    linear speed xalign x

transform my_left:
    xalign 0.33
    yalign 1.0

transform flip:
    xzoom -1.0