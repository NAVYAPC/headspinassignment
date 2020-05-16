

n=int(input('Enter the upper limit '))
for num in range (1,n+1):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+(digit**3)
        temp=temp/10
    if num==sum:
        print(num)
