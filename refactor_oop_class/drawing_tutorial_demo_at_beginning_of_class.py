import graphics

def main():
    # ============= WINDOW ==================
    window_width = 1200
    window_height = 600
    window = graphics.GraphWin("My House", window_width, window_height)

    # ============= HOUSE BODY =============
    # define house bottom left and height and width
    house_x_left = 100
    house_distance_from_bottom = 50 # y goes from top to bottom
    house_width = 200
    house_height = 100 # not including roof
    house_y_bottom = window_height - house_distance_from_bottom
    house_x_center = house_x_left + house_width/2

    # based on above, calculate house top right which is needed to create rectangle
    house_x_right = house_x_left + house_width
    house_y_top = house_y_bottom - house_height
    p1 =  graphics.Point(house_x_left, house_y_bottom)
    p2 = graphics.Point(house_x_right, house_y_top)

    # draw main rectangle of house
    body = graphics.Rectx`angle(p1,p2)
    body.setFill("green")

    # ============= HOUSE ROOF =============
    # calculate three points for the roof
    roof_height = 50
    roof_left_point =  graphics.Point (house_x_left, house_y_top)
    roof_right_point = graphics.Point(house_x_right, house_y_top)
    roof_top_y = house_y_top - roof_height
    roof_top_point = graphics.Point (house_x_center, roof_top_y)
    roof = graphics.Polygon(roof_left_point,roof_right_point, roof_top_point)
    roof.setFill("yellow")

    # ============= HOUSE DOOR =============

    door_height = 60
    door_width = 30
    door_x_left = house_x_center-door_width/2
    door_x_right = house_x_center+door_width/2
    door_top_y = house_y_bottom - door_height
    p1 = graphics.Point(door_x_left, house_y_bottom)
    p2 = graphics.Point(door_x_right, door_top_y)
    door = graphics.Rectangle(p1,p2)
    door.setFill("blue")

    # ============ DRAW HOUSE COMPONENTS =============
    body.draw(window)
    roof.draw(window)
    door.draw(window)

    # ============ PAUSE FOR CLICK ON WINDOW =============
    window.getMouse() # pause for click in window
    window.close()

main()




