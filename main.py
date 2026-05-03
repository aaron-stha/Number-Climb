import random

print("\n🎮 SELECT DIFFICULTY")
print("1. Easy (1-9)")
print("2. Medium (1-12)")
print("3. Hard (1-15)")

difficulty = input("> ")

if difficulty == "1":
    numbers = list(range(1, 10))

elif difficulty == "2":
    numbers = list(range(1, 13))

elif difficulty == "3":
    numbers = list(range(1, 16))

else:
    print("❌ Invalid choice! Defaulting to Medium.")
    numbers = list(range(1, 13))
best_score = 999

def show_numbers(numbers):
    print(f"\nThe numbers are: {numbers}")


def roll_dice(numbers):
    if max(numbers) <= 6:
        dice1 = random.randint(1, 6)

        print("rolling one dice only because you have less 7 numbers")
        return dice1, 0, dice1
    
    else:
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
    
    if len(user_list) != len(set(user_list)):
        print("Duplicate number is not allowed")
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

    while True:

        if len(numbers) == 0:
            print("\n🔥 YOU WIN!")
            break

        show_numbers(numbers)

        input("\nPress Enter to roll dice...")

        dice1, dice2, total = roll_dice(numbers)

        if dice2 == 0:
            print(f"\n🎲 You rolled {dice1}")
        else:
            print(f"\n🎲 You rolled {dice1} + {dice2} = {total}")

        if not check_possible(total, numbers):

            print("\n💀 GAME OVER")
            print("Final numbers:", numbers)

            score = sum(numbers)
            print("Score:", sum(numbers))

            global best_score

            if score < best_score:
                best_score = score
                print("new best score")

            print(f"your best score was   {best_score}")
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
    agains = again.upper()
    if agains != "Y":
        print("👋 Thanks for playing!")
        break
