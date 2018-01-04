#!python

import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import seaborn

import sys

def load_percentages(percentage_file):
    percentages = []
    with open(percentage_file) as pfile:
        for line in pfile:
            pct = float(line.strip()[:-1])
            if abs(pct) > 10000.0:
                continue
            percentages.append(pct)
    return numpy.array(percentages)

def generate_histogram(percentages, limit, label):
    percentages = numpy.array([pct for pct in percentages if abs(pct) < limit])
    seaborn_plot = seaborn.distplot(percentages, label=label)
    figure = seaborn_plot.get_figure()
    return figure


seaborn.set_style('whitegrid')

print "Local:"
local_percentages = load_percentages("percentage_deltas/local")
print "Count: %d" % len(local_percentages)
print "mean: %s" % local_percentages.mean()
print "min: %s, max: %s" % (local_percentages.min(), local_percentages.max())
print "std. dev.: %s" % local_percentages.std()
print

print "Cloud:"
cloud_percentages = load_percentages("percentage_deltas/cloud")
print "Count: %d" % len(cloud_percentages)
print "mean: %s" % cloud_percentages.mean()
print "min: %s, max: %s" % (cloud_percentages.min(), cloud_percentages.max())
print "std. dev.: %s" % cloud_percentages.std()

generate_histogram(local_percentages, 40, "Local")
figure = generate_histogram(cloud_percentages, 40, "Cloud")

pyplot.legend()
figure.axes[0].set_xlim(-40, 40)
figure.savefig("histogram.png")

pyplot.clf()

generate_histogram(local_percentages, 10, "Local")
figure = generate_histogram(cloud_percentages, 10, "Cloud")

pyplot.legend()
figure.axes[0].set_xlim(-10, 10)
figure.savefig("histogram_close.png")
