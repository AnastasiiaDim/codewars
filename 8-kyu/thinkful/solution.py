def update_light(current):
    lights_list = ['green', 'yellow', 'red']
    next_index = lights_list.index(current) + 1

    if current == 'red':
        next_index = 0
    return lights_list[next_index]


# def update_light(current):
#     lights = ['green', 'yellow', 'red']

#     # (2 + 1) % 3 gives 0. Red (2) turns into Green (0) by itself

#     next_index = (lights.index(current) + 1) % len(lights)
#     return lights[next_index]
