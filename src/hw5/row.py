from cols import Cols

class Row:
	'''
	Parameters:
	t = table
	'''
	def __init__(self, t):


		self.cells = t

	def row(data, t): 
		if data.cols is not None:
			data['rows'] = data['rows'].append(t)
			for _,cols in enumerate([data['cols']['x'], data['cols']['y']]):
				for _, col in enumerate(cols): 
					Cols.add(col, t[col['at']])

		else: 
			data.cols = cols(t)
		return data 
