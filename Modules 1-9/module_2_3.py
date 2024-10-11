my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
done = 0

while done != len(my_list):
    if my_list[done] < 0:
        break
    elif my_list[done] == 0:
        done += 1
        continue
    else:
        print(my_list[done])
        done += 1
