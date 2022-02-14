def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("The average Score of alpha = ", cal_average([20, 30, 40]))
print("The average Score of beta = ", cal_average([30, 40, 50]))

