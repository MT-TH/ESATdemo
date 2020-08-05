import sys
import time
import threading
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

# plotting
plt.style.use('dark_background')

plt.axis([0, 50, 0, 100])

x_values = []
y_values = []

for i in range(50):
    x_values.append(i)
    y_values.append(random.randint(0, 100))
    plt.plot(x_values, y_values,'r')
    plt.pause(0.05)

plt.show()


#
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