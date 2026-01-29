def num_cards(h):
    # base case of height 1
    if h == 1:
        return 2
    # recursive solution
    else:
        # returns number of cards for tower of height h
        return 3*(h-1) + 2 + num_cards(h-1)


#--- TEST CASES ---#
print(num_cards(1)==2)
print(num_cards(2)==7)
print(num_cards(3)==15)
print(num_cards(4)==26)

def num_triangles(h):
    # base case of height 1 
    if h == 1:
        return 0
    if h == 2:
        return 2
    else:
        # returns number of triangles for tower of height h
        upright = 3 * (h-2)
        upside_down = 2 * (h-2)
        return upright + upside_down + num_triangles(h-1)

#--- TEST CASES ---#
for i in range(1,10):
    print(num_triangles(i))

