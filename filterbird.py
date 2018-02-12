#filterbird is a image filtering library for opencv3 
#Currently includes 
#number of filters : 6
#developed by shreyas kapale 
#requirements : opencv3 , python 2


import cv2

import math


def baw(img_in, width, height):
	#black and white filter
	columns = width

	rows = height

	for j in range(columns):

		for i in range(rows):

			(g,b,r) = img_in[i,j]

			img_in[i,j] = (0.2126*r+ 0.7152*g + 0.0722*b)

			Matter_return = img_in

	return Matter_return

def bred(img_in, width, height):
	#bloodyred filter
	columns = width

	rows = height

	for j in range(columns):

		for i in range(rows):

			(g,b,r) = img_in[i,j]

			b = 0

			g = 0

			img_in[i,j] = ( g, b, r)

			Matter_return = img_in

	return Matter_return

def mgdt(img_in, width, height):
	#midnight filter
	columns = width

	rows = height

	for j in range(columns):

		for i in range(rows):

			(b,g,r) = img_in[i,j]

			img_in[i,j] = 0.299*r + 0.114*b

			Matter_return = img_in

	return Matter_return

def pkgr(img_in, width, height):
	#pink-green filter
	columns = width

	rows = height

	for j in range(columns):

		for i in range(rows):

			(b,g,r) = img_in[i,j]

			img_in[i,j] = (g,b,r)

			Matter_return = img_in

	return Matter_return

def alien(img_in, width, height):
	#alien filter - green and purple fade
	columns = width

	rows = height

	for j in range(columns):

		for i in range(rows):

			(b,g,r) = img_in[i,j]

			img_in[i,j] = (b,r,g)

			Matter_return = img_in

	return Matter_return

def sunfade(img_in, width, height):
	#greenish sunfade fliter
	columns = width

	rows = height

	for j in range(columns):

		for i in range(rows):

			(b,g,r) = img_in[i,j]

			img_in[i,j] = (g,167,r)

			Matter_return = img_in

	return Matter_return