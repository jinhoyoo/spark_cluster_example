import os
from pyspark import SparkContext
from scipy import special, optimize
from sklearn import svm
from sklearn import datasets
import numpy as np

def run(sc):
	data = range(0, 100)
	distData = sc.parallelize(data)


if __name__ == '__main__':
	print run(SparkContext() )
