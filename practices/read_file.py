try:
    with open("/Users/rutendogono/Desktop/hardy.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("The file you want to open doesn't exist")
except Exception:
    print("Something went wrong while reading the file")
