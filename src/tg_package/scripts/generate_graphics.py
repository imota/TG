#!/usr/bin/env python

import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt


def saveFigure(x, y, title, hline):
    fig = plt.figure()
    plt.plot(x, y)
    plt.axhline(y=hline, color='r', linestyle='--')
    plt.ylabel('Pontuacao')
    plt.xlabel('Episodio')
    plt.title(title)
    plt.savefig(title + '_graphic.png')


def get_data(file):
    data = pd.read_csv(file)
    y = data['260.0']
    X = [i for i in range(len(y))]
    return X, y

if __name__ == '__main__':
    X, y = get_data('results_mrspacman_random.csv')
    saveFigure(x=X, y=y, title='Mrs Pacman', hline=213)
