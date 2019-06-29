import numpy as np
from intersection import Intersection as it
import svg

class Line:
    def __init__(self):
        self.points = [[None, None],[None, None]]
        self.vector = [None, None]
        self.degree = 0
        self.radian = 0
        self.a = 0
        self.b = 0
        self.function = "y = {0}x + {1}".format(self.a,self.b)

    def set_2points(self, point1, point2):
        self.points = [point1, point2]
        arr_p1 = np.array(point1)
        arr_p2 = np.array(point2)
        arr_vec = arr_p2 - arr_p1
        self.vector = arr_vec.tolist()
        self.radian = np.arctan(arr_vec[1]/arr_vec[0])
        self.degree = np.rad2deg(self.radian)
        self.a = np.tan(self.radian)
        self.b = point1[1] - self.a * point1[0]
        self.function = "y = {0}x + {1}".format(self.a,self.b)
    
    def set_angle_point(self, angle, point, is_radian = False):
        if is_radian == False:
            angle = np.deg2rad(angle)
        point2 = [point[0] + np.cos(angle), point[1] + np.sin(angle)]
        self.set_2points(point, point2)

    def set_vector_point(self, vector, point):
        point2 = [point[0] + vector[0], point[1] + vector[1]]
        self.set_2points(point, point2)
    
    def get_angle2lines(self, line, is_radian = False):
        angle_1 = self.radian
        angle_2 = line.radian
        angle_A = abs(angle_1 - angle_2)
        angle_B = np.pi - angle_A
        if angle_A < angle_B:
            angle = [angle_A, angle_B]
        else:
            angle = [angle_B, angle_A]
        if is_radian == False:
            angle = np.rad2deg(angle).tolist()
        return angle

    def x_point(self, line):
        point1 = self.points[0]
        point2 = line.points[0]
        vector1 = self.vector
        vector2 = line.vector
        x = it(point1, vector1, point2, vector2)
        return x

    def is_on_line(self, point, threshold = 0.00001):
        a = np.tan(self.radian)
        b = self.points[0][1] - a * self.points[0][0]
        if abs(point[1] -(a * point[0] + b)) > threshold:
            return False
        else:
            return True

    def extention_x(self, terminal_x2, terminal_x1 = None):
        if terminal_x1 == None:
            terminal_x1=self.points[0][0]
        point1=[terminal_x1, self.a * terminal_x1 + self.b]
        point2=[terminal_x2, self.a * terminal_x2 + self.b]
        self.set_2points(point1, point2)
    
    def extention_y(self, terminal_y2, terminal_y1 = None):
        if terminal_y1 == None:
            terminal_y1=self.points[0][1]
        point1=[(terminal_y1-self.b)/self.a, terminal_y1]
        point2=[(terminal_y2-self.b)/self.a, terminal_y2]
        self.set_2points(point1, point2)

    def extention_Length(self, length):
        point1 = self.points[0]
        point2 = [length*np.cos(self.radian)+self.points[0][0], length*np.sin(self.radian)+self.points[0][1]]
        self.set_2points(point1,point2)
    
    def extention_xy(self,top_left,bottom_right,):
        (terminal_x1, terminal_y1) = top_left
        (terminal_x2, terminal_y2) = bottom_right
        self.extention_x(terminal_x2,terminal_x1)
        self.extention_y(terminal_y2,terminal_y1)

    def write_svg(self, svg, stroke="black", stroke_width=1):
        x1=self.points[0][0]
        y1=self.points[0][1]            
        x2=self.points[1][0]
        y2=self.points[1][1]
        svg.create_line(x1,y1,x2,y2,stroke=stroke,stroke_width=stroke_width)