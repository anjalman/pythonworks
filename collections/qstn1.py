
arr=[100,200,300,400,500]

k=2

for i in range(1,k+1):
    
    poped_elemnt=arr.pop()

    arr.insert(0,poped_elemnt)

print(arr)