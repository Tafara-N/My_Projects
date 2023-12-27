#Type Casting - Converting the data type of a value to another data type

x = 3 #(int)
y = 3.0 #(float)
z = "3" #(str)

# Converting y & z to int
print(int(y)) #This provides temporary conversion of y to int

#To provide permanent conversion from 1 type to another it needs reassignement of the variable
y = int(y)
z = int(z)

print(y)
print(z)
