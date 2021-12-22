area_y = [-68, -44]
area_x = [269, 292]

list_y = [ el for el in range(area_y[0], area_y[1])]
list_x = [ el for el in range(area_x[0], area_x[1])]
list_y.append(area_y[1])
list_x.append(area_x[1])

def series_sum(n):
    return n*(n+1)/2

def solve_1():
    possible_y = set()
    for vy in range(-100,100):
        max_series = series_sum(vy)
        for t in range(1, 300):
            if (max_series - series_sum(vy-t)) in list_y:
                possible_y.add(vy)
                break
    return series_sum(max(possible_y))

def solve_2():
    possible_y = []
    for vy in range(-100,100):
        max_series = series_sum(vy)
        for t in range(1, 1000):
            if (max_series - series_sum(vy-t)) in list_y:
                possible_y.append((vy, t))

    possible_x_y = set()
    for p in possible_y:
        for vx in range(23, 300):
            tmp = int(series_sum(max(0,vx-p[1])))
            if (series_sum(vx) - tmp) in list_x:
                possible_x_y.add(f'{vx}-{p[0]}')
    return len(possible_x_y)

print(solve_1())
print(solve_2())
