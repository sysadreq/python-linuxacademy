#timer

import time


start_time = (time.localtime())

#print(time.strftime("%H:%M:%S"))

print(f"Timer started at {time.strftime('%X', start_time)}" )

#Wait for user to stop timer

input("press 'Enter' to stop timer ")

stop_time = (time.localtime())
print(time.mktime(start_time))
print(time.mktime(stop_time))
difference= (time.mktime(stop_time) - time.mktime(start_time))


print(f"Timer stopped at {time.strftime('%X', stop_time)}" )
print(f"Total time: {difference} seconds" )


