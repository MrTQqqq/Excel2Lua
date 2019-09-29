
def process(data):
	sheet1 = data[0]
	sheet2 = data[1]

	res = {}
	res['seven_day'] = {}
	for info in sheet1:
		res['seven_day'][info['days']] = info


	res['total'] = {}

	for info in sheet2:
		res['total'][info['day']] = info


	return res


