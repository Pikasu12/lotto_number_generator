from resources.game_rule import games
import random

class LuckyNumbers():
    def __init__(self, game_num):
        # Defining the needed variables.
        self.game_num = game_num 
        self.total_pick = int(games[self.game_num]["Max_pick"]) # This is the total number needs by the user which is currently 6.
        self.max_number = int(games[self.game_num]["Max_number"]) # This is the max number that can be chosen randomly.
        
    def generate_number(self):
        temp_numbers = []    # This will hold the randomly generated numbers.
        
        # This will add the generated numbers.
        while len(temp_numbers) < (self.total_pick):
            temp_numbers.append(random.randint(1, self.max_number))

        return temp_numbers