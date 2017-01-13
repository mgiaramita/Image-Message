#!/usr/bin/python
import Image 
import sys

def encode(image, msg):
	im = Image.open(image)
	pix = im.load()
	width, height = im.size
	ms = list(open(msg, 'r+').read())

	for i in range(0,height):
		for j in range(0,width):
			if (i * width) + j > len(ms) - 1:
				break;	
			c = ord(ms[(i * width) + j])

			p3 = pix[j,i][2] - (pix[j,i][2] % 10) + (c % 10)
			if p3 > 255:
				p3 -= 10
			c /= 10
			p2 = pix[j,i][1] - (pix[j,i][1] % 10) + (c % 10)
			if p2 > 255:
				p2 -= 10
			c /= 10
			p1 = pix[j,i][0] - (pix[j,i][0] % 10) + c
			if p1 > 255:
				p1 -= 10

			pix[j,i] = (p1,p2,p3)

		if (i * width) + j > len(ms) - 1:
			p3 = pix[j,i][2] - (pix[j,i][2] % 10)
			p2 = pix[j,i][1] - (pix[j,i][1] % 10)
			p1 = pix[j,i][0] - (pix[j,i][0] % 10)
			pix[j,i] = (p1,p2,p3)
			break;

	im.save('./out.png', format='PNG', compress_level=0)

def decode(image, out):
	im = Image.open(image)
	pix = im.load()
	width, height = im.size
	msg = ""
	breakFlag = False

	for i in range(0,height):
		for j in range(0,width):
			p3 = pix[j,i][2] % 10
			p2 = pix[j,i][1] % 10
			p1 = pix[j,i][0] % 10
			val = p1*100 + p2*10 + p3

			if val == 0:
				breakFlag = True
				break;
			try:
				c = chr(val)
			except ValueError:
				c = ""
			msg += c
		if breakFlag:
			break;

	f = open(out, 'w')
	print >> f, msg

def main():
	try:
		flag = sys.argv[1]
		image = sys.argv[2]
		file = sys.argv[3]
	except IndexError:
		print "Invalid args. Correct usage:"
		print "  ImageMessage -[e,d] <imagename> <in/output filename>"
		return -1

	if flag == "-e":
		try:
			encode(image, file)
		except AttributeError:
			print "Invalid image name"
	elif flag == "-d":
		try:
			decode(image, file)
		except AttributeError:
			print "Invalid image name"
	else:
		print "Invalid args. Correct usage:"
		print "  ImageMessage -[e,d] <imagename> <in/output filename>"

if __name__ == "__main__":
	main()
