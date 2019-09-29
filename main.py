
import xlrd
import os
import luaMaker

# 处理表格
def deal_table(table):
	# 每列数据索引
	e_name = table.row_values(0)
	# 数据类型
	types = table.row_values(2)
	result = []
	for r in range(3, table.nrows):
		row = table.row_values(r)
		row_data = {}
		for c in range(0, table.ncols):
			if row[c] or row[c] == 0:
				if types[c] == 'int' or types[c] == 'float' :
					row_data[e_name[c]] = int(row[c])
					
				elif types[c] == 'intarry':
					splites = row[c].split('|')
					array_data = []
					for value in splites:
						array_data.append(int(value))
					row_data[e_name[c]] = array_data

				elif types[c] == 'stringarray':
					splites = row[c].split('|')
					array_data = []
					for value in splites:
						array_data.append(value)
					row_data[e_name[c]] = array_data

				elif types[c] == 'float':
					row_data[e_name[c]] = row[c]

				elif types[c] == 'string':
					if isinstance(row[c], float):
						row_data[e_name[c]] = str(int(row[c])) 
					else :
						row_data[e_name[c]] = row[c] 
			else :
				pass
				
		result.append(row_data)
	return result

# excel表文件路径
excel_file_path = './excel/'

all_data = {}

# 生成索引
def generate_index(file_name):
	(filename, extension) = os.path.splitext(file_name)
	return (filename, extension)



# 读取单个表格
def read_excel(file):
	workbook = xlrd.open_workbook(file)
	print("reading...", file)
	file_name = os.path.basename(file)

	sheet_num = len(workbook.sheet_names())
	this_excel = []
	for index in range(0, sheet_num):
		table = workbook.sheet_by_index(index)
		
		res = deal_table(table)

		this_excel.append(res)
	(filename, extension) = os.path.splitext(file_name)
	all_data[filename] = this_excel


# 读取表格中的数据，存储到内存中
for root, dirs, files in os.walk(excel_file_path) :
	for file in files:
		read_excel(excel_file_path+file)
	


# 新增文件时，需要手动import
import conv.test as conv_test
import conv.opr as conv_opr
import conv.checkin as conv_checkin
# 新增文件时，需要手动将上面的as写入这个list
conv_file = [
	conv_test,
	conv_opr,
	conv_checkin,

]


# 预生成文件的数据
converted_data = {}

# 分发到单独的处理文件
for file in conv_file:
	# os.path.basename(file)
	file_name = os.path.basename(file.__file__)
	
	(filename, extension) = os.path.splitext(file_name)
	converted = file.process(all_data[filename])
	converted_data[filename] = converted


# 生成文件夹
if not os.path.isdir('./lua_file'):
	os.mkdir("./lua_file")
os.chdir('./lua_file')


print("-------------------------------------------------------")

# 生成lua文件
for data in converted_data:
	print("generateing...", data + ".lua")
	fd = open(str(data+'.lua'), mode = 'w', encoding = 'utf-8')
	res_str = 'return '
	res_str += luaMaker.LuaMaker.makeLuaTable(converted_data[data])
	fd.write(res_str)
	fd.close()















