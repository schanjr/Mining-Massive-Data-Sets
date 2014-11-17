import matplotlib.pyplot as plt
import numpy as np



class Point(object):
    '''class Point and LineString helps distinguish x and y axis'''
    def __init__(self, x, y):
            self.x = x
            self.y = y
    
class LineString(Point):
    def __init__(self, *points):
        #~ self.points=points
        self.points = []
        for point in points:
            if not isinstance(point, Point):
                point = Point(*point)
            self.points.append(point)

    def length(self):
        L = len(self.points)
        return L
    
def show_plot(x,y,m=0,b=0):
    x = [int(lin.points[i].x) for i in range(len(lin.points))] 
    y = [int(lin.points[i].y) for i in range(len(lin.points))] 
    if m is None and b is None:
        m, b = np.polyfit((x),(y),1)    
    plt.plot(x, y, 'ro')
    for i in range(20): 
        plt.plot(i, m*i + b, '.',alpha=0.7)
    plt.axes([0, 20, 0, 20])
    return plt.show()


#Sample data set
lin = LineString((1, 1),(0, 2),(1,2),(2,3),(3,4),(5,6),(0,3),(12,12))


