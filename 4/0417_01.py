num = [1, 2, 3, 4, 5]

input = int(input())

for i in num:
    if i == input:
        num.remove(i)

print(num)