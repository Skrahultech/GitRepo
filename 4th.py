my_num=int(input())
count=0
for i in range(2,my_num+1):
    flag=0
    if(i>1):
        for j in range(2,i):
            if(i % j == 0):
                flag=1
                break
        if (flag == 0):
            count=count+1

print(count)z