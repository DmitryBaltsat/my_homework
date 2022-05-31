numbers = []
total_sum_one = 0
total_sum_two = 0

for number in range (1, 1001, 2):
    cube_number = number ** 3
    numbers.append(cube_number)
    str_num = str(cube_number)
    sum = 0
    for idx in range (len(str_num)):
        sum += int(str_num[idx])
    if sum % 7 == 0:
        total_sum_one += cube_number
print(f'Cумма цифр кратных семи из первого списка равна - {total_sum_one}.')

for idx in range(len(numbers)):
    numbers[idx] += 17
# numbers[:] = [num + 17 for num in numbers]

for new_number in numbers:
    str_num = str(new_number)
    sum = 0
    for idx in range (len(str_num)):
        sum += int(str_num[idx])
    if sum % 7 == 0:
        total_sum_two += new_number
print(f'Cумма цифр кратных семи из второго списка (+17) равна - {total_sum_two}.')


