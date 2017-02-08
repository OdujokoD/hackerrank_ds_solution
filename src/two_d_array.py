arr = []
hour_glass_total = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


def generate_hourglass(i, j):
    temp_total = 0
    temp_total += arr[i][j]
    for x in range(j, j + 2):
        temp_total += arr[i][x + 1]
        # temp.append((i, x + 1))

    temp_total += arr[i + 1][j + 1]
    # temp.append((i + 1, j + 1))

    for y in range(j, j + 3):
        temp_total += arr[i + 2][y]
        # temp.append((i + 2, y))

    hour_glass_total.append(temp_total)


def minimize():
    for i in range(4):
        for j in range(4):
            generate_hourglass(i, j)


def get_max_hour():
    max_hour = hour_glass_total[0]
    for i in range(len(hour_glass_total)):
        if hour_glass_total[i] > max_hour:
            max_hour = hour_glass_total[i]

    return max_hour


minimize()
print(get_max_hour())