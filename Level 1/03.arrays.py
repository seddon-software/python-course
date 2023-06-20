mylist = [3, 6, 10, 15, 21, 28, 36]
total = 0
for n in mylist:
    total = total + n
average = total / len(mylist)
print(f"average of mylist = {average:.2f}")

mylist2 = [2, 5, 9, 2, 8, 19]
total = 0
for n in mylist2:
    total = total + n
average = total / len(mylist2)
print(f"average of mylist2 = {average:.2f}")

mylist3 = range(1, 20)
total = 0
for n in mylist3:
    total = total + n
average = total / len(mylist3)
print(f"average of mylist3 = {average:.2f}")
