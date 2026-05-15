ages = [5,25,65,98,32,10,18,45,12,64,18,2,0,39]

i = 0 
list_size = len(ages)
while i < list_size:
    age = ages[i]
    print(f"Current age {age}")
    if age < 18:
        print('Mineur')
    else:
        print("Majeur")
    i = i + 1




# for age in ages:
#     if age < 18:
#         print(age)