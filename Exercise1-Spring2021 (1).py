#!/usr/bin/env python
# coding: utf-8

# In[2]:


ice_cream_rating = 4
sleeping_rating = 10
print('Enter your first name:')
first_name = input()
print('Now enter your last name')
last_name = input()

my_name = first_name + last_name

print('Hello, ' + my_name)

happiness_rating = (ice_cream_rating + sleeping_rating)/2
print(my_name + ' has a happiness rating of', happiness_rating)
print(my_name +'\'s ice cream rating is', ice_cream_rating)
print(my_name +'\'s sleep rating is', sleeping_rating)

