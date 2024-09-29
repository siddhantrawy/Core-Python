""" Write a Python program to display the current date and time. """

import datetime
print("Current Date & Time -")
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))