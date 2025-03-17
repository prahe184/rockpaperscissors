import random

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for Paper and 's' for scissors :")
    computer = random.choice(['p', 'r', 's'])
    #p>r, s>p, r>s

    if user == computer:
        return "Tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost!"
    
def is_win(player, opponent):
         #return true if player wins
         #p>r, s>p, r>s
         if(player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's'):
          return True
print(play())
         
    
         


