import random

#print(random.sample(range(1,50),k=6))

numbers=range(1,50)

result_list=random.choices(numbers,k=6)

for result in result_list:
    print(result)