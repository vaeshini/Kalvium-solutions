import random
class RockPaperScissors:
    score =0
    highest_score = 0
    player_name = ''
    def _init_(self):
        self.player_name = 'Varshini'
        self.highest_score = 0
        self.score = 0
    
    def play(self, player_move):
        moves = ['rock', 'paper', 'scissors']
        computer_move = random.choice(moves)
        
        if player_move == computer_move:
            result = 'draw'
        elif player_move == 'rock' and computer_move == 'scissors':
            result = 'win'
        elif player_move == 'scissors' and computer_move == 'paper':
            result = 'win'
        elif player_move == 'paper' and computer_move == 'rock':
            result = 'win'
        else:
            result = 'lose'
        
        if result == 'win':
            self.score += 1
            if self.score > self.highest_score:
                self.highest_score = self.score
        
        return (self.player_name, player_move, computer_move, result)
    
    def get_score(self):
        return self.score
    
    def get_highest_score(self):
        return self.highest_score
game = RockPaperScissors()


while True:
    player_move = input('Enter your move (rock, paper, or scissors), or type q to quit: ')
    if player_move == 'q':
        break
    
    result = game.play(player_move)
    print(result)
    print('Current score:', game.get_score())
    print('Highest score:', game.get_highest_score())

print('Highest score:', game.get_highest_score())