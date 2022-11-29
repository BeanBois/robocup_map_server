
#assuming that i have a server that takes location and return the name of the room


import rospy
import Vertice, Graph



class MapCreationServer:

    def __init__(self, own_location_server, room_name_server):

        self.map = Graph()
        pass

    def makeVertice(self,req):
        room_name = req.room_name.pop()
        corners = req.corners
        vertice = Vertice(room_name, corners)
        return vertice

    def addRoom(self, vertice):
        self.map.addVertice(vertice)

    def connectTwoRooms(self,vertice_1,vertice_2):
        self.map.connect_2_vertice(vertice_1,vertice_2)

    def map_creation_service(self,req):
        if req.request_type == 'ADD_ROOM':
            vertice = self.makeVertice(req)
            self.addRoom(vertice)
        elif req.request_type == 'COONNECT_2_ROOM':
            #we assume that the 2 rooms are already in there
            room_1 = self.map.getRoom[req.room_name[0]]
            room_2 = self.map.getRoom[req.room_name[1]]
            self.connectTwoRooms(room_1,room_2)



    



if __name__ == '__main__':
    rospy.init_node("map_creation_server", anonymous=True)
    try:
        while not rospy.is_shutdown():
            server = MapCreationServer()
            service = rospy.Service('map_creation', MapCreation, server.map_creation_service)
            rospy.loginfo("Map Creation Server is ready")
            rospy.spin()
    except rospy.ROSInterruptException:
        pass