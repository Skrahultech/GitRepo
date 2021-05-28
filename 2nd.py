my_list=[]
n=int(input("Enter number of elements :"))
for i in range(0,n):
    num=int(input())
    my_list.append(num)
my_list.sort()

if(n%2==0):
    m1 = my_list[n//2]
    m2 = my_list[n//2]
    median = (m1 + m2)//2
else:
    median = my_list[n//2]
print("Median is : "+ str(median))