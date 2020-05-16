n=int(input("enter Total Number of terms"))
sum=0
count = 1
for i in range(0,n):
        sum = sum + ((float)(pow(count, 2)) / (float)(pow(count, 3)))
        count += 2
print("sum of the series:",sum)
