import random

# ======================
# SETUP
# ======================
numbers = list(range(1, 10))  # 1–9

# ======================
# FUNCTIONS
# ======================

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def show_numbers(nums):
    print("\nAvailable numbers:", nums)

def is_valid_choice(choice, nums, total):
    return sum(choice) == total and all(num in nums for num in choice)

# ======================
# GAME LOOP
# ======================

print("🎲 Welcome to Shut the Box!")

while True:
    if not numbers:
        print("\n🔥 You shut all the numbers! You WIN!")
        break

    show_numbers(numbers)

    dice1, dice2 = roll_dice()
    total = dice1 + dice2

    print(f"\nYou rolled: {dice1} + {dice2} = {total}")

    # Check if any move is possible
    possible = False
    for i in range(1, len(numbers) + 1):
        from itertools import combinations
        for combo in combinations(numbers, i):
            if sum(combo) == total:
                possible = True
                break
        if possible:
            break

    if not possible:
        print("\n💀 No possible moves! Game Over.")
        print("Your remaining numbers:", numbers)
        print("Score:", sum(numbers))
        break

    # Player input
    try:
        choice = input("Enter numbers to remove (space-separated): ")
        selected = list(map(int, choice.split()))

        if is_valid_choice(selected, numbers, total):
            for num in selected:
                numbers.remove(num)
        else:
            print("❌ Invalid move! Try again.")

    except ValueError:
        print("❌ Enter valid numbers!")
