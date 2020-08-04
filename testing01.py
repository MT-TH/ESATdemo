import sys
import time
import threading
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


sys.path.append("C:/Users/Education/PycharmProjects/test01/venv/Lib/site-packages/ballcosmos")

import os
try:
  os.environ["COSMOS_USERPATH"]
except:
   # os.environ["COSMOS_USERPATH"] = "C:/git/COSMOS/demo"
  os.environ["COSMOS_USERPATH"] = "C:/COSMOS/COSMOS/ESAT_GS_COSMOS_configuration"

from ballcosmos.script import *

print("BallCosmos Userpath:")
print(ballcosmos.top_level.USERPATH)


set_replay_mode(False)

def run_thread():
    print("Running thread")


thread = threading.Thread(target=run_thread)
thread.start()
thread.join()

# print(connect_interface('EXAMPLE_INT'))
# print(interface_state('TEMPLATED_INT'))

# TEST LOOP

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()

#    plotting
def animate(i):
    x_values.append(next(index))
    y_values.append(tlm('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
    plt.cla()
    plt.plot(x_values,y_values)
    print(tlm('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
    print(get_tlm_buffer('ESAT12_WIFI', 'ADCS_PACKET'))

ani = FuncAnimation(plt.gcf(),animate, 150)

plt.tight_layout()
plt.show()

count = 0
while count < 15:
    print(tlm('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
    count += 1
    time.sleep(0.2)



#~ # telemetry.py
print("-> tlm / ADCS_SOLAR_SENSOR_X_PLUS")
print(tlm('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
print("-> tlm_raw / ADCS_SOLAR_SENSOR_X_PLUS")
print(tlm_raw('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
print("-> tlm_ formatted / ADCS_SOLAR_SENSOR_X_PLUS")
print(tlm_formatted('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))
print("-> tlm_with_units /  ADCS_SOLAR_SENSOR_X_PLUS")
print(tlm_with_units('ESAT12_WIFI ADCS_PACKET ADCS_SOLAR_SENSOR_X_PLUS'))

print("--------------------")

print(get_tlm_details([['ESAT12_WIFI', 'ADCS_PACKET', 'ADCS_SOLAR_SENSOR_X_PLUS'], ['ESAT12_WIFI', 'ADCS_PACKET', 'ADCS_SOLAR_SENSOR_X_PLUS']]))
print(get_tlm_buffer('ESAT12_WIFI', 'ADCS_PACKET'))
id = subscribe_packet_data([['ESAT12_WIFI', 'ADCS_PACKET']])
print(get_packet_data(id))
unsubscribe_packet_data(id)

print("--------------------")

script_disconnect()


shutdown_cmd_tlm()
