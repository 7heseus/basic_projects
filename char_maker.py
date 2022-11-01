from audioop import ratecv
from dataclasses import replace
from msilib.schema import Class
from math import floor

#   LISTS
race_list = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 
             'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling']
class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter',
              'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 
              'Warlock', 'Wizard']
align_list = ['LG', 'NG', 'CG', 'LN', 'N', 'CN','LE', 'NE', 'CE']
stats_def = { 'STR': ['Athletics'], 
              'DEX': ['Acrobatics', 'Slight of Hand', 'Stealth'],
              'CON': [],
              'INT': ['Arcana', 'History', 'Investigation', 'Nature', 'Religion'],
              'WIS': ['Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival'],
              'CHA': ['Diseption', 'Intimidation', 'Performance', 'Persuasion']}
level_prof_dict = {1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 
                   8: 3, 9: 4, 10: 4, 11: 4, 12: 4, 13: 5, 
                   14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6, 20: 6}

#   DEFINING THE CLASS
class Character:
        
    player_name = 'Jerry'
    char_name = 'Alverior'
    char_alignment = 'NG'
    race = 'Half-Elf'
    char_class = 'Ranger'
    char_level = 1
    stat_dict = {}
    ## stat_dict = {'STR': {'base':15, 'mod':2}}
    stat_prof_list = [False, False, False, False, False, False]
    skills_dict = {}
    skill_prof_list = [False, False, False, False, False, 
                       False, False, False, False, False, 
                       False, False, False ,False, False, 
                       False, False, False]

    @property
    def proficiency(self):
        return level_prof_dict[self.char_level]   

    def set_stats(self):
        for stat in stats_def:
            base = int(input(stat + ' = '))
            self.stat_dict.update({stat: {'base': base, 'mod': round_down((base-10)/2)}})

    def get_base(self, stat = ''):
        return self.stat_dict[stat]['base']

    def get_mod(self, stat = ''):
        stat_value = self.stat_dict[stat]
        mod_value = stat_value['mod']
        return mod_value

    def print(self):
        print("Player:", self.player_name)
        print("-----", self.char_name, "-----")
        print("Race:", self.race)
        print("Class:", self.char_class)
        print("Alignment:", self.char_alignment)
        print("Level:", self.char_level)
        print("Proficiency Bonus:", self.proficiency)
        for stat in self.stat_dict:
            print(stat, self.get_base(stat), '|', self.get_mod(stat), ', '.join(stats_def[stat]))
my_char = Character()

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n * multiplier) / multiplier

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
my_char.char_level = int(input("Enter your level: "))

print('Enter a value for your base stats (1-20)')
my_char.set_stats()

#   SHEET PRINT
my_char.print()








