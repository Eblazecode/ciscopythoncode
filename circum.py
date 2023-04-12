x = 10
y= 12
age =  [12, 23, 15, 13]
# access a list
x = age[1] + age[3]
print(x)
if age[2] > age[3]:
    print(age[2], " is  greater")
else:
    print(age[3], "is the greatest")
# slicing a list
y = age[:3]
print(y)
# mutability
age[3]= 59
print(age)

# TUPLES
food= ("rice", "beans", "garri", "cassava")
# acessing
food_x = food[0]
print(food_x)
# immutability
# food[2]= "milo"
print(food)

# looping a list
for i in age:
    print(i)
# sum the items
t_sum = 0
for x in age :
    t_sum += x
print(t_sum/4)
# DICTIONARY
veritas_uni = {
    # KEY : VALUE
    "name": "veritas uni Abuja",
    "date" : 2002,
    " faculties": ["NAS", "SOCIAL SCI", "HEALTH SCI", "LAW","BUSI ADMIN"],
    "students": 1000,
    "dept": {
        "NAS": ["CIT", "CHEM", "SOFT ENGR", "MCB","BIO CHEM"],
        "SOCIAL SCI": ["POL SCI", "ECO", "PEACE & CON", "MASS COMM"],

    },
    1: "OUR WINNING SIDE"

}

print(veritas_uni)
# accessing a dict
z = veritas_uni[" faculties"]
print(z)
for i in veritas_uni[" faculties"]:
    if i== "NAS":
        print(" this is my faculty ")
    print(i)

# getting keys .keys()
x = veritas_uni.keys()
print(x)
# dict val
z = veritas_uni.values()
# mutability
veritas_uni["name"] = "VERITAS UNIVERSITY BWARI ABUJA".lower()
veritas_uni.update({'date': 2008})
print(veritas_uni)
veritas_uni[" faculties"][0]= " NATURAL AND APPLIED SCIENCES ".capitalize()

# removing item
#veritas_uni.pop("")
print(veritas_uni.items())

# LOOPING
#keys
for x in veritas_uni:
    print("the keys",x)

#using keys to get values
print("these are the val")
for j in veritas_uni:
    print(veritas_uni[j])

for z in veritas_uni.values():
    print(z)

# copying a dict
nig_uni = veritas_uni.copy()

#populating a dictionary
csc105 = {}
for l in range(6):
    x_keys = input(" ENTER THE KEYS ")
    y_val = input("ENTER THE VALUE ")
    csc105.update({
        x_keys,y_val
    })

for m,k in csc105.items():
    print(m,k)
