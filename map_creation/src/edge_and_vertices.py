import numpy as np

class Vertice:

    def __init__(self, name, corners):
        self.name = name 
        self.corners = {corners}

    #works if room are in a globular shape, and not some weird edgy shape
    #we work with 1 sqm uncertainty
    def withinCorners(self,location,epsilon = 1):
        def PolyArea(x, y):
            return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
        area_of_room = PolyArea([x[0] for x in self.corners], [y[1] for y in self.corners])

        #now we choose 2 corners, which will be the first 2
        chosen_corners = self.corners[:2]
        x_coords = [x[0] for x in chosen_corners]
        x_coords.apped(location[0])
        y_coords = [y[1] for y in chosen_corners]
        y_coords.append(location[1])

        area_of_formed_triangle = PolyArea(x_coords,y_coords)
        return area_of_formed_triangle < (area_of_room - epsilon)

    #we are assuming all corners added are valid
    def addCorners(self, new_corner):
        self.corners.add(new_corner)
    
    def isNot(self, other):
        return not self.name == other.name

    def notName(self, name):
        return not self.name == name



class Graph:

    def __init__(self):

        self.size = 0
        self.adjLists = {}

    def getRoom(self,name):
        for room in self.adjLists.keys():
            if room.name == name:
                return room
        return None

    def hasVertice(self, vertice):
        for v in self.adjLists:
            if vertice.name == v.name:
                return True
        return False


    #links 2 vertice together
    def addVertice(self, vertice):
        if not self.hasVertice(vertice):
            self.size +=1
            self.adjLists[vertice] = []
            return True
        else:
            return False

    def connect_2_vertice(self, vertice_1, vertice_2):
        tmp = self.adjLists[vertice_1]
        tmp.append(vertice_2)
        self.adjLists[vertice_1] = tmp

        tmp = self.adjLists[vertice_2]
        tmp.append(vertice_1)
        self.adjLists[vertice_2] = tmp

        return True

    #as of now graph does not check for consistency
    def check_consistency(self):
        pass


