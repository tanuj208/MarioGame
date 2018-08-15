f = open("background.txt",'r')
x=[]
for i in range(25):
    x.append(f.readline())

# print(x)
for i in range(25):
    print(x[i],end='')
# print(x[2])