import graphics


class House(object):

    def __str__(self):
        return "House "+str(self.house_x_left)

    def __init__(self, house_x_left, house_distance_from_bottom, house_width, house_height, graphics_window):

        # TODO: Remove graphics_window from list.  Move parameter to draw along with any calculations.
        # TODO: Make all __init__ parameters into self
        self.house_x_left = house_x_left
        self.house_distance_from_bottom = house_distance_from_bottom

        # TODO: Make a class for Body
        # ============= HOUSE BODY =============
        # define house bottom left and height and width
        # house_x_left = 100
        # house_distance_from_bottom = 50 # y goes from top to bottom
        # house_width = 200
        # house_height = 100 # not including roof
        house_y_bottom = graphics_window.height - house_distance_from_bottom
        house_x_center = house_x_left + house_width/2

        # based on above, calculate house top right which is needed to create rectangle
        house_x_right = house_x_left + house_width
        house_y_top = house_y_bottom - house_height
        p1 =  graphics.Point(house_x_left, house_y_bottom)
        p2 = graphics.Point(house_x_right, house_y_top)

        # draw main rectangle of house
        self.body = graphics.Rectangle(p1,p2)
        self.body.setFill("green")

        # TODO: Make roof into a class
        # ============= HOUSE ROOF =============
        # calculate three points for the roof
        roof_height = 50
        roof_left_point =  graphics.Point (house_x_left, house_y_top)
        roof_right_point = graphics.Point(house_x_right, house_y_top)
        roof_top_y = house_y_top - roof_height
        roof_top_point = graphics.Point (house_x_center, roof_top_y)
        self.roof = graphics.Polygon(roof_left_point,roof_right_point, roof_top_point)
        self.roof.setFill("yellow")

        # TODO: Make door into a class
        # ============= HOUSE DOOR =============
        door_height = 60
        door_width = 30
        door_x_left = house_x_center-door_width/2
        door_x_right = house_x_center+door_width/2
        door_top_y = house_y_bottom - door_height
        p1 = graphics.Point(door_x_left, house_y_bottom)
        p2 = graphics.Point(door_x_right, door_top_y)
        self.door = graphics.Rectangle(p1,p2)
        self.door.setFill("blue")


        # TODO: Make Window into a class
        # ============ WINDOWS ================

        window_width = 20
        window_height = 30
        door_space = 15

        left_window_right_side = door_x_left - door_space
        left_window_left_side = left_window_right_side - window_width
        right_window_left_side = door_x_right + door_space
        right_window_right_side = right_window_left_side + window_width

        window_top = door_top_y
        window_bottom = door_top_y + window_height

        left_window_bottom_left = graphics.Point(left_window_left_side, window_bottom)
        left_window_top_right = graphics.Point(left_window_right_side, window_top)
        self.left_window = graphics.Rectangle(left_window_bottom_left, left_window_top_right)
        self.left_window.setFill("purple")

        right_window_bottom_left = graphics.Point(right_window_left_side, window_bottom)
        right_window_top_right = graphics.Point(right_window_right_side, window_top)
        self.right_window = graphics.Rectangle(right_window_bottom_left, right_window_top_right)
        self.right_window.setFill("purple")

        self.components = [self.body,self.door,self.left_window,self.right_window,self.roof]

    def move(self,deltax,deltay):
        for component in self.components:
            component.move(deltax,deltay)

    def draw(self,graphics_window):
        # ============ DRAW HOUSE COMPONENTS =============
        for component in self.components:
            component.draw(graphics_window)


def main():
    # ============= WINDOW ==================
    graphics_window_width = 1200
    graphics_window_height = 600
    graphics_window = graphics.GraphWin("My House", graphics_window_width, graphics_window_height)
    house1= House(100,50,200,100,graphics_window)

    house1.draw(graphics_window)
    print(house1.house_distance_from_bottom)

    house2 = House(400,100,100,300,graphics_window)
    house2.move(300, -100)
    house2.draw(graphics_window)

    print(house1)
    print(house2)


    # ============ PAUSE FOR CLICK ON WINDOW =============
    graphics_window.getMouse() # pause for click in window
    graphics_window.close()


if __name__ == "__main__":
    main()
