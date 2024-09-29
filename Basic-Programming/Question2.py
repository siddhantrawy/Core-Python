"""  Write a Python program to find out what version of Python you are using. """

import sys

print("Python Version : ", end=" ")
print(sys.version) #Use the sys.version attribute to get the Python version
print("Version Info : ", end=" ")
print(sys.version_info) #Use the sys.version_info attribute to get detailed version information