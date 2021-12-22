from math import sqrt

# Not worth the code to read the puzzle
area_y = [-68, -44]
area_x = [269, 292]

list_y = [ el for el in range(area_y[0], area_y[1])]
list_x = [ el for el in range(area_x[0], area_x[1])]
list_y.append(area_y[1])
list_x.append(area_x[1])

min_vy = area_y[0]
max_vy = -area_y[0]
min_vx = round(sqrt(2*area_x[0] + 0.25) - 0.5)
max_vx = area_x[1] + 1

def series_sum(n):
    return n*(n+1)/2

def get_all_y():
    possible_y = []
    for vy in range(min_vy, max_vy):
        max_series = series_sum(vy)
        for t in range(1, 300):
            if (max_series - series_sum(vy-t)) in list_y:
                possible_y.append((vy, t))
    return possible_y

def solve_1(all_y):
    unique_y = set([el[0] for el in all_y])
    return int(series_sum(max(unique_y)))

def solve_2(all_y):
    possible_x_y = set()
    for p in all_y:
        for vx in range(min_vx, max_vx):
            tmp = int(series_sum(max(0,vx-p[1])))
            if (series_sum(vx) - tmp) in list_x:
                possible_x_y.add((vx,p[0]))
    return len(possible_x_y)

all_y = get_all_y()

print(solve_1(all_y))
print(solve_2(all_y))
