import math
def paint_cal(height, width, cover):
    num_cans = (height * width) / cover
    round_cans = math.ceil(num_cans)
    print(f"you will need {round_cans} cans to paint")

h = int(input())
w = int(input())
coverage = 5

paint_cal(h, w, coverage)
# paint_cal(height = h, w = width, cover = coverage)