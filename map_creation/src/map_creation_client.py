#!/usr/bin/env python3

import rospy
# from nav_msgs improt Odometry
# from geometry_msgs import PoseWithCovariance, Pose, Point, Quaternion
from map_server.srv import map_creationRequest, map_creationResponse, map_creation

class MapCreationClient:
    def __init__(self):
        rospy.wait_for_service('room info')
        self.room_info_subscriber = rospy.Subscriber('room_information', self.room_info_callback)
        self.room_connection_subscriber = rospy.Subscriber('room_connections', self.room_connection_callback)
        # self.location_subscriber = rospy.Subscriber('location', Odemetry, self.callback)
        rospy.wait_for_service('map_creation')
        self._client = rospy.ServiceProxy('map_creation', map_creation)

    def room_info_callback(self,data):
        print(data)
        request_type = 'ADD_ROOM'
        room_name = [data.roomName]
        corners = data.corners
        self.call(corners,room_name,request_type)

    def room_connection_callback(self,data):
        request_type = 'CONNECT_ROOM'
        room_name_1 = data.roomName1
        room_name_2 = data.roomName2
        room_name = [room_name_1, room_name_2]
        corners = []
        self.call(corners,room_name,request_type)

    def call(self, corners, room_name, request_type):
        # get current position, and with that get the room name
        req = map_creationRequest()
        req.corners = corners
        req.room_name = room_name
        req.request_type = request_type

        resp = self._client(req)
        return resp.is_updated

if __name__ == '__main__':
    rospy.init_node("map_creation_clinet", anonymous=True)
    try:
        while not rospy.is_shutdown():
            client = MapCreationClient()
            rospy.spin()
            # client.call()
    except rospy.ROSInterruptException:
        pass