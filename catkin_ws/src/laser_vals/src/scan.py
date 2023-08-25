#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan


def callback(msg):
    li = msg.ranges
    l = len(li)
    # print(l)
    list = [];
    # taking 80 valuse for 38 degrees
    for i in range(l-40, l-1, 1):
        list.append(li[i])
    for i in range(0,  40, 1):
        list.append(li[i])
        
    ma = max(list);
    mi = min(list);
    height = ma-mi;
    c = 0;
    st = False;
    for i in list:
        if ((i>ma-0.000001) and (i < ma+0.00001)):
            if (st == False):
                st=True;
            c = c+1;
        if (st == True):
            break;
    
    length = c/2;
    length = length/1000;
    
     
     
    print("height:" + str(height))
    print("length:" + str(length))
    print("\n")   
    # for i in list:
    #    print(str(i) + " ", end=" ")
    # print("\n")

    

rospy.init_node('scan_vals')
sub=rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()