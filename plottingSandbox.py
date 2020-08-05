import sys
import time
import threading
from itertools import count
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import numpy as np
import time
import datetime as dt

import matplotlib.pyplot as plt

plt.style.use('dark_background')


#  length of window
n = 50

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(n))
ys = [0]*n

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):


    # Add x and y to lists
    # xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(random.randint(0, 100))

    # Limit x and y lists to 'n' items
    # xs = xs[-n:]
    ys = ys[-n:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Fancy title')
    plt.ylabel('Sun sensor (%)')
    plt.axis([0,n+4,0,100])
    plt.xticks([])

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=500)
plt.show()

#  --------------------------------
#
# # plotting
# plt.style.use('dark_background')
#
# plt.axis([0, 50, 0, 100])
#
# x_values = []
# y_values = []
#
# for i in range(50):
#     x_values.append(i)
#     y_values.append(random.randint(0, 100))
#     plt.plot(x_values, y_values,'r')
#     plt.pause(0.05)
#
# #     for future
#     timeAx = dt.datetime.now().strftime('%H:%M:%S.%f')
#
# plt.show()


# ----------------------------------------------
#
# plt.style.use('fivethirtyeight')
#
# x_values = []
# y_values = []
#
# index = count()
#
# #    plotting
# def animate(i):
#     x_values.append(next(index))
#     # y_values.append(tlm('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
#     y_values.append(random.randint(0,100))
#     plt.cla()
#     plt.plot(x_values,y_values)
#     # print(tlm('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
#     # print(get_tlm_buffer('ESAT12_WIFI', 'ADCS_PACKET'))
#
# ani = FuncAnimation(plt.gcf(),animate, 150)
#
# plt.tight_layout()
# plt.show()