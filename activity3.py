#Armstrong number

num=int(input("Enter a number"))

sum=0
temp=num

while temp>0:
    rem=temp%10
    sum+=rem**3
    temp//=10

if num==sum:
    print("Its a Armstrong number")
else:
    print("Its not Armstrong number")
