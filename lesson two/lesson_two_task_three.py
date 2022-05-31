input_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for elem in range(len(input_str)):
    if input_str[elem].isdigit():
        input_str[elem] = str(input_str[elem].rjust(2,'0'))
    if input_str[elem].startswith('+'):
        input_str[elem] = str(input_str[elem].zfill(3))

count = 0

while count < len(input_str):
    if input_str[count].isdigit() or input_str[count].startswith('+'):
        input_str.insert(count, '"')
        input_str.insert(count + 2, '"')
        count += 1
    count += 1

joint_str = ' '.join(input_str)

print(joint_str.capitalize())

