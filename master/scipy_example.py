from pyspark import SparkContext
from sklearn import datasets, svm

def run(sc):
	iris = datasets.load_iris()
	digits = [ datasets.load_digits(), datasets.load_digits()]


	def learn(x):
		clf = svm.SVC(gamma=0.001, C=100.)
		clf.fit(x.data[:-1], x.target[:-1] )
		return clf.predict(x.data[-1])

	return sc.parallelize(digits).map(learn).collect()


if __name__ == '__main__':
	print run(SparkContext() )
