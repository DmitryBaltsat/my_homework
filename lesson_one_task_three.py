first_ending = [1, 21, 31, 41, 51, 61, 71, 81, 91]
second_ending = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]

for percent in range (1, 101):
    if percent in first_ending:
        print(f'{percent} процент')
    elif percent in second_ending:
        print(f'{percent} процента')
    else:
        print(f'{percent} процентов')




