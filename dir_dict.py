import os
from collections.abc import MutableMapping


class DirDict(MutableMapping):
	def __init__(self, path):
		if not os.path.exists(path):
			raise NotExistDirError()
		self.path = path

	def __len__(self):
		return len(os.listdir(self.path))

	def __iter__(self):
		for key in os.listdir(self.path):
			yield key

	def __getitem__(self, file):
		file_path = os.path.join(self.path, file)
		if(os.path.exists(file_path)):
			with open(file_path, 'r') as f:
				data = f.read()
			return data
		else:
			raise NotExistFileError()

	def __delitem__(self, file):
		file_path = os.path.join(self.path, file)
		if(os.path.exists(file_path)):
			if(os.path.isfile(file_path)):
				remove(file_path)
		else:
			raise NotExistFileError()

	def __setitem__(self, file, value):
		file_path = os.path.join(self.path, file)
		with open(file_path, 'w') as f:
			f.write(value)

	def clear(self):
		for file in os.listdir(self.path):
			os.remove(os.path.join(self.path, file))

	def values(self):
		return [self.__getitem__(key) for key in os.listdir(self.path)]

	def keys(self):
		return [key for key in os.listdir(self.path)]

	def items(self):
		return [(key, self.__getitem__(key)) for key in os.listdir(self.path)]

	def pop(self, key):
		self.__delitem__(key)
