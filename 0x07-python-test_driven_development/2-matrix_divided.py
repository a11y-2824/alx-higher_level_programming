#!/usr/bin/python3


''' Define the prototype

matrix should be a list of integers or floats

''' 


def matrix_divided(matrix, div):
	''' Raise a TypeError exception if matrix list are not int or float'''
	if (not isinstance(matrix, int) and not isinstance(matrix, float)):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	''' Raise a TypeError exception if matrix rows are different sizes '''
	''' Raise a TypeError exception if div is not an int or float'''
	if (not isinstance(div, int) and not isinstance(div, float)):
		raise TypeError("div must be a number")
	''' Raise a ZeroDivisionError if div==0'''
	if div==0:
		raise ZeroDivisionError("division by zero")
''' All elements should be divided by div and rounded to 2dp'''
matrix % 2 == 0
''' Return a new matrix'''
	return(matrix_divided)
