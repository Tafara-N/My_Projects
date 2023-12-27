import random

# my_num1 = random.randrange(1,10)
# my_num2 = random.randint(1, 10)
# my_num3 = random.random()

# print(my_num1)
# print(my_num2)
# print(my_num3)

# my_list = ("Simon", "Captain", "Micheal", "Munya", "Simeon")
# winner = random.choice(my_list)
# print(winner)

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "H"]
random.shuffle(cards)
print(cards)
