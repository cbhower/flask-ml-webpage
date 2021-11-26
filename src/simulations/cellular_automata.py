import random
import pandas as pd


class CellularAutomata:
    def __init__(self, rule):
        self.rules = self.get_rules(rule)
        self.iterations = 20
        self.cells = 25
        self.buffer = '0'
        self.initial_grid = '00000000001000000000'
        self.state = ''.join(random.choice('01') for i in range(self.cells))
        self.on = '`'
        self.off = '*'

    def run_ca(self):
        grid = pd.DataFrame()
        for i in range(self.iterations):
            # print("Iteration %i:  %s" % (i,
            #                              self.state.replace('0', self.off).replace('1', self.on)))
            grid_entry = self.state.replace('0', self.off).replace('1', self.on)
            self.state = self.buffer + self.state + self.buffer
            self.state = ''.join(self.rules[self.state[i:i + 3]] for i in range(self.cells))
            grid_entry = pd.Series(list(grid_entry))
            grid = grid.append(grid_entry, ignore_index=True)

        return grid

    def get_rules(self, rule):
        if rule == '1':
            return {'000': '0',
                    '001': '1',
                    '010': '1',
                    '011': '1',
                    '100': '0',
                    '101': '1',
                    '110': '1',
                    '111': '0'}
        elif rule == '2':
            return {'000': '0',
                    '001': '1',
                    '010': '0',
                    '011': '1',
                    '100': '1',
                    '101': '0',
                    '110': '1',
                    '111': '0'}
        elif rule == '3':
            return {'000': '1',
                    '001': '0',
                    '010': '1',
                    '011': '1',
                    '100': '0',
                    '101': '0',
                    '110': '1',
                    '111': '0'}
        elif rule == '4':
            return {'000': '1',
                    '001': '0',
                    '010': '1',
                    '011': '0',
                    '100': '1',
                    '101': '0',
                    '110': '1',
                    '111': '0'}
        elif rule == '5':
            return {'000': '0',
                    '001': '1',
                    '010': '0',
                    '011': '1',
                    '100': '0',
                    '101': '0',
                    '110': '0',
                    '111': '1'}
        elif rule == '6':
            return {'000': '1',
                    '001': '0',
                    '010': '1',
                    '011': '1',
                    '100': '0',
                    '101': '0',
                    '110': '1',
                    '111': '0'}


if __name__ == "__main__":
    ca = CellularAutomata('1')
    grid = ca.run_ca()
    print(grid)
