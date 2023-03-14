import random
import time
import json

with open('2program_gra/strings.json') as user_file:
    file_contents = json.load(user_file)

player_hp = 100
player_dmg = random.randint(5, 15)

monster_count = 3
monster_list = []
monster_dmg = random.randint(2, 10)
monster_hp_range = (20, 50)

for i in range(monster_count):
    monster_list.append({
        "name": f"Potwór {i+1}",
        "hp": random.randint(*monster_hp_range),
    })

print(file_contents['history1'])
time.sleep(1)
print(file_contents['history2'])
time.sleep(3)
print(file_contents['history3'])
time.sleep(3)
print(file_contents['history4'])
time.sleep(1)
print(f"Twoje HP: {player_hp}")
print(file_contents['task'])

while len(monster_list) > 0 and player_hp > 0:
    print()
    print(file_contents['new_round'])
    print(f"Twoje HP: {player_hp}")

    for i, monster in enumerate(monster_list):
        print(f"{i+1}. {monster['name']} (HP: {monster['hp']})")

    choice = input(file_contents['choise_attact'])

    if choice == "q":
        print(file_contents['end'])
        break

    try:
        choice = int(choice)
    except ValueError:
        print(file_contents['error'])
        continue

    if choice < 1 or choice > len(monster_list):
        print(file_contents['error'])
        continue

    monster = monster_list[choice-1]
    print(f"Atakujesz potwora {monster['name']}!")

    monster['hp'] -= player_dmg
    time.sleep(2)
    print(f"Zadałeś {player_dmg} obrażeń.")
    print(f"HP potwora: {monster['hp']}")

    if monster['hp'] <= 0:
        print(f"Potwór {monster['name']} pokonany!")
        monster_list.remove(monster)
        continue
    
    time.sleep(2)
    print(f"{monster['name']} kontratakuje!")

    player_hp -= monster_dmg
    print(f"Zadał ci {monster_dmg} obrażeń.")
    time.sleep(2)
    print(f"Twoje HP: {player_hp}")

if len(monster_list) == 0:
    print(file_contents['win'])
elif player_hp <= 0:
    print(file_contents['lose'])