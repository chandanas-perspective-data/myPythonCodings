
# Define a function that returns commonly shared letters of two strings
def shared_letters(str1, str2):
	return len(set(str1) & set(str2))


print (shared_letters("hello", "python"))