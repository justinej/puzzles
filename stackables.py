ninth_layer = [[9,0,9],  [8,0,9], [7,0,9], [7,1,9], [7,2,9], [8,2,9], [8,1,9], [9,1,9], [9,2,9], [9,3,9], [8,3,9], [7,3,9], [4,0,9], [4,1,9], [4,2,9], [4,3,9], [3,3,9], [2,3,9], [2,4,9], [3,4,9], [3,5,9], [2,5,9], [1,5,9], [0,5,9], [0,6,9], [0,1,9], [3,8,9], [3,9,9], [2,9,9]]

eigth_layer =  [[9,0,8],  [8,0,8], [7,0,8], [6,0,8], [5,0,8], [4,0,8], [2,0,8], [3,0,8], [9,3,8], [8,3,8], [7,3,8], [9,6,8], [8,6,8], [5,6,8], [4,6,8],  [3,6,8], [2,6,8], [1,6,8], [5,7,8], [4,7,8],  [3,7,8], [2,7,8], [1,7,8], [4,8,8], [5,8,8],  [6,8,8], [7,8,8], [8,8,8], [9,8,8], [9,9,8]]

seventh_layer = [[9,9,7], [8,6,7], [7,6,7], [6,6,7], [5,6,7], [4,6,7], [3,6,7], [9,0,7], [7,0,7], [6,0,7], [5,0,7], [3,0,7], [3,1,7], [4,1,7], [5,1,7], [6,1,7], [7,1,7], [9,1,7], [9,2,7], [9,3,7]]

sixth_layer = [[9,0,6], [8,0,6], [3,6,6], [3,7,6], [2,7,6], [1,7,6], [0,7,6], [3,8,6], [2,8,6], [1,8,6], [0,8,6], [1,9,6]]

fifth_layer = [[9,0,5], [8,0,5], [9,4,5], [8,4,5], [7,4,5], [9,5,5], [8,5,5], [7,5,5], [6,5,5], [5,5,5], [9,6,5], [8,6,5], [7,6,5], [6,6,5], [5,6,5], [9,9,5], [8,9,5], [7,9,5], [6,9,5], [5,9,5], [4,9,5], [3,9,5], [2,9,5], [1,9,5]]

fourth_layer = [[9,9,4], [8,9,4], [7,9,4], [9,7,4], [8,7,4], [7,7,4], [6,7,4], [5,7,4], [4,7,4], [3,7,4], [9,6,4], [8,6,4], [7,6,4], [6,6,4], [5,6,4], [4,6,4], [3,6,4], [8,4,4], [7,4,4], [9,0,4], [8,0,4], [7,0,4], [6,0,4], [5,0,4], [4,0,4]]

third_layer = [[9,9,3], [8,9,3], [7,9,3], [9,6,3], [8,6,3], [7,6,3], [6,6,3], [5,6,3], [4,6,3], [3,6,3], [2,6,3], [1,6,3], [0,6,3], [9,4,3], [8,4,3], [9,0,3], [4,0,3], [3,0,3], [2,0,3], [1,0,3], [0,0,3]]

second_layer = [[9,9,2], [8,9,2], [7,9,2], [6,9,2], [5,9,2], [4,9,2], [3,9,2], [2,9,2], [7,7,2], [6,7,2], [0,6,2], [1,6,2], [2,6,2], [3,6,2], [0,0,2], [1,0,2], [9,0,2], [2,2,2], [3,2,2], [4,2,2], [5,2,2], [9,4,2]]


first_layer = [[1,0,1], [2,0,1], [3,0,1], [4,0,1], [0,1,1], [1,1,1], [2,1,1], [3,1,1], [4,1,1], [0,2,1], [1,2,1], [2,2,1], [5,2,1], [6,2,1], [7,2,1], [7,3,1], [7,4,1], [8,4,1], [9,4,1], [3,6,1], [4,6,1], [5,6,1], [6,6,1], [7,6,1], [6,7,1], [7,7,1], [6,8,1], [7,8,1], [2,9,1], [3,9,1], [4,9,1], [5,9,1]]

zeroth_layer =  [[9,0,0], [8,0,0], [7,0,0], [7,5,0], [7,6,0], [7,8,0], [7,9,0], [6,0,0], [6,1,0], [6,5,0], [6,9,0], [5,1,0], [5,2,0], [5,3,0], [5,4,0], [5,5,0], [5,9,0], [4,4,0], [4,5,0], [4,6,0], [3,4,0], [3,5,0], [3,6,0], [2,4,0], [2,5,0]]

squares = zeroth_layer + first_layer + second_layer + third_layer
squares = squares + fourth_layer + fifth_layer + sixth_layer
squares = squares + seventh_layer + eigth_layer + ninth_layer


def visualize_x(squares, x_coord):
    cross_section = [sq for sq in squares if sq[0] == x_coord]
    print "_"*10
    for z_coord in xrange(10):
        row = ""
        for y_coord in xrange(10):
            if [x_coord, y_coord, z_coord] in cross_section:
                row = row + "X"
            else: row = row + " "
        print row
    print "-"*10

def visualize_y(squares, y_coord):
    cross_section = [sq for sq in squares if sq[1] == y_coord]
    print "_"*10
    for z_coord in xrange(10):
        row = ""
        for x_coord in xrange(10):
            if [x_coord, y_coord, z_coord] in cross_section:
                row = row + "X"
            else: row = row + " "
        print row
    print "-"*10

def visualize_z(squares, z_coord):
    cross_section = [sq for sq in squares if sq[2] == z_coord]
    print "_"*10
    for y_coord in xrange(10):
        row = ""
        for x_coord in xrange(10):
            if [x_coord, y_coord, z_coord] in cross_section:
                row = row + "X"
            else: row = row + " "
        print row
    print "-"*10
    

print "Printing all x cross_sections"
for x_coord in xrange(10):
    visualize_x(squares, x_coord)
    print ""

print "Printing all y cross_sections"
for y_coord in xrange(10):
    visualize_y(squares,y_coord)

print "Printing normals"
for z_coord in xrange(10):
    visualize_z(squares, z_coord)
