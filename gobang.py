import random
import numpy as np
from consts import *

class GoBang(object):
    def __init__(self):
        self.chessMap = [[ChessboardState.EMPTY for j in range(N)] for i in range(N)]
        self.currentI = -1
        self.currentJ = -1
        self.currentState = ChessboardState.EMPTY

    def get_valid_position(self):
        validPosition = []
        for i in range(N):
            for j in range(N):
                if self.chessMap[i][j] == ChessboardState.EMPTY:
                    validPosition.append((i,j))
        return validPosition

    def get_chessMap(self):
        return self.chessMap

    def get_chessboard_state(self, i, j):
        return self.chessMap[i][j]

    def set_chessboard_state(self, i, j, state):
        self.chessMap[i][j] = state
        self.currentI = i
        self.currentJ = j
        self.currentState = state

    def get_chess_result(self):
        if self.have_five(self.currentI, self.currentJ, self.currentState):
            return self.currentState
        else:
            return ChessboardState.EMPTY

    def count_on_direction(self, i, j, xdirection, ydirection, color):
        count = 0
        for step in range(1, 5): 
            if xdirection != 0 and (j + xdirection * step < 0 or j + xdirection * step >= N):
                break
            if ydirection != 0 and (i + ydirection * step < 0 or i + ydirection * step >= N):
                break
            if self.chessMap[i + ydirection * step][j + xdirection * step] == color:
                count += 1
            else:
                break
        return count

    def have_five(self, i, j, color):
        directions = [[(-1, 0), (1, 0)], \
                      [(0, -1), (0, 1)], \
                      [(-1, 1), (1, -1)], \
                      [(-1, -1), (1, 1)]]

        for axis in directions:
            axis_count = 1
            for (xdirection, ydirection) in axis:
                axis_count += self.count_on_direction(i, j, xdirection, ydirection, color)
                if axis_count >= 5:
                    return True

        return False

    def print_chess_map(self):
        strr = ' '
        for index in range(N + 1):
            if index < 9:
                strr = strr + str(index) + '  '
            else:
                strr = strr + str(index) + ' '
        print(strr)
        
        numOfLine = 1
        for line in self.chessMap:
            if numOfLine < 10:
                strr = ' ' + str(numOfLine) + '  '
            else:
                strr = str(numOfLine) + '  '
            for grid in line:
                strr = strr + grid + '  '
            print(strr)
            numOfLine = numOfLine + 1
    
    def get_map_feature(self):
        res = np.zeros(225)
        for index_i in range(N):
            for index_j in range(N):
                if self.chessMap[index_i][index_j] == ChessboardState.WHITE:
                    res[index_i * N + index_j] = 1
                elif self.chessMap[index_i][index_j] == ChessboardState.BLACK:
                    res[index_i * N + index_j] = 2
        return res
