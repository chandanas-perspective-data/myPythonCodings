def palindromic_date(date):
    d, m, y = date.split('/')
    return (d+m)[::-1] == y and (m+d)[::-1] == y


print (palindromic_date("02/02/2020"))