import math

def paint_calc(height, width, cover):
    result = (height * width) / cover
    print(math.ceil(result))


test_h = int(input("Height of wal: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)