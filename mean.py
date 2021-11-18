
import math



# list of elements to calculate mean
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]


# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)
    mean = total / n
    return mean

mean=mean(data)
sqList=[]
for i in data:
    diff=mean-int(i)
    diff=diff**2
    sqList.append(diff)
sum=0
for i in sqList:
    sum=sum+int(i)
result=sum/(len(data)-1)
sd=math.sqrt(result)
print("after a long calculation we found that the standard deviation is......",sd)