



def process(data):
	# print(data)
	sheet1 = data[0]

	res = {}

	for info in sheet1:
		res[info['opr']] = info['id']

	return res


