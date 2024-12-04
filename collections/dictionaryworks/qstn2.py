

arr=[10,20,30,40,2,3,7,8,9]

# result=even number square
# result=odd numbers cube

even_squre={num:num**2 for num in arr if num%2==0}

print(even_squre)

odd_cube={num:num**3 for num in arr if num%2!=0}

print(odd_cube)

frequancy_count={num:arr.count(num) for num in arr}

print(frequancy_count)