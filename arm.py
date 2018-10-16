import triad_openvr
import time
import sys


v = triad_openvr.triad_openvr()
v.print_discovered_objects()
while True:
    start = time.time()
    txt = ""
    count = 0
    for each in v.devices["controller_1"].get_pose_quaternion():
        if count <6:
            print each
            count = count + 1
        else:
            time.sleep(1)
            print("\n")
            print each
            count = 0


    #     txt += each
    #     txt += " "
    # print "\r" + txt,
    # sleep_time = interval - (time.time() - start)
    # if sleep_time > 0:
    #     time.sleep(sleep_time)