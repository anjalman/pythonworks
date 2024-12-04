arr=[2,3,4,5,6,7,8]


left=0

right=len(arr)-1

sum=9

while(left<right):

    cur_sum=arr[left]+arr[right]

    #there are 3 case
    #cur_sum==sum
    #cur_sum<sum=left+=1
    #cur_sum>sum=right-=1

    if cur_sum==sum:
        
        print(arr[left],arr[right])

        left+=1
        right-=1

    elif cur_sum>sum:

        right-=1

    elif cur_sum<sum:

        left+=1

