



def process(data):
	
	sheet1 = data[0]

	res = {}

	for info in sheet1:
		res[info['id']] = info

	return res


