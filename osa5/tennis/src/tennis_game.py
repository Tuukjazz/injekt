class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1
        else:
            raise ValueError("Invalid player name")

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_even_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_advantage_or_win_score()
        else:
            return self._get_regular_score()

    def _get_even_score(self):
        if self.m_score1 < 3:
            return self.SCORE_NAMES[self.m_score1] + "-All"
        else:
            return "Deuce"

    def _get_advantage_or_win_score(self):
        minus_result = self.m_score1 - self.m_score2
        if abs(minus_result) == 1:
            leading_player = self.player1_name if minus_result == 1 else self.player2_name
            return f"Advantage {leading_player}"
        else:
            winning_player = self.player1_name if minus_result >= 2 else self.player2_name
            return f"Win for {winning_player}"

    def _get_regular_score(self):
        return f"{self.SCORE_NAMES[self.m_score1]}-{self.SCORE_NAMES[self.m_score2]}"
