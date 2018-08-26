


lists = [1,2,3,3,4,5,6,3,3]
num_pop = 0
for i in range(len(lists)):
    if (lists[i-num_pop] == 3):
        lists.pop(i-num_pop)
        i -= 1
        num_pop += 1
        print(i)
    if i == len(lists) - 1 - num_pop:
        break
print(lists)