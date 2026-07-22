numbers=[10,20,30,40]
map_obj=map(lambda n:n+1,numbers)
print(type(map_obj))
new_numbers=list(map_obj)
print(new_numbers)