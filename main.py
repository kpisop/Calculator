from functions.basic import *
from functions.LCM import *

request = input("Enter a request: ")

# Basic Operations
if request.startswith(basic_ID[0]):
    numbers = [float(x) for x in request.replace(basic_ID[0], "").split()]
    print(add(*numbers))
elif request.startswith(basic_ID[1]):
    numbers = [float(x) for x in request.replace(basic_ID[1], "").split()]
    print(subtract(*numbers))
elif request.startswith(basic_ID[2]):
    numbers = [float(x) for x in request.replace(basic_ID[2], "").split()]
    print(multiply(*numbers))
elif request.startswith(basic_ID[3]):
    numbers = [float(x) for x in request.replace(basic_ID[3], "").split()]
    print(divide(*numbers))

# LCM
elif request.startswith(LCM_ID):
    numbers = [float(x) for x in request.replace(LCM_ID, "").split()]
    print(lcm(*numbers))
    