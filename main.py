import random

# ======================
# PLAYER CLASS
# ======================
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.inventory = ["potion"]
        self.coins = 0

    def show_stats(self):
        print(f"\n{self.name} | HP: {self.health} | ATK: {self.attack} | Coins: {self.coins}")
        print("Inventory:", self.inventory)


# ======================
# ENEMY CLASS
# ======================
class Enemy:
    def __init__(self):
        self.name = random.choice(["Goblin", "Orc", "Skeleton"])
        self.health = random.randint(30, 60)
        self.attack = random.randint(5, 15)


# ======================
# FUNCTIONS
# ======================

def fight(player):
    enemy = Enemy()
    print(f"\n⚔️ A wild {enemy.name} appears!")

    while enemy.health > 0 and player.health > 0:
        print(f"\nEnemy HP: {enemy.health}")
        print("1. Attack")
        print("2. Use Potion")

        choice = input("> ")

        if choice == "1":
            damage = player.attack + random.randint(0, 5)
            enemy.health -= damage
            print(f"You hit {enemy.name} for {damage} damage!")

        elif choice == "2":
            if "potion" in player.inventory:
                player.health += 20
                player.inventory.remove("potion")
                print("You used a potion! +20 HP")
            else:
                print("No potions left!")

        else:
            print("Invalid choice!")

        # Enemy attacks
        if enemy.health > 0:
            damage = enemy.attack
            player.health -= damage
            print(f"{enemy.name} hits you for {damage} damage!")

    if player.health > 0:
        print(f"\n✅ You defeated {enemy.name}!")
        player.coins += random.randint(10, 30)
    else:
        print("\n💀 You died...")


def find_treasure(player):
    reward = random.choice(["coins", "potion"])
    if reward == "coins":
        amount = random.randint(10, 50)
        player.coins += amount
        print(f"\n💰 You found {amount} coins!")
    else:
        player.inventory.append("potion")
        print("\n🧪 You found a potion!")


def save_game(player):
    with open("save.txt", "w") as f:
        f.write(f"{player.name},{player.health},{player.attack},{player.coins},{'|'.join(player.inventory)}")
    print("Game saved!")


def load_game():
    try:
        with open("save.txt", "r") as f:
            data = f.read().split(",")
            player = Player(data[0])
            player.health = int(data[1])
            player.attack = int(data[2])
            player.coins = int(data[3])
            player.inventory = data[4].split("|") if data[4] else []
            print("Game loaded!")
            return player
    except:
        print("No save file found!")
        return None


# ======================
# MAIN GAME LOOP
# ======================

def game():
    print("=== 🏰 Dungeon Escape ===")

    print("1. New Game")
    print("2. Load Game")

    choice = input("> ")

    if choice == "2":
        player = load_game()
        if player is None:
            name = input("Enter your name: ")
            player = Player(name)
    else:
        name = input("Enter your name: ")
        player = Player(name)

    # MAIN LOOP
    while player.health > 0:
        player.show_stats()

        print("\nChoose action:")
        print("1. Explore")
        print("2. Inventory")
        print("3. Save & Exit")

        choice = input("> ")

        if choice == "1":
            event = random.choice(["enemy", "treasure", "nothing"])

            if event == "enemy":
                fight(player)
            elif event == "treasure":
                find_treasure(player)
            else:
                print("\nNothing happened...")

        elif choice == "2":
            print("\nInventory:", player.inventory)

        elif choice == "3":
            save_game(player)
            break

        else:
            print("Invalid choice!")

    if player.health <= 0:
        print("\nGame Over 💀")


# ======================
# RUN GAME
# ======================
if __name__ == "__main__":
    game()