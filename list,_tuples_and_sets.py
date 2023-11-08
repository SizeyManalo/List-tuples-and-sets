# -*- coding: utf-8 -*-
"""list, tuples and sets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Ry0PAc0yPbWGqnY_LL3bYxrFNm7XhEY

# Lists, Tuples, Sets and Dictionaries

## 1) List
"""

#List - ordered sequence of elements, always uses [] to represent the list. Each item is seperated by ,.

food = ["pizza","burger","rice", "noodles"]
print(food)

print(food[0])

# to add element in list
food.append("cake")
print(food)

food.append("sandwhich")
print(food)

food.extend(["sandwhich","pasta"])
print(food)

food.extend(["sandwhich","pasta"])
food

print(food*2)

food + ["coffee","tea"]
food

food = food + ["coffee","tea"]
food

food[1:3]

food[3]= 'Sweet'
food

food.index('cake')

food.insert(3,'Paratha')
food

drinks = food.remove('tea')
print(drinks)

onlyfood = food.remove('tea')
print(onlyfood)

xyz = food.remove("coffee")
print(xyz)

print(food)

menu = ['pizza', 'burger', 'rice', 'noodles', 'icecream', 'juice']
print(menu)

print('initial menu', menu)
menu.reverse()
print('reversed menu', menu)
print(type(reversed(menu)))

print('initial menu', menu)
menu.sort()
print('sorted menu',menu)

del menu[-2]
menu

print(menu[2:4])

menu.remove(['juice','noodles'])
print(menu)

print(menu)

menu.remove('juice')
print(menu)

print(menu)

menu.remove('icecream','noodles')
print(menu)

menu_2 = ['pizza','burger', 'rice', 'noodles','icecream']
print(menu_2)

menu_2.pop()

menu_2.clear()
print(menu_2)

"""## 2) Tuples"""

# Tuples - same as list, both contains sequence of items, mixed data types, and it contains individual elements also it is
# immutable, it represents by ().

empty = ()
print("empty tuple",empty)

# to create int tuple
int = (2,1,3,4,5)
print(int)

#mix tuple
mix = (4,"Python",4.2)
print(mix)

# nested tuple
nested = ('python', ["int","data","float"], 100)
print(nested)

str1 = "Python Prog",
print(str1)

Country = ("USA", "China", "Philippine", "India")
print(Country)

Country[2]="Singapore"
print(Country)

del Country[1]

Country + ("Singapore","Japan")
print(Country)
Country1 = Country + ("Singapore","Japan")
print(Country1)

Country1.count('China')

ex1 = ('a','p','y','t','h','o','n','a','y')
print(ex1.count('a'))

print(ex1.index('y'))

# to check an item available in tuple or not
print("Australia" in Country1)

print("Singapore" in Country1)

del Country1

print(Country1)



"""## 3. Sets"""

# Sets - collection of items which are not in order
# but we cannot change the items in set but we can the add or remove
# Elements cannot be duplicated
# also there is no indexing or slicing
# useig {}, Union, Intersections, difference

temp = [['Mary',101,26],
        ['Alex',102,27]]
print(temp)

countries = {'USA', 'China', 'Philippine', 'India', 'Singapore', 'Japan'}
print(countries)
print(type(countries))

print(len(countries))

# adding an element
countries.add("Germany")
print(countries)

#deleting the element
countries.discard("Germany")
print(countries)

# Other Sets Operations
country_1 = {'USA', 'China', 'India', 'Japan', 'Singapore', 'Philippine'}
country_2 = {"India",'Singapore','Germany','Indonesia'}
Setof_Country= country_1.union(country_2)
print(Setof_Country)

print(country_1 | country_2)

# intersection
print(country_1.intersection(country_2))

print(country_1 & country_2)

print(country_2.difference(country_1))
print(country_1.difference(country_2))

set_ex = {11,22,67,54}
output_set = 78 in set_ex
print(output_set)

output_set = 78 not in set_ex
print(output_set)

# Upfating the set
country_2 = {"India",'Singapore','Germany','Indonesia'}
update_set = {'Africa','Malaysia','India'}
country_2.update(update_set)
print(country_2)

country_2.clear()
print(country_2)

"""## 4) Dictionary"""

# Dictionary - collection of elements, keys and values pair, key and value are separated by :.
# it is mutable and unordered,
# if we want to access the elements then we use key

emp_dict = {'Name':'john','age':25,'Dept':'sales'}
print(emp_dict)

print(emp_dict['Name'])

emp_dict['age']=29
print(emp_dict['age'])

print(len(emp_dict))

key = emp_dict.keys()
print(key)

emp_dict

emp_dict = {'Name':'john','age':25,'Dept':'sales','Dept': 'HR'}
print(emp_dict)

print(type(emp_dict))

emp = dict(name='Mary',age=25,id=101)
print(emp)

v = emp.values()
print(v)
print(emp.items())
print()

# Nested Dictionary

Company = {'emp1':{'name':'Daniel','year':2018},
           'emp2':{'name':'Jimmy','year':2020},
           'emp3':{'name':'John','year':2022}}
print(Company)

del emp['age']
print(emp)

print(emp.pop('id'))

emp.clear()

del emp
print(emp)

empName = Company['emp1']['name']
print(empName)
