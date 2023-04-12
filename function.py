# CREATING
def greeter():
    print("good morning !..it is a beautiful day ye ye")

# invoking / calling
greeter()

# function that returns
def mult():
    x = 2
    y = 1
    z = 3
    return x * y * z
# invoke
g =mult() / 4
print("  from the function", mult())
print(" outside compute",g)

student_names = []
for i in range(mult()):
    names=  input(" ENTER STUDENT NAMES ")
    student_names.append(names)

print(student_names)

# parameterized functions
def n_AP(a,n,d=3):
    tn = a + (n-1)* d
    return  tn

y= n_AP( 2, 10, 7)
x = n_AP(3, 4 , 1) * 2
print(y)
print(n_AP( 2, 10, 3))
print(x)

