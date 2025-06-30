
numbers=[3,-1,4,9,7,12,14,28]

def divisible_by4(num):
    if num%4==0:
        return True
    return False    

# map
new_list=map(divisible_by4,numbers)
new_list=list(new_list)
print(new_list)

# lambda

new_result=[]
for i in numbers:
    ans=lambda a: True if(a%4==0) else False
    new_result.append(ans(i))
print(new_result)    
    

    