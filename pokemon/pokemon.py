
import random

print("Your Pokemon Adventure!")
name = input("What's your name? ")

starters = {
    "1": {"name": "Charmander", "type": "Fire"},
    "2": {"name": "Squirtle", "type": "Water"},
    "3": {"name": "Bulbasaur", "type": "Grass/Poison"}
}

print("\nChoose your starter Pokemon!")
print("1. Charmander")
print("2. Squirtle")
print("3. Bulbasaur")

choice = input("> ")

if choice not in starters:
    choice = "1"

pokemon = starters[choice]["name"]
pokemon_type = starters[choice]["type"]

print(f"\nYou chose {pokemon}!")
print(f"Type: {pokemon_type}")

hp = 30
max_hp = 30
potions = 3
pokeballs = 5
team = [pokemon]

print(f"\n{name}, your adventure begins!")

enemy_data = {
    "Pidgey": ("Normal/Flying", 25),
    "Zubat": ("Poison/Flying", 28),
    "Geodude": ("Rock/Ground", 35),
    "Eevee": ("Normal", 30),
    "Pikachu": ("Electric", 25)
}

enemy = random.choice(list(enemy_data.keys()))
enemy_type, enemy_hp = enemy_data[enemy]
max_enemy_hp = enemy_hp

print(f"\nA wild {enemy} appeared!")
print(f"Type: {enemy_type}")

while hp > 0 and enemy_hp > 0:
    print(f"\n{pokemon}: {hp}/{max_hp} HP")
    print(f"{enemy}: {enemy_hp}/{max_enemy_hp} HP")
    print(f"Potions: {potions} | Pokeballs: {pokeballs}")

    print("\n1. Attack")
    print("2. Use Potion")
    print("3. Throw Pokeball")
    print("4. Run Away")

    move = input("> ")

    if move == "1":
        damage = random.randint(6, 12)
        enemy_hp -= damage
        print(f"{pokemon} attacks for {damage} damage!")

    elif move == "2":
        if potions > 0:
            healing = min(12, max_hp - hp)
            hp += healing
            potions -= 1
            print(f"{pokemon} recovered {healing} HP!")
        else:
            print("You have no potions!")
            continue

    elif move == "3":
        if pokeballs > 0:
            pokeballs -= 1
            chance = 50

            if enemy_hp <= max_enemy_hp // 3:
                chance = 80

            if random.randint(1, 100) <= chance:
                print(f"You caught {enemy}!")
                team.append(enemy)
                break
            else:
                print(f"{enemy} broke free!")
        else:
            print("You have no Pokeballs!")
            continue

    elif move == "4":
        print("You escaped safely!")
        break

    else:
        print("Invalid choice!")
        continue

    if enemy_hp > 0:
        damage = random.randint(3, 8)
        hp -= damage
        print(f"{enemy} attacks for {damage} damage!")

if hp <= 0:
    print(f"\n{pokemon} fainted!")
elif enemy_hp <= 0:
    print(f"\nYou defeated {enemy}!")
    potions += 1
    print("You found a Potion!")

print("\nYour Pokemon Team:")
for member in team:
    print("-", member)

print("\nYour Pokemon Adventure has just only begun! Keep exploring and catching more Pokemon!")
print("\nThank you for playing!")
