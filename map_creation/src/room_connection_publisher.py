#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from map_server.msg import room_connections



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
def publish_room_connections():
    room_connecitonsss = [
        [String('room_1') , String('room_3')],
        [String('room_2') , String('room_3')],
        [String('room_3') , String('room_1')],
        [String('room_3') , String('room_2')],
        [String('room_3') , String('room_5')],
        [String('room_3') , String('room_4')],
        [String('room_4') , String('room_3')],
        [String('room_5') , String('room_3')],

    ]
    pub = rospy.Publisher('room_connections', room_connections, queue_size=10)
    for room_connection in room_connecitonsss:
        pub.publish(room_connections(room_connection[0], room_connection[1]))
        

if __name__ == '__main__':
    rospy.init_node("room_info_publisher", anonymous=True)
    try:
        publish_room_connections()
    except rospy.ROSInterruptException:
        pass