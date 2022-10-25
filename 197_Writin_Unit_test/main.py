def do_stuff(num=0):
	try:
		if num:
			return int(num) + 5
		if num == 0:
			return 0
		else:
			return 'Please, return a number'
	except ValueError as err:
		return err