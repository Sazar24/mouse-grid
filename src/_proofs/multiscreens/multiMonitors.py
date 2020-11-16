# https://stackoverflow.com/questions/30312875/tkinter-winfo-screenwidth-when-used-with-dual-monitors

import screeninfo
result = screeninfo.get_monitors()

# result:
# [
#     Monitor(x=-1920, y=-1, width=1920, height=1080, width_mm=509, height_mm=286, name='\\\\.\\DISPLAY1'),
#     Monitor(x=0, y=0, width=1920, height=1080, width_mm=527, height_mm=297, name='\\\\.\\DISPLAY2'),
#     Monitor(x=1920, y=11, width=1920, height=1080, width_mm=509, height_mm=286, name='\\\\.\\DISPLAY3')
# ]
m: screeninfo.common.Monitor
print("monitors:")
for m in result:
    print(m)
print("------------")

print(f"Total monitors amount: {len(result)}")


def get_monitor_from_coord(x, y):
    monitors = screeninfo.get_monitors()

    for m in reversed(monitors):
        if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
            return m
    return monitors[0]


# Get the screen which contains top
# current_screen = get_monitor_from_coord(top.winfo_x(), top.winfo_y())
current_screen = get_monitor_from_coord(2, 3)

# where top is your Tk root)
# print(current_screen)

# Get the monitor's size
# print(current_screen.width)
# print("------------")
# print(current_screen.height)
