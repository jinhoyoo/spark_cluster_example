import os
from pyspark import SparkContext
from scipy import special, optimize
from sklearn import svm
from sklearn import datasets
import numpy as np

def run(sc):
	data = range(0, 10000)
	distData = sc.parallelize(data)
	distData.cache()

	accum = sc.accumulator(0)
	distData.foreach( lambda x: accum.add(x) )

	print accum.value


if __name__ == '__main__':
	print run(SparkContext() )
