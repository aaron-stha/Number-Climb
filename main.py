import random

numbers = list(range(1, 13))


def show_numbers(numbers):
    print(f"\nThe numbers are: {numbers}")


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2, dice1 + dice2


def remove_numbers(user_list, total, numbers):

    for num in user_list:
        if num not in numbers:
            print("❌ Invalid number:", num)
            return False

    if sum(user_list) != total:
        print("❌ Numbers do not match dice total")
        return False

    for num in user_list:
        numbers.remove(num)

    print("✅ Move accepted!")
    return True


def check_possible(total, numbers):

    if total in numbers: #checks one input number
        return True

    for i in range(len(numbers)): #checks two number input
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == total:
                return True
        
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                
                if numbers[i] + numbers[j] + numbers[k] == total:
                    return True 

    return False


# ---------------- GAME ----------------

def game():

    numbers = list(range(1, 13))

    while True:

        if len(numbers) == 0:
            print("\n🔥 YOU WIN!")
            break

        show_numbers(numbers)

        input("\nPress Enter to roll dice...")

        dice1, dice2, total = roll_dice()

        print(f"\n🎲 You rolled {dice1} + {dice2} = {total}")

        if not check_possible(total, numbers):
            print("\n💀 GAME OVER")
            print("Final numbers:", numbers)
            print("Score:", sum(numbers))
            break

        # PLAYER INPUT LOOP
        while True:

            print("\nEnter numbers to remove (space separated)")
            user_input = input("> ")

            try:
                user_list = []

                for x in user_input.split():
                    user_list.append(int(x))

                if len(user_list) == 0:
                    print("❌ Enter at least one number!")
                    continue

                if remove_numbers(user_list, total, numbers):
                    break

            except:
                print("❌ Invalid input!")


# ---------------- RESTART ----------------

while True:
    game()

    again = input("\nPlay again? (y/n): ")

    if again != "y":
        print("👋 Thanks for playing!")
        break
