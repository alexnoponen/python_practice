#Write a function that computes the volume of a sphere given its radius.

def vol(rad):
	return (4/3)*(3.14)*(rad**3)

#Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num,low,high):
	return num in range(low,high+1)

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
	lowercase = 0
	uppercase = 0

	for char in s:
		if char.isupper():
			uppercase += 1
		elif char.islower():
			lowercase += 1
		else:
			pass
	print(f"Original String: {s}")
	print(f"Uppercase count: {uppercase}")
	print(f"Lowercase count: {lowercase}")

#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
	return list(set(lst))

#Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
	total = 1
	for num in numbers:
		total = total * num
	return total

#Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
	#remove string spaces
	s = s.replace(' ','')
	#check if string is == reversed version

	return s == s[::-1]


#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
	
	#create a set of the alphabet
	alphaset = set(alphabet)
	#remove any spaces from the input string
	str1 = str1.replace(' ','')
	#convert all into lowercase
	str1 = str1.lower()
	#grab all unique letters from the string set
	str1 = set(str1)
	#alphabet set == string set input
	return str1 == alphaset














