import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import Circle as Circle
import seaborn as sns


class EstimatePi:
    def __init__(self):
        self.current = pd.DataFrame(columns=['current_estimate'])
        self.coordinates = pd.DataFrame(columns=['x', 'y'])
        self.circle = 0
        self.palette = sns.color_palette("flare")

    def generate_points(self):

        for sim in range(self.n_sims):
            sim += 1
            x = np.random.uniform(-1, 1)
            y = np.random.uniform(-1, 1)
            r_squared = np.square(x) + np.square(y)

            self.coordinates = self.coordinates.append({'x': x, 'y': y}, ignore_index=True)

            if r_squared <= 1:
                self.circle += 1

            estimate = self.calc_estimate(sim)
            self.current = self.current.append({'current_estimate': estimate}, ignore_index=True)

    def calc_estimate(self, n_sims):
        pi = 4 * self.circle / n_sims

        return pi

    def estimate(self, n_sims):
        self.n_sims = n_sims
        self.generate_points()

        return self.current['current_estimate'].iloc[-1]

    def plot_area(self):
        y = self.coordinates['x']
        x = self.coordinates['y']

        fig, ax = plt.subplots(figsize=(5, 5))
        # ax.scatter(x, y)
        ax = sns.scatterplot(x=x, y=y, color=self.palette[0], marker="+")
        ax.add_patch(Circle((0, 0), 1, color=self.palette[1], fill=False))
        ax.set_title('Area Plot')
        ax.set_xlabel(None)
        ax.set_ylabel(None)
        rectangle = plt.Rectangle((-1, -1), 2, 2, ec=self.palette[1], fill=False)
        ax.add_patch(rectangle)
        plt.axis('scaled')
        plt.show()

    def plot_estimate(self):
        current = self.current['current_estimate']
        n_sims = range(self.n_sims)

        fig, ax = plt.subplots(figsize=(5, 5))
        ax = sns.lineplot(x=n_sims, y=current, color=self.palette[3])
        ax.set_title('Running Pi Estimate')
        ax.set_ylabel('Estimated Value')
        ax.set_xlabel('Iteration')
        plt.show()

if __name__ == "__main__":
    pi = EstimatePi()
    pi_estimate = pi.estimate(1000)
    pi.plot_area()
    pi.plot_estimate()
    print(pi_estimate)