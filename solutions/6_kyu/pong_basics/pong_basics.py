"""Artemii Hrynevych
My solution for 6 kyu "Pong! [Basics]" kata
https://www.codewars.com/kata/pong-basics
"""

class Pong:
    def __init__(self, max_score):
        self.max_score = max_score
        self.player_1_score = 0
        self.player_2_score = 0
        self.player_1_turn = True

    def play(self, ball_pos, player_pos):
        print(self.player_1_score, self.player_2_score)
        if self.player_1_score >= self.max_score\
        or self.player_2_score >= self.max_score:
        # if game is already over
            return 'Game Over!'
        if ball_pos >= player_pos-3\
        and ball_pos <= player_pos+3:
            if self.player_1_turn:
                self.player_1_turn = not self.player_1_turn
                return 'Player 1 has hit the ball!'
            else:
                self.player_turn = 1
                self.player_1_turn = not self.player_1_turn
                return 'Player 2 has hit the ball!'
        else:
            if self.player_1_turn:
                self.player_1_turn = not self.player_1_turn
                self.player_2_score += 1
                if self.player_2_score >= self.max_score:
                    return 'Player 2 has won the game!'
                else:
                    return 'Player 1 has missed the ball!'
            else:
                self.player_1_turn = not self.player_1_turn
                self.player_1_score += 1
                if self.player_1_score >= self.max_score:
                    return 'Player 1 has won the game!'
                else:
                    return 'Player 2 has missed the ball!'