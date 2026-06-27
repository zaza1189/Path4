class Draw:
    def __init__(self, cards, draw_id=""):
        self.cards = cards
        self.draw_id = draw_id

    def __repr__(self):
        return f"{self.draw_id}: {' '.join(self.cards)}"


class PathEngine:

    def __init__(self):
        self.draws = []

    def load_draws(self, filename):
        self.draws = []

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                cards = line.split()

                if len(cards) != 4:
                    continue

                self.draws.append(Draw(cards))

    def total_draws(self):
        return len(self.draws)

    def print_draws(self):
        print("=== Draws ===")

        for i, draw in enumerate(self.draws):
            print(f"{i+1:02d}. {' '.join(draw.cards)}")


if __name__ == "__main__":

    engine = PathEngine()

    engine.load_draws("draws.txt")

    print()

    print("Path4 Engine")

    print("----------------")

    print(f"Draws loaded: {engine.total_draws()}")

    print()

    engine.print_draws()
