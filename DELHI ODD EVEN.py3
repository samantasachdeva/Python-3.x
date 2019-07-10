#Due to growing Traffic Problem Kejriwal wants to devise a new scheme. The scheme is as follows, each car will be allowed to run on Sunday if the sum of digits which are even is divisible by 4 or sum of digits which are odd in that number is divisible by 3. However to check every car for the above criteria can't be done by the Delhi Police. You need to help Delhi Police by finding out if a car numbered N will be allowed to run on Sunday?


#Input Format: The first line contains N , then N integers follow each denoting the number of the car.

#Constraints:N<=1000, 
#Output Format: N lines each denoting "Yes" or "No" depending upon whether that car will be allowed on Sunday or Not !

N=int(input("how many car numbers?"))
sum1=0 
sum2=0
if N<=1000:
    for j in range(0,N):
        car_no=input("enter the car numbers ")
        for i in car_no:
            if int(i)%2==0:
              sum1=sum1+int(i)
            else:
              sum2=sum2+int(i)
        if sum1%4==0 or sum2%3==0:
            print("yes")
        else:
            print("No")
else:
    print("No")
