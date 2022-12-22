from plyer import notification
import psutil

battery = psutil.sensors_battery()
title = "Battery Low"
message = "Please connect your charger"

if battery.percent < 30:
    notification.notify(title = title ,message = message)

