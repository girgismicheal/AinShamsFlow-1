import numpy as np


class Dataset:
	def __init__(self, x=None, y=None):
		if x is not None:
			self.data = np.array(x)
		else:
			self.data = None

		if y is not None:
			self.target = np.array(y)
		else:
			self.target = None

	def __str__(self):
		pass

	def __bool__(self):
		pass

	def __len__(self):
		pass

	def __iter__(self):
		self.index = 0
		return self

	def __next__(self):
		if self.data is not None and self.target is not None:
			x = self.data[self.index]
			y = self.target[self.index]
			self.index += 1
			return x, y

		elif self.data is not None:
			x = self.data[self.index]
			self.index += 1
			return x
		
	def apply(self, transformation):
		pass

	def numpy(self):
		dataset=list()
		for i in range(len(self.data)):
                      dataset.append([self.data[i],self.target[i]])
                return np.array(dataset)                                                                                                                                                      
        
	def batch(self,batch_size,drop_reminder=True):
		i = 0
		dt = list()
		targ = list()
		sz = len(self.data)
		if drop_reminder==True:
			sz-=sz%batch_size
		while i < sz:
			t=i
			i+=batch_size
			dt.append(self.data[t:i])
			targ.append(self.target[t:i])
		self.data=np.array(dt)
		self.target=np.array(targ)
        
	def cardinality(self):
		""" Returns the number of data points in the dataset """
		assert self.data is not None
		return self.data.shape[0]

	def concatenate(self):
		pass

	def enumerate(self):
		pass

	def filter(self):
		pass

	def map(self,func):
		ds=[]
		for element in self.data:
			ds.append(func(element))
		self.data=np.array(ds)


	def range(self, *args):
		self.data = np.arange(*args)

	def reduce(self):
		pass

	def shuffle(self):
		""" Arrays shuffled in-place by their first dimension - nothing returned """

		assert self.data is not None

		# Generate random seed
		seed = np.random.randint(0, 2 ** (32 - 1) - 1)

		if self.target is not None:
			# Ensure self.data and self.target have the same length along their first dimension
			assert self.data.shape[0] == self.target.shape[0]

			# Shuffle both arrays in-place using the same seed
			for array in [self.data, self.target]:
				# Generate random state object
				r_state = np.random.RandomState(seed)
				r_state.shuffle(array)

		else:
			# Generate random state object and only shuffle the data array
			r_state = np.random.RandomState(seed)
			r_state.shuffle(self.data)

	def skip(self):
		pass
	
	def take(self,limit):
		return self.data[:limit]
	
	def split(self, split_percentage, shuffle=False):

		"""
		Splits the dataset into 2 batches (training and testing/validation)

			Inputs:
				- split_percentage: (float) percentage of the testing/validation data points
				- shuffle:			(bool)	if true, the data is shuffled before the split

			Returns (as numpy arrays):
				- If the dataset was initialized with x only:	returns x_train, x_test
				- If the dataset was initialized with x and y:	returns x_train, y_train, x_test, y_test
		"""

		assert self.data is not None
		holdout = int(split_percentage * self.data.shape[0])
		if shuffle:
			self.shuffle()

		x_test = self.data[:holdout]
		x_train = self.data[holdout:]

		if self.target is not None:
			y_test = self.target[:holdout]
			y_train = self.target[holdout:]
			return x_train, y_train, x_test, y_test
		return x_train, x_test


	def unbatch(self):
		pass

	def zip(self):
		pass
	
	def normalize(self):
		pass


class ImageDataGenerator(Dataset):
	def __init__(self):
		pass

	def flow_from_directory(self, directory):
		pass


if __name__ == '__main__':
        ds = Dataset()
        x = np.array([[1,3,2],[1,5,6],[8,1,9],[9,3,2],[9,8,1],[5,2,3],[7,1,5]])
        y= np.array([1,3,1,2,3,4,5])
        ds = Dataset(x,y)
        ds.batch(3)
        print(ds.numpy())
