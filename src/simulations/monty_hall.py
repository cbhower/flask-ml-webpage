import numpy as np
import pandas as pd


class MontyHallSimulation:
    def __init__(self, n_doors: int, n_sims: int):
        self.n_doors = n_doors
        self.first_guess_history = pd.DataFrame(columns=['score'])
        self.second_guess_history = pd.DataFrame(columns=['score'])
        self.n_sims = n_sims
        self.prize_door = np.random.randint(0, self.n_doors)

    def make_guess(self):
        return np.random.randint(0, self.n_doors)

    def reveal_goat(self, guess: int):
        goat = np.random.randint(0, self.n_doors)
        while goat == self.prize_door or goat == guess:
            goat = np.random.randint(0, self.n_doors)
        return goat

    def check_if_guess_is_correct(self, guess: int):
        if guess == self.prize_door:
            return True
        else:
            return False

    def calculate_scores(self):
        first_instinct = float(self.first_guess_history.sum(axis=0) / self.n_sims)
        second_guess = float(self.second_guess_history.sum(axis=0) / self.n_sims)

        return first_instinct, second_guess

    def run_sim(self):
        iteration = 0
        while iteration < self.n_sims:
            guess = self.make_guess()
            goat = self.reveal_goat(guess)

            if self.check_if_guess_is_correct(guess):
                self.first_guess_history = self.first_guess_history.append({'score': 1}, ignore_index=True)
            else:
                pass

            second_guess = self.make_guess()
            while second_guess == goat or second_guess == guess:
                second_guess = self.make_guess()

            if self.check_if_guess_is_correct(second_guess):
                self.second_guess_history = self.second_guess_history.append({'score': 1}, ignore_index=True)
            else:
                pass

            iteration += 1


if __name__ == "__main__":
    mh = MontyHallSimulation(3, 100)
    mh.run_sim()
    first, second = mh.calculate_scores()
    print(f" first score is {first}, second score is {second}")
