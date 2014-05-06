#!/usr/bin/env python
# -*- coding: latin1 -*-

import scipy as sp
import matplotlib.pyplot as plt

# Get data from external file
file = "./data/web_traffic.tsv"
data = sp.genfromtxt(file, delimiter="\t")

# all examples will have three classes in this file
colors = ['g', 'k', 'b', 'm', 'r']
linestyles = ['-', '-.', '--', ':', '-']

# Divide into two lists
x = data[:, 0]
y = data[:, 1]

# Remove NAN
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
fx = sp.linspace(0, x[-1], 1000)


# Plot data in graphics
def plot_data(x, y, models, mx=None, ymax=None, xmin=None):
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title("Web traffic over the last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w * 7 * 24 for w in range(10)], ['week %i' % w for w in range(10)])

    if models:
        if mx is None:
            mx = sp.linspace(0, x[-1], 1000)
        for model, style, color in zip(models, linestyles, colors):
            plt.plot(mx, model(mx), linestyle=style, linewidth=2, c=color)

        plt.legend(["d=%i" % m.order for m in models], loc="upper left")

    plt.autoscale(tight=True)
    plt.ylim(ymin=0)
    if ymax:
        plt.ylim(ymax=ymax)
    if xmin:
        plt.xlim(xmin=xmin)
    plt.grid(True, linestyle='-', color='0.75')
    plt.show()

# Divide data into two blocks, separated at 3.5 weeks
inflection = 3.5 * 7 * 24
xa = x[:inflection]  # before the inflection point
ya = y[:inflection]
xb = x[inflection:]  # after the inflection point
yb = y[inflection:]

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

plot_data(x, y, [fa, fb])
