
# sets
# dict

# set
# collection of data 

# unordered

a = {1,2,3,4}
b = {3,2,4,1}
print(a == b)

# unindexed

# print(a[0])

# containing no duplicates values

a = {1,2,3,4,5,1,2,3,6,7,4,3,2,8,9,1,5}
print(a)
b = set
b = {3,2,1,4}

fruits = {"mango","orange","apple","pinnapple","watermelon","grapes","banana"}
for i in fruits:
    print(i)

# mutable

# union
# intersection
# difference

a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}

print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a&b)

print(a-b)
print(b-a)

# Dictionary

# keyvalue paired datatype
# key:"value" 

# unindexed

userdata = {"name":"mohan", "age": 27, "location":"kochi" }
print (userdata["age"])
print (userdata["location"])

# mutable

data = {}
data["name"] = "das"
data["age"] = 27
data["email"] = "das@123.com"
data["location"] = "kochi"
data["phone"] = 987654321
data["name"] = "priya"
print(data)


data = {'name': 'priya', 'age': 27, 'email': 'das@123.com', 'location': 'kochi', 'phone': 987654321, 'name': 'das'}
print(data)

# restriction
# 1.keys are unique
# 2.keys are immutable type





# --------inbuilt function----------

a = {"name":"mohan","age": 30,"location":"kochi"}

# print(a.get("name"))
# print(a["name"])

# print(a.keys()) #collection of keys
# print(a.values())
# print(a.items())

a.update({'age': 34})
a.update({'phone': 987654321})
a['age']=50


a.pop("name")
a.popitem()
a.clear()

print(a)

data =  {"name":"mohan","age": 30,"location":"kochi"}

# for i in data:
#     print(i,data[i])

for i,j in data.items():
    print(i,j)




