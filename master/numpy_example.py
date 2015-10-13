from pyspark import SparkContext
import numpy as np #Spark has numpy for python.

def run(sc):
	data = [np.arange(0, 99), np.arange(100, 200) ]
	distData = sc.parallelize(data)

	def sumData(x):
		return np.sum(x)

	mappedSum = distData.map( sumData )
	return mappedSum.reduce(lambda a, b: a + b)

if __name__ == '__main__':
	print run(SparkContext() )
