from consts import *
from gobang import GoBang
from agent import GobangAI


class GameRender(object):
    def __init__(self, gobang, ai_color):
        self.gobang = gobang
        self.ai_color = ai_color
        self.currentPieceState = ChessboardState.BLACK
        self.gobang.print_chess_map()
        self.aiAgent = GobangAI(gobang, ai_color)

    def play_chess(self):

        
        strr = '------------------------ Current Player: '
        if self.currentPieceState == ChessboardState.BLACK:
            strr = strr + ' BLACK '
        else:
            strr = strr + ' WHITE '
        strr = strr + '(' + self.currentPieceState + ') ------------------------'
        
        print(strr)

        if self.currentPieceState == self.ai_color:
            x, y = self.aiAgent.play()
            print('The agent decided to play at (' + str(x + 1) + ', ' + str(y + 1) + ')')
            self.gobang.set_chessboard_state(x, y, self.ai_color)
            self.gobang.print_chess_map()
        else:
            coordinatePlayed = input('Input the coordinate you want to play, seperate with space: ').split(' ')
            x = coordinatePlayed[0]
            y = coordinatePlayed[1]

            valid = True

            try:
                if 1 > int(x) or N < int(x):
                    valid = False
                    print('The coordinate is out of range, please input again')
                if 1 > int(y) or N < int(y):
                    valid = False
                    print('The coordinate is out of range, please input again')
                if not self.gobang.get_chessboard_state(int(x) - 1, int(y) - 1) == ChessboardState.EMPTY:
                    valid = False
                    print('The coordinate is already taken, please input again')
            except BaseException:
                valid = False
                print('The coordinate is not numbers, please input again')

            if valid:
                self.gobang.set_chessboard_state(int(x) - 1, int(y) - 1, self.currentPieceState)
                self.gobang.print_chess_map()
            else:
                self.play_chess()

    def if_end(self):
        if self.gobang.get_chess_result() == ChessboardState.EMPTY:
            return False
        return True

    def show_result(self):
        if self.if_end():
            if self.currentPieceState == ChessboardState.BLACK:
                print('BLACK WINS !!!')
            else:
                print('WHITE WINS !!!')

    def switch_palyer(self):
        if self.currentPieceState == ChessboardState.BLACK:
            self.currentPieceState = ChessboardState.WHITE
        else:
            self.currentPieceState = ChessboardState.BLACK

