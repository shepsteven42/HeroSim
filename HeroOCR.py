#!/bin/python
from PIL import ImageGrab
from PIL import Image
import time
import pyautogui
import pytesseract
import cv2
import os
import numpy as np
import threading

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# takes grayscale screenshot of specified bounding box tuple: (X1, Y1, X2, Y2)
def screengrab_as_numpy_array(location):
	im = np.array(ImageGrab.grab(bbox=(location[0], location[1], location[2], location[3])))
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	# cv2.imshow('im', im)
	return(im)

# converts image to binary map, default brightness threshold 145
def tesser_image(image, thresh=145):	
	image = cv2.resize(image, (0,0), fx=2, fy=2)
	ret, image = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)
	# cv2.imshow('im', image)
	# cv2.waitKey(0)
	image = Image.fromarray(image)
	txt = pytesseract.image_to_string(image)
	return(txt)

# Boolean, detects when the spell menu is on-screen
def is_spell_menu():
	coords = (1246,596,1264,631)
	im = screengrab_as_numpy_array(coords)
	avg = np.mean(im)
	if avg < 100:
		return True
	else:
		return False

# takes screenshots from capture window and saves to file
def grab_screens(N, filelist):
	start_time = time.time()
	prev = True
	curr = True
	success = 0
	trigger = False
	while success < N:
		# set triger if previous frame was light and curr frame dark
		prev = curr
		curr = is_spell_menu()
		if prev==False and curr==True:
			trigger = True
			time.sleep(0.05)

		# grab screenshot if trigger==True
		if trigger:
			trigger = False
			im = screengrab_as_numpy_array((1270,455,1570,655))
			# cv2.imshow("Image",im)
			# cv2.waitKey(0)
			filename = "./images/img" + str(success) + ".png"
			cv2.imwrite(filename, im)
			# print("image number: " + str(success))
			time.sleep(0.1)
			if success % 25 == 0:
				t = (N - success)*1.6
				# print("Elapsed time: %0.2f minutes" % ((time.time() - start_time)/60))
				# print("Estimated Time Remaining: %0.2f minutes" % (t/60))
			success +=1
			filelist.append(filename)

# takes screenshots from capture window and saves to file
def grab_screens_2(N, imagelist):
	start_time = time.time()
	prev = True
	curr = True
	success = 0
	trigger = False
	while success < N:
		# set triger if previous frame was light and curr frame dark
		prev = curr
		curr = is_spell_menu()
		if prev==False and curr==True:
			trigger = True

		# grab screenshot if trigger==True
		if trigger:
			trigger = False
			im = screengrab_as_numpy_array((1270,455,1570,655))
			# cv2.imshow("Image",im)
			# cv2.waitKey(0)
			imagelist.append(im)
			print("Screengrabbing image " + str(success) + "...")
			success +=1

# returns list of strings of spells read with tesser_image()
def detect_spells_image(image):
	coords = [
		(0,0,300,50),
		(0,50,300,100),
		(0,100,300,150),
		(0,150,300,200)
	] 

	spells = [
		"Acceleratle",
		"Bang",
		"Bounce",
		"Flame Slash",
		"Hatchet Man",
		"Heal",
		"Hocus Pocus",
		"Kaboom",
		"Kaclang",
		"Kacrackle Slash",
		"Kamikazee",
		"Magic Burst",
		"Metal Slash",
		"Oomph",
		"Psyche Up",
		"Sizz",
		"Sizzle",
		"Snooze",
		"Thwack",
		"Whack",
		"Zoom"
	]

	sizzes = [
		"S744",
		"SiZZ",
		"$izz"
	]

	result = []
	#cv2.imshow("image", image)
	#cv2.waitKey(0)
	start = time.time()
	for p in coords:
		imp = image[p[1]:p[3], p[0]:p[2]]
		#cv2.imshow("crop", imp)
		#cv2.waitKey(0)
		for thresh in range(135,155, 2):
			read = tesser_image(imp, thresh)
			if read in spells:
				result.append(read)
				# print(thresh)
				break
			if read in sizzes:
				result.append("Sizz")
				#print(thresh)
				#print(read)
				break
	
	if len(result) == len(set(result)) and len(result) == 4:
		return result
	else:
		return

# returns list of strings of spells read with tesser_image()
def detect_spells_file(filename):
	coords = [
		(0,0,300,50),
		(0,50,300,100),
		(0,100,300,150),
		(0,150,300,200)
	] 

	spells = [
		"Acceleratle",
		"Bang",
		"Bounce",
		"Flame Slash",
		"Hatchet Man",
		"Heal",
		"Hocus Pocus",
		"Kaboom",
		"Kaclang",
		"Kacrackle Slash",
		"Kamikazee",
		"Magic Burst",
		"Metal Slash",
		"Oomph",
		"Psyche Up",
		"Sizz",
		"Sizzle",
		"Snooze",
		"Thwack",
		"Whack",
		"Zoom"
	]

	sizzes = [
		"S744",
		"SiZZ",
		"$izz"
	]

	result = []
	image = cv2.imread(filename,0)
	#cv2.imshow("image", image)
	#cv2.waitKey(0)
	start = time.time()
	for p in coords:
		imp = image[p[1]:p[3], p[0]:p[2]]
		#cv2.imshow("crop", imp)
		#cv2.waitKey(0)
		for thresh in range(135,155, 2):
			read = tesser_image(imp, thresh)
			if read in spells:
				result.append(read)
				# print(thresh)
				break
			if read in sizzes:
				result.append("Sizz")
				#print(thresh)
				#print(read)
				break
	
	if len(result) == len(set(result)) and len(result) == 4:
		return result
	else:
		return

def reading_worker(N, file_list, spell_lists, fail_list,start_time):
	total = 0
	while total < N:
		if len(file_list) > 0:
			f = file_list.pop()
			time.sleep(0.05)
			print("Analyzing image number: " + str(total) + "...")


			r = detect_spells_image(f)
			if r != None:
				spell_lists.append(r)
			else:
				print("Reading failed on attempt " + str(total) + ".\n  Writing to file in ./failures...")
				filename = "./failures/img" + str(len(fail_list)) + ".png"
				cv2.imwrite(filename, f)
				fail_list.append(filename)
			total += 1
			if total % 25 == 1:
				print("Time elapsed: %0.2f minutes" % ((time.time() - start_time)/60))
				print("Estimated time remaining: %0.2f minutes" % ((time.time() - start_time)/total*(N-total)/60))
	return

def grabbing_worker(N, imagelist, spell_lists):
	print("Beginning Screen Grabber...")
	grab_screens_2(N, imagelist)
	return

def make_data_threaded(N):
	start_time = time.time()
	failIndex = []
	threads = []
	filelist=[]
	spell_lists = []

	t_grab = threading.Thread(target=grabbing_worker, args=(N,filelist,spell_lists,))
	threads.append(t_grab)
	t_grab.start()

	t_read = threading.Thread(target=reading_worker, args=(N, filelist,spell_lists,failIndex,start_time,))
	threads.append(t_read)
	t_read.start()

	for t in threads:
		t.join()

	fails = len(failIndex)
	outfile	= open("./OCR_List.csv", "w")
	print("All images analyzed. Writing to file...")
	for r in spell_lists:
		if r != None:
			csvstring = r[0] + "," + r[1] + "," + r[2] + "," + r[3] + "\n"
			outfile.write(csvstring)

	total_time = time.time() - start_time
	print("Tried reading " + str(N) + " images in " + str(total_time))
	print("Avg time per image: " + str(total_time/N))
	print()
	print("Failure rate: " + str(fails / N))
	print("Failed Images:")
	print(failIndex)

make_data_threaded(20)