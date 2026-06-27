# ==========================================
# Path4 - Path Analysis Engine
# Version 0.1
# ==========================================

# ערכי הקלפים האפשריים
CARDS = ["7", "8", "9", "10", "J", "Q", "K", "A"]


class Draw:
    def __init__(self, cards, draw_id=""):
        self.cards = cards
        self.draw_id = draw_id

    def __repr__(self):
        return f"{self.draw_id}: {' '.join(self.cards)}"


class PathEngine:

    def __init__(self):
        self.draws = []

    def add_draw(self, cards, draw_id=""):
        self.draws.append(Draw(cards, draw_id))

    def total_draws(self):
        return len(self.draws)

    def print_draws(self):
        for draw in self.draws:
            print(draw)


if __name__ == "__main__":

    engine = PathEngine()

    print("Path4 Engine Started")
    print("--------------------")
    print("Draws loaded:", engine.total_draws())
