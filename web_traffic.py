#!/usr/bin/env python
# -*- coding: latin1 -*-

import scipy as sp
import matplotlib.pyplot as plt

# Get data from external file
file = "./data/web_traffic.tsv"
data = sp.genfromtxt(file, delimiter="\t")

# Divide into two lists
x = data[:, 0]
y = data[:, 1]

# Remove NAN
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

# Show graphics with traffic details
plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()