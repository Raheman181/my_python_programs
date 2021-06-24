import random
class roller():
    def func(roll):
        l = [1, 2, 3, 4, 5, 6]
        for i in range(roll):
            c = random.choice(l)
            d = random.choice(l)
            print("Both Dices Shuffled",i+1,"times !!")
            print(c,"&&", d)
        choice = input("want to shuffle again!!  y or n ")
        for i in choice:
                 if i == "y":
                     rolle = int(input("enter how many times you want to roll"))
                     roller.func(rolle)
                 else:
                     break
def main():
    roll = int(input("enter how many times you want to roll"))
    cd = roller.func(roll)

if __name__ == '__main__':
    main()