# print hour, minute, second and microsecond

#once you create a time object, you can easily print its attributes such as hour, minute etc.

from datetime import time
a=time(11,34,56)
print("hour=",a.hour)
print("minute=",a.minute)
print("second=",a.second)
print("microsecond=",a.microsecond)