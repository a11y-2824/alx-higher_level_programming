#!/usr/bin/python3

'''inherit class from base'''

from models.base import Base

'''create a new class'''
class Rectangle:


'''assign private instance attributes with getters and setters'''
'''create a class constructor'''
	def __init__(self, width, height, x=0, y=0, id=None):
	'''call the super class with id from Base class'''
	'''Assign the arguemnts to th attributes'''
	self.width = width
	self.height = height
	self.x = x
	self.y = y
