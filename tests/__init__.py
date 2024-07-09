import subprocess

def run_command(args):
	"""运行命令行程序并返回输出"""
	result = subprocess.run(
		['python', '-m', "src.log_structured_file_io.main"] + args,
		capture_output=True,
		text=True
	)
	return result
