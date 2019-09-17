num_list = []
num = int(input("please insert number: "))


def creator(num):
    up = 1
    while up < num:
        temp = up + sum([int(j) for j in str(up)])
        if temp == num:
            num_list.append(up)
        up += 1


creator(num)
print(num_list)