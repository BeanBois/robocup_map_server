#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point
from map_server.msg import room_information



#ROOMS 100X100
#
#       #         #
#       #    1    #
#       #         #
#########         ############
#                            #
#    2       3         4     #
#                            #
##########        ############
#        #        #   
#        #   5    #
#(0,0)   #        #
def publish_room_info():
    room_informations =[
        [String('room_1') , [Point(100,300,0),Point(200,300,0), Point(100,200,0), Point(200,200,0)]],
        [String('room_2') , [Point(0,100,0),Point(0,200,0), Point(100,100,0), Point(100,200,0)]],
        [String('room_3') , [Point(100,100,0),Point(100,200,0), Point(200,100,0), Point(200,200,0)]],
        [String('room_4') , [Point(200,200,0),Point(200,100,0), Point(300,100,0), Point(300,200,0)]],
        [String('room_5') , [Point(100,0,0),Point(200,0,0), Point(100,100,0), Point(200,100,0)]]

    ]
    pub = rospy.Publisher('room_information', room_information, queue_size=10)
    for room_info in room_informations:
        pub.publish(room_information(room_info[0], room_info[1]))

    print('published')

if __name__ == '__main__':
    rospy.init_node("room_info_publisher", anonymous=True)
    try:
        publish_room_info()
    except rospy.ROSInterruptException:
        pass