from math import sqrt, cos, sin, tan, pi, radians


class Point:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str((self.x, self.y))


class Shape:
    def __init__(self):
        self.center = Point(0, 0)

    def get_center(self):
        return self.center

    def move(self, x, y):
        self.center.x = x
        self.center.y = y

    def get_distance(self, figure1, figure2):
        return sqrt((figure2.center.x-figure1.center.x)**2
                    + (figure2.center.y-figure1.center.y)**2)


class Circle(Shape):
    def __init__(self, radius=1):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return round((self.radius**2)*pi, 2)


class Triangle(Shape):
    def __init__(self, face=1):
        super().__init__()
        self.face = face

    def get_area(self):
        return round((self.face**2)*sqrt(3)/4, 2)

    def get_vertex(self):
        R = self.face/sqrt(3)
        a = Point(R*cos(0)+self.center.x, R*sin(0)+self.center.y)
        b = Point(R*cos(pi/3*2)+self.center.x, R*sin(pi/3*2)+self.center.y)
        c = Point(R*cos(pi/3*4)+self.center.x, R*sin(pi/3*4)+self.center.y)
        return([a, b, c])


class Square(Shape):
    def __init__(self, face=1):
        super().__init__()
        self.face = face

    def get_area(self):
        return (self.face**2)

    def get_vertex(self):
        half = self.face/2
        a = Point(self.center.x+half, self.center.y+half)
        b = Point(self.center.x-half, self.center.y+half)
        c = Point(self.center.x-half, self.center.y-half)
        d = Point(self.center.x+half, self.center.y-half)
        return([a, b, c, d])


class Polygon(Shape):
    def __init__(self, face=1, vertex=3):
        super().__init__()
        self.face = face
        # rotation in degrees
        self.rotation = 0
        if vertex < 3:
            self.vertex = 3
        else:
            self.vertex = vertex

    def get_area(self):
        # radius of circle inscribed in a polygon
        insc_radius = self.face/(2*tan(pi/self.vertex))
        # perimeter of a polygon
        perimeter = self.face * self.vertex
        # area of a polygon
        return round(0.5 * perimeter * insc_radius, 2)

    def get_vertex(self):
        # circumscribed radius of a polygon
        R = self.face/(2*sin(2*pi/(2*self.vertex)))
        # list of vertexes of a polygon
        vertex_list = []
        for cur_vert in range(self.vertex):
            cur_degree = ((2*pi)/self.vertex)*cur_vert+radians(self.rotation)
            #radians(360/self.vertex*cur_vert+self.rotation)
            vertex_list.append(Point(R*cos(cur_degree)+self.center.x,
                                     R*sin(cur_degree)+self.center.y))
        return vertex_list

    def rotate(self, degree):
        self.rotation += int(degree)
        if self.rotation >= 360:
            self.rotation = self.rotation % 360


print("Create a circle with radius = 1 ...")
circle1 = Circle()
print("Area of the circle is ", circle1.get_area())
print("------------------------------------------------------------")

print("Create a triangle with face = 1 ...")
triangle1 = Triangle()
print("Area of the triangle is ", triangle1.get_area())
print("Coordinates of vertexes: ", triangle1.get_vertex())
print("------------------------------------------------------------")

print("Create a polygon with face = 1 and vertex = 3 ...")
my_poly = Polygon(1, 3)
print("Area of the polygon is ", my_poly.get_area())
print("Coordinate of vertexes: ", my_poly.get_vertex())
print("------------------------------------------------------------")

print("Create a square with face = 2,5 ...")
square1 = Square(2.5)
print("Area of the square is ", square1.get_area())
print("Center of the square is ", square1.get_center())
print("Move the square to the point(10, 10)")
square1.move(10, 10)
print("Center of the square is ", square1.get_center())
print("Coordinates of vertexes: ", square1.get_vertex())
print("------------------------------------------------------------")

print("Create a polygon with face = 2,5 and vertex = 4 ...")
my_poly = Polygon(2.5, 4)
print("Area of the polygon is ", my_poly.get_area())
my_poly.move(10, 10)
print("Center of the polygon is ", my_poly.get_center())
print("Coordinates of vertexes: ", my_poly.get_vertex())
print("Rotation of the poligon is {} degrees".format(my_poly.rotation))
print("Rotate the polygon by 45 degrees")
my_poly.rotate(45)
print("Rotation of the poligon is {} degrees".format(my_poly.rotation))
print("Coordinates of vertexes: ", my_poly.get_vertex())
print("------------------------------------------------------------")

print("Create a polygon with face = 1,5 and vertex = 10 ...")
my_poly = Polygon(1.5, 10)
print("Area of the polygon is ", my_poly.get_area())
print("Coordinates of vertexes: ", my_poly.get_vertex())
print("Rotation of the poligon is {} degrees".format(my_poly.rotation))
print("Rotate the polygon by 120 degrees")
my_poly.rotate(120)
print("Rotation of the poligon is {} degrees".format(my_poly.rotation))
print("Coordinates of vertexes: ", my_poly.get_vertex())
print("Rotate the polygon again by 240 degrees")
my_poly.rotate(240)
print("Rotation of the poligon is {} degrees".format(my_poly.rotation))
print("Coordinates of vertexes: ", my_poly.get_vertex())
