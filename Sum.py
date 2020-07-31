n1=int(input("enter num1"))
n2=int(input("enter num2"))
sum=0
if n1<n2:
 for i in range(n1,n2+1):
    sum=sum+i
    n3=n2-n1+1
else:
    for i in range(n1,n2-1,-1):
        sum=sum+i
    n3=n1-n2+1
print("sum of numbers" , sum)

avg= sum/n3
print("average of number", avg)