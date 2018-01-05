
from sys import exit
from consts import *
from gobang import GoBang
from render import GameRender
from agent import GobangAI

if __name__ == '__main__': 
    gobang = GoBang()
    flag = input('Do you want to play first/black? Input y for yes, other characters for no: ')
    ai_color = ChessboardState.BLACK
    if flag == 'y':
        ai_color = ChessboardState.WHITE
    render = GameRender(gobang, ai_color)
    while not render.if_end():
        render.play_chess()
        render.switch_palyer()
    render.switch_palyer()
    render.show_result()
