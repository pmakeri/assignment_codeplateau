def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

alpha = [20, 30, 40]
print(f"alpha Scores: {alpha}")
print("The average Score of alpha = ", cal_average([20, 30, 40]))
beta = [30, 40, 50]
print(f"beta Scores: {beta}")
print("The average Score of beta = ", cal_average([30, 50, 70]))


