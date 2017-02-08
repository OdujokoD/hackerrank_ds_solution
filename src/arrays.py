n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

output = ""
for i in reversed(arr):
    output += str(i) + " "

print(output)