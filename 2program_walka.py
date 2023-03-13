import random
import time

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

print("Witaj w grze!")
time.sleep(1)
print("Jesteś śmiałkiem który wszedł do jaskini zła aby wybić wszystkie stwory")
time.sleep(3)
print("Tak naprawdę jeśteś wieśniakiem co chciał pokazać DUŻE kochonez (no ale tak jakoś wyszło)")
time.sleep(3)
print("Zabij lub bądź zabity, powodzenia!")
time.sleep(1)
print(f"Twoje HP: {player_hp}")
print("Twoje zadanie: pokonać wszystkie potwory")

while len(monster_list) > 0 and player_hp > 0:
    print()
    print("Nowa runda:")
    print(f"Twoje HP: {player_hp}")

    for i, monster in enumerate(monster_list):
        print(f"{i+1}. {monster['name']} (HP: {monster['hp']})")

    choice = input("Który potwór zaatakować? (podaj numer lub wpisz 'q' by zakończyć grę): ")

    if choice == "q":
        print("Koniec gry.")
        break

    try:
        choice = int(choice)
    except ValueError:
        print("Nieprawidłowa wartość. Spróbuj ponownie.")
        continue

    if choice < 1 or choice > len(monster_list):
        print("Nieprawidłowa wartość. Spróbuj ponownie.")
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
    print("Brawo, pokonałeś wszystkie potwory! Masz szacun na dzielni oraz status DUŻYCH kochonez")
elif player_hp <= 0:
    print("Niestety, zostałeś zabity a twoja śmierć i tak nikogo nie nauczy a wszyscy cię zapomną. Koniec gry.")