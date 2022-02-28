from arthmetic import *;
'''
Classes can represent real-world objects or abstract ideas. After defining a class, you use it by making an instance, or object,of the class. 
You can make as many instances as you want from one class.
As an example, you might use a class to represent a website user. 
The class would have attributes associated with the user’s username, password, registration date, and more.
Methods would define the actions the user could take, such as registering, authenticating, logging in, and logging out. 
You could then make one instance for each user who registers on the site.
Many external libraries are written as classes, so learn-ing to work with classes makes it easier to work with many existing projects.
'''

ar = Arithmetic()
print(ar.add())
print(ar.divide())
print(ar.remainder())
ar.print_self()

#TODO: create several more instance of the Arithmetic class and add different values

numbers1 = Arithmetic(30, 50)
print(numbers1.add())
print(numbers1.divide())
print(numbers1.remainder())
numbers1.print_self()

numbers2 = Arithmetic(13, 25)
print(numbers2.add())
print(numbers2.divide())
print(numbers2.remainder())
numbers2.print_self()

numbers3 = Arithmetic(18, 78)
print(numbers3.add())
print(numbers3.divide())
print(numbers3.remainder())
numbers3.print_self()