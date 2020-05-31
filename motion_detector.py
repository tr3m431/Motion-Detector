
'''
===============================================================================
ENGR 133 Program Description
	Motion Detector
Assignment Information
	Assignment:     Individual project
	Author:         Tremael Arrington, Tarring@purdue.edu
	Team ID:        004-03 (e.g. 001-14 for section 1 team 14)

Contributor:    Stack Overflow [repeat for each]
	My contributor(s) helped me:
	[] understand the assignment expectations without
		telling me how they will approach it.
	[x] understand different ways to think about a solution
		without helping me plan my solution.
	[x] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.

    Contributor:    Geeks to Geeks [repeat for each]
    	My contributor(s) helped me:
    	[] understand the assignment expectations without
    		telling me how they will approach it.
    	[x] understand different ways to think about a solution
    		without helping me plan my solution.
    	[] think through the meaning of a specific error or
    		bug present in my code without looking at my code.
    	Note that if you helped somebody else with their code, you
    	have to list that person as a contributor here as well.
===============================================================================
'''

# add 1 more user-defined functions

import cv2
import time
import pandas
from datetime import datetime

# explicitly import required user-defined functions
from motdetlib import quit_key
from motdetlib import record
from motdetlib import turn_off

key = quit_key()

# Assigning our static_back to None
static_back = None

# List when any moving object appear
motion_list = [None, None]

# Time of movement
time = []

# Initializing DataFrame, one column is start
# time and other column is end time
df = pandas.DataFrame(columns = ["Start", "End"])

# Capturing video
video = cv2.VideoCapture(0) #this is what controls fps *most likely*

# Infinite while loop to treat stack of image as video
record(time, static_back, motion_list, video, key)

# Appending time of motion in DataFrame
for i in range(0, len(time), 2):
    df = df.append({"Start":time[i], "End":time[i + 1]}, ignore_index = True)

# Creating a csv file in which time of movements will be saved
csv_datafile = "movements.csv"
df.to_csv(csv_datafile)

turn_off(video)

# 19 lines
'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
