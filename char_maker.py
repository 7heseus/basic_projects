from audioop import ratecv
from dataclasses import replace
from msilib.schema import Class

#   LISTS
race_list = ['Dwarf', 'Elf', 'Halfling', 'Human', 
             'Dragonborn', 'Gnome', 'Half-Elf', 
             'Half-Orc', 'Tiefling']
class_list = ['Barbarian', 'Bard', 'Cleric', 
              'Druid', 'Fighter', 'Monk', 'Paladin', 
              'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 
              'Wizard']
align_list = ['LG', 'NG', 'CG', 'LN', 'N', 'CN',
              'LE', 'NE', 'CE']
# do i need this? stat_dict = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

#   DEFINING THE CLASS
class Character:
        
    player_name = 'Jerry'
    char_name = 'Alverior'
    char_alignment = 'NG'
    race = 'Half-Elf'
    char_class = 'Ranger'
    char_level = 1
    profiency = char_level
    stat_dict = {'STR': 10,
                 'DEX': 10,
                 'CON': 10,
                 'INT': 10,
                 'WIS': 10,
                 'CHA': 10}
    skills_list = {}
    
    def print(self):
        print("Player:", self.player_name)
        print("-----", self.char_name, "-----")
        print("Race:", self.race)
        print("Class:", self.char_class)
        print("Alignment:", self.char_alignment)
        print("Level:", self.char_level)
        print(self.stat_dict)

my_char = Character()

#   INQUIRY PROMPT ARRAY
def prompt_array(prompt = 'choose one', list_array = []):
    print(prompt)
    x = 1
    for item in list_array:
        print(' ', x, ') ', item)
        x += 1
    item_num = int(input("> "))
    return list_array[item_num - 1]

#   INQUIRIES
my_char.player_name = input("Enter player name: ")
my_char.char_name = input("Enter your character's name: ")
my_char.race = prompt_array('Choose a race', race_list)
my_char.char_class = prompt_array('Choose a class', class_list)
my_char.char_alignment = prompt_array('Choose your alignment', align_list)
my_char.char_level = input("Enter your level: ")

def stat_array():
    stats_dict = my_char.stat_dict
    for stat in stats_dict:
        print(stat)
        stats_dict[stat] = int(input('> '))

print('Enter a value for your base stats (1-20)')
my_char.skills_list = stat_array()

#   SHEET PRINT
my_char.print()








