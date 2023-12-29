long_str = "Hello , hello , hello to the world"
short_str = "hello"
count = 0
long_str = long_str.split()
for i in range(len(long_str)):
    if (long_str[i].lower() == short_str):
        count += 1
print(count)
