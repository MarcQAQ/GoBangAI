import random
from gobang import GoBang

class GobangAI():
    
    def __init__(self, gobang, ai_color):
        self.gobang = gobang
        self.color = ai_color

    def play(self):
        vaildPosition = self.gobang.get_valid_position()
        print(vaildPosition)
        return random.choice(vaildPosition)