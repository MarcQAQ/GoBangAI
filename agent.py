import random
from gobang import GoBang
import keras
from keras.models import load_model
import tensorflow
from consts import *

class GobangAI():

    def __init__(self, gobang, ai_color):
        self.gobang = gobang
        self.color = ai_color
        self.model = load_model('pre_knowledge.model')

    def play(self):
        vaildPosition = self.gobang.get_valid_position()
        res = self.model.predict(self.gobang.get_map_feature().reshape(-1,15,15,1))
        print(vaildPosition)
        position_played = None
        tmp = 0
        for position in vaildPosition:
            (i, j) = position
            if res[0][i * N + j] > tmp:
                tmp = res[0][i * N + j]
            position_played = position
        return position_played
