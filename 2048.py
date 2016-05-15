import curses
from random import randrange, choice
from collections import defaultdict

class GameField(object):
def __init__(self, height=4, width=4, win=2048):
    self.height = height       
    self.width = width         
    self.win_value = 2048      
    self.score = 0             
    self.highscore = 0         
    self.reset()               
def reset(self):
  if self.score > self.highscore:
    self.highscore = self.score

  self.score = 0
  self.field = [[0 for i in range(self.width)] for j in range(self.height)]
  self.spawn_new_number()
  self.spawn_new_number()

def spawn_new_number(self):
  new_number = 4 if randrange(100) > 50 else 2
  (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
  self.field[i][j] = new_element

def move():
  def move_row_left(row):
    # squeese non-zeor element together
    def tighten(row):
      new_row = [i for i in row if i !=0]
      new_row += [0 for i in range(len(row) - len(new_row))]
      return new_row
    def merge(row):
      new_row = []
      pair = False
      




def get_user_action(keyword):
  char = 'N'
  while char not in actions_dict:
    char = keyword.getch()
  return actions_dict[char]

#helpers -----------------------------------------
def transpose(field):
    return [list(row) for row in zip(*field)]
def invert(field):
    return [row[::-1] for row in field]
def is_win(self):
    return any(any(i >= self.win_value for i in row) for row in self.field)
def is_gameover(self):
    return not any(self.move_is_possible(move) for move in actions)


#-------------------------------------------------



def main(stdsrc):
  def init():
    game_fieldreset()
    return 'Game'

  def not_game(state):
    game_field.draw(stdscr)

    #get input from user
    action = get_user_action(stdscr)

    #default current game state
    response = defaultdict(lambda:state)
    response['Restart'] = 'Init'
    response['Exit'] = 'Exit'

    return response[action]

  def game():
    game_field.draw(stdscr)

    #get input from user
    action = get_user_action(stdscr)

    if action == 'Restart':
      return 'Init'
    if action == 'Exit':
      return 'Exit'
    if game.move(action):
      if game_field.is_win():
        return 'Win'
      if game_field.is_lose():
        return 'Gameover'

    return 'Game'


    state_actions = {
      'Init': init,
      'Win': lambda: not_game('Win'),
      'Gameover': lambda: not_game('Gameover'),
      'Game': game
    }

    curses.use_default_colors()
    game_field = GameField(win=32)

    state = 'Init'

    while state != 'Exit':
      state = state_actions[state]()

curses.wrapper(main)
