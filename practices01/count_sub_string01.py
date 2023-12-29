long_str = "Hello , hello , hello to the world"
short_str = "hello"
count = 0
long_str = long_str.split()
for word in long_str:
    if (word.lower() == short_str):
        count += 1
print(count)
