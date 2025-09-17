import time
import numpy as np
import sys

#delay printing

def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#create a class
class Pokemon:
    def __init__(self, name, types, moves, EVs, health='======================='):
        #save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 #amount of health bars left

    def fight(self, Pokemon2):
        # Allow two pokemon to fight eachother

        # print out the fight info
        print("-----POKEMON BATTLE!!!-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * round(1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        # Consider type advantages
        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.types == k:
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                    #pokemon2 is Strong
                if Pokemon2.types == version[(i + 1) % 3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                    #pokemon2 is weak
                if Pokemon2.types == version[(i + 2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        while (self.bars > 0) and (Pokemon2.bars > 0):
            # print health of each Pokemon at start of turn
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i + 1}.", x)
            index = int(input("Pick a move: "))
            delay_print(f"\n{self.name} used {self.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            for j in range(int(Pokemon2.bars + .1 * int(Pokemon2.defense))):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
            time.sleep(.5)

            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + " has fainted...")
                break

            while True:
                try:
                    index = int(input("Pick a move: "))
                    if 1 <= index <= len(Pokemon2.moves):
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(Pokemon2.moves)}")
                except ValueError:
                    print(f"Please enter a valid {len[index - 1]}")
            delay_print(f"\n{self.name} used {self.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_1_attack)

            # Pkmn2's turn - removed duplicate health display
            print(f"\nGo {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i + 1}.", x)
            index = int(input("Pick a move: "))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            self.bars -= Pokemon2.attack
            self.health = ""

            for j in range(int(self.bars + .1 * self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
            time.sleep(.5)

            if self.bars <= 0:
                delay_print("\n..." + self.name + " has fainted...")
                break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}!")


if __name__ == '__main__':
    #create pokes!!!!!!!!!
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 7})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE': 10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK': 8, 'DEFENSE': 12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK': 4, 'DEFENSE': 2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'ATTACK': 3, 'DEFENSE': 3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK': 2, 'DEFENSE': 4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK': 6, 'DEFENSE': 5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE': 5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK': 4, 'DEFENSE': 6})

    Charmeleon.fight(Charmander)