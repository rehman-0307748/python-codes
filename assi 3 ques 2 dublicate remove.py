# bseds 22032 
# Abdul Rehman 
# question # 2

def Duplicate_Remove(mylist): 
    final_list = [] 
    for num in mylist: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
mylist= [2, 4, 10, 20, 5, 2, 20, 4] 
print(Duplicate_Remove(mylist))
