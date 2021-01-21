import psutil
from win10toast import ToastNotifier
import time
import requests
import sys
import signal

toaster = ToastNotifier()
battery = psutil.sensors_battery()
minutes_to_sleep = 15

def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0)
    sys.exit(0)

if sys.argv[1] == "handle_signal":
    signal.signal(signal.SIGTERM, sigterm_handler)

def notify_user():
    plugged_boolean = battery.power_plugged
    network_adapter = psutil.net_if_stats()
    percent = str(battery.percent)
    ethernet = network_adapter['Ethernet']
    if int(percent) == 100 and plugged_boolean:
        if ethernet.isup:
            requests.get(
                'https://maker.ifttt.com/trigger/TurnOffPersonalLaptop/with/key/hgjNN_6R1Xb8QSrh0H-S5xhG74kYZd2BlVOfQWdW_g0')
            toaster.show_toast("Battery Full", "Request made to turn off Smart Plug Charger")
            return
        toaster.show_toast("Turn off Charger", "Device is now at 100% battery, please turn off charger!")
    elif int(percent) <= 25 and not plugged_boolean:
        if ethernet.isup:
            toaster.show_toast("Battery Low", "Device is now at {}% battery, Request made to turn on Smart Plug Charger!"
                               .format(percent))
            requests.get(
                'https://maker.ifttt.com/trigger/TurnOnPersonalLaptop/with/key/hgjNN_6R1Xb8QSrh0H-S5xhG74kYZd2BlVOfQWdW_g0')
            return
        toaster.show_toast("Turn on Charger", "Device is now at {}% battery, you may want to plug a charger in!"
                               .format(percent))

try:
    print("Hello")
    while True:
        notify_user()
        time.sleep(minutes_to_sleep * 60)
finally:
    requests.get('https://maker.ifttt.com/trigger/TurnOnPersonalLaptop/with/key/hgjNN_6R1Xb8QSrh0H-S5xhG74kYZd2BlVOfQWdW_g0')
    print("Goodbye")
