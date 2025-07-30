data = {1:"navin", 2:"kiran", 4:"vishnu"}
print(data[1])
print(data[2])
print(data[4])
print(data)
print(data.get(1))
print(data.get(3))
print(data.get(3, "not found"))
print(data.get(4, "not found"))

keys = ["Navin", "Kiran", "Vishnu"]
values = ["Python", "Java", "C++"]
data = dict(zip(keys, values))
print(data)

print(data['Kiran'])
data["Monika"] = "CS"
print(data)

del data["Kiran"]
print(data)

prog = {'js':"atom", "cs":"vs", "python":["pycharm", "sublime"], "java":{"jave":"netbeans", "python":"eclipse"}}

print(prog['python'])
print(prog['python'][1])
print(prog['java']["python"])


num = 5
print(id(num))

name = "vishnu"
print(id(name))

a = 10
b = a
print(id(a))
print(id(b))
k = 10
print(id(k))

a = 9
print(id(a))

k = a
print(id(k))

b = 8
print(id(b))