import re

def calc(arr,n1,n2):
    i=0
    sum=0
    while i<=(n2-n1):
        sum=arr[i]+sum
        i=i+1
        
    return sum
    

#arr = [1,2,3,4,5,6]
#sum=0
#sum=calc(arr,1,5)
#print(sum)


def extract(string):
    listNum=[int(x) for x in re.findall('\d+', string)]
    rent=0
    if "an" in string:
        rent=max(listNum)
    else:
        rent=max(listNum)*12
    return rent


#string="le loyer actuel est de 5000,00 euros/an."
#price=extract(string)
#print(price)

def ComputeJoinPoint(n1,n2):
    arr = []
    while n1 != n2:
        stringN1=str(n1)
        stringN2=str(n2)
        
        for i in range(len(stringN1)):
            n1= n1 + int(stringN1[i])
            
        for i in range(len(stringN2)):
            n2= n2 + int(stringN2[i])
            
    return n1   
        
#print(ComputeJoinPoint(471,480))