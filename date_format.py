def format_date(date):
	m, d, y = date.split('/')
	return ''.join((y, d, m))


print (format_date("12/11/2019"))