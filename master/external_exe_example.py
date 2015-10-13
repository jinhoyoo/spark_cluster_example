from pyspark import SparkContext
from subprocess import call, check_output
import numpy as np #Spark has numpy for python.


def run(sc):
	data = [np.arange(0, 99), np.arange(100, 200) ]
	distData=sc.parallelize(data)
	sc.addFile("/master/sum_of_numbers")

	def sumData(x):
		strCmd = map(str, x)
		strCmd.insert(0, "./sum_of_numbers")
		strResult=check_output(strCmd)
		return int(strResult)

	return distData.map(sumData).reduce(lambda a, b: a + b)

if __name__ == '__main__':
	print run(SparkContext())
