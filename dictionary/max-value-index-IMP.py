# The pattern is very important (uses everywhere: arrays, ML, trading, etc.)
# what the code doing -> Loop → initialize → compare → update max

my_points = {'a':(4,3), 'b':(1,2), 'c':(5,1)}

coordinates = my_points.values()

max_x = max( pair[0] for pair in coordinates)
max_y = max( pair[1] for pair in coordinates)

print('maximum values at index(my_points, 0) = ', max_x)
print('maximum values at index(my_points, 1) = ', max_y)
