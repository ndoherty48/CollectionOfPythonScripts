import psutil
from win10toast import ToastNotifier
import time
import requests

toaster = ToastNotifier()
battery = psutil.sensors_battery()
plugged_boolean = battery.power_plugged
network_adapter = psutil.net_if_stats()
percent = str(battery.percent)
ethernet = network_adapter['Ethernet']
minutes_to_sleep = 30


def notify_user():
    if int(percent) == 100 and plugged_boolean:
        if ethernet.isup:
            requests.get(
                'https://maker.ifttt.com/trigger/TurnOffPersonalLaptop/with/key/hgjNN_6R1Xb8QSrh0H-S5xhG74kYZd2BlVOfQWdW_g0')
            toaster.show_toast("Battery Full", "Request made to turn off Smart Plug Charger")
        else:
            toaster.show_toast("Turn off Charger", "Device is now at 100% battery, please turn off charger!")
    elif int(percent) <= 25 and not plugged_boolean:
        if ethernet.isup:
            toaster.show_toast("Battery Low", "Device is now at {}% battery, Request made to turn on Smart Plug Charger!"
                               .format(percent))
            requests.get(
                'https://maker.ifttt.com/trigger/TurnOnPersonalLaptop/with/key/hgjNN_6R1Xb8QSrh0H-S5xhG74kYZd2BlVOfQWdW_g0')
        else:
            toaster.show_toast("Turn on Charger", "Device is now at {}% battery, you may want to plug a charger in!"
                               .format(percent))


while True:
    notify_user()
    time.sleep(minutes_to_sleep * 20)
