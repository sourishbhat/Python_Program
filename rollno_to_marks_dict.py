rn = int(input("Enter the # of roll numbers in the list: "))
rn_list = []

for x in range(rn):
    r = int(input("Enter the roll number: "))
    rn_list.append(r)
    
ma = int(input("Enter the maximum marks: "))
ma_list = []

for x in range(0, r):
    m = int(input("Enter the maximum marks for roll number {}: ".format(x + 1)))
    ma_list.append(m)

d = {}

for i in range(min(rn, ma)):
    d[rn_list[i]] = ma_list[i]

print("Roll Number to Maximum Marks Dictionary:", d)
