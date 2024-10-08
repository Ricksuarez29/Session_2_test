# Exercise 2: Basic Data Filtering 
#1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats. 
#2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list.
#3. Print the New List: Output the filtered list of integers.

mixed_data= [5,10,8,'hello','ricardo',2.5,5.1,'barcelona',2]

new_list=[]
for i in mixed_data:
    if type(i) == int:
        new_list.append(i)
## way to do it shorter: new_list = [x for x in mixed_data if type(x) == int]

print(new_list)