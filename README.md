# Excel2Lua
excel to Lua table realized with Python



环境Python 3

没安装过Python环境的，需要 控制台安装库一下文件 pip install xxx
	xlrd


新增excel文件时，将excel文件放入excel文件下

并在conv文件夹下创建同名.py文件，用于处理自己所需的lua格式

再在main.py中import进conv中的py文件，并将as后的名字加到conv_file的列表中

无需自己创建lua_file文件夹，脚本自动添加
