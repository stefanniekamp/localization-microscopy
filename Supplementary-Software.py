import random
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
import matplotlib.mlab as mlab
import os
import shutil
import os.path
import time
from optparse import OptionParser
import csv
from scipy.stats import gamma

##########################################################################################
###      READ ME      READ ME      READ ME      READ ME      READ ME      READ ME      ###
##########################################################################################

"In this script you can change the values for the expected distance (mu) and for localization errors of channel 1 and 2 (sigmamean1 and sigmamean2). The underlying distribution of the standard deviation in fluorophores localization of channel 1 and 2 (sigmastd1 and sigmastd2) is set to a third of sigmamean1 and sigmamean2, respectively. This is based on experimental data since the observed standard deviation in fluorophores localization was in most cases approximately a third of the localization error. Moreover, the number of spot pairs of channel 1 and channel 2 (numberofspots) as well as the number of frames / number of observations of each molecule (frames) can be set. In addition, a standard deviation for heterogeneous samples (mustd) can be chosen. Finally, you can decide how many data sets with a particular parameter set (numberofrepeats) you like to generate. You also have the option to simulate multiple combinations of parameters at once. For instance, if you select two different distances, it will carry out all simulations for the other parameters for both distances."

"Note: Values that are not needed for distance prediction in mManager (e.g. intensity, background, ...) are set to 1"

mu = [10]
sigmamean1 = [10.0]
sigmamean2 = [10.0]
#sigmastd1 = 1/3 x sigmamean1
#sigmastd2 = 1/3 x sigmamean2
numberofspots = [1000] 
frames = [10]
mustd = 2.0  #sample heterogeneity (set to 0 for homogeneous sample)
numberofrepeats = 1

##########################################################################################
###                     DO NOT MAKE ANY CHANGES BELOW HERE                             ###
##########################################################################################

channels = 2


for x in range(numberofrepeats):
	for l in range(len(mu)):
		for m in range(len(frames)):
			for q in range(len(numberofspots)):
				for o in range(len(sigmamean1)):
					sigmastd1 = sigmamean1[o]/3.0
					sigmastd2 =	sigmamean2[o]/3.0
					x1list = []
					x2list = []
					y1list = []
					y2list = []
					fh = open("MCS_distance_" + str(mu[l]) + "_frames_" + str(frames[m]) + "_numberofspots_" + str(numberofspots[q]) + "_sigmamean_" + str(sigmamean1[o]) + "_sigmastd_" + str(sigmastd1) + "_sample-heterogeneity_" + str(mustd) + "_" + str(x) + ".txt", "w+")
					fh.write("application_id: 6	name: MCS_distance_" + str(mu[l]) + "_frames_" + str(frames[m]) + "_numberofspots_" + str(numberofspots[q]) + "_sigmamean_" + str(sigmamean1[o]) + "_sigmastd_" + str(sigmastd1) + "_sample-heterogeneity_" + str(mustd) + "_" + str(x) + ".txt	filepath: /Volumes/sniekamp/TIRF-Data/20170123_Nanoruler/20170123_40nm_20x20beads_1	nr_pixels_x: 512	nr_pixels_y: 512	pixel_size: 159.0	nr_spots: 1046	box_size: 12	nr_channels: 2	nr_frames: " + str(frames[m]) + "	nr_slices: 1	nr_pos: 400	location_units: NM	intensity_units: PHOTONS	fit_mode: 1	is_track: false	has_Z: false")
					fh.write("\n")
					fh.write("molecule	frame	slice	channel	pos	x_position	y_position	x	y	intensity	background	width	a	theta	sigma	intensity_aperture	background_aperture	intensity_ratio	m_sigma	integral_aperture_sigma")
					fh.write("\n")
					n = 0
					for j in range(channels):
						for k in range(frames[m]):
							for i in range(numberofspots[q]):
								mean1 = 12500
								if mustd == 0:
									mean2 = 12500 + mu[l]
								if mustd != 0:
									mulist = np.random.normal(mu[l], mustd, 1)
									mureg = mulist[0]
									mean2 = 12500 + mureg
								n = n + 1
								channel = j + 1
								frame = k + 1
								pos = i + 1
								fh.write(str(n) + "\t") #write molecule number
								fh.write(str(frame) + "\t") #write frame number
								fh.write(str(1) + "\t")	 #write slice number (always set to 1)
								fh.write(str(channel) + "\t") #write channel number
								fh.write(str(pos) + "\t") #write position number
								fh.write(str(1) + "\t")	#write intensity number (always set to 1)
								fh.write(str(1) + "\t")	#write background number (always set to 1)
								if channel == 1:
									sigmalist = np.random.gamma(float((sigmamean1[o]**2)/sigmastd1**2), float((sigmastd1**2)/sigmamean1[o]), 100)
									sigma = sigmalist[0]
									mean_1 = [mean1, 12500]
									cov = [[sigma**2, 0], [0, sigma**2]]  # diagonal covariance
									number = 1
									x1, y1 = np.random.multivariate_normal(mean_1, cov, number).T
									fh.write(str(x1[0]) + "\t") #write x coordinate for channel 1
									fh.write(str(y1[0]) + "\t") #write y coordinate for channel 1
									x1list.append(x1[0])
									y1list.append(y1[0])
								if channel == 2:
									sigmalist = np.random.gamma(float((sigmamean2[o]**2)/sigmastd2**2), float((sigmastd2**2)/sigmamean2[o]), 100)
									sigma = sigmalist[0]
									mean_2 = [mean2, 12500]
									cov = [[sigma**2, 0], [0, sigma**2]]  # diagonal covariance
									number = 1
									x2, y2 = np.random.multivariate_normal(mean_2, cov, number).T
									fh.write(str(x2[0]) + "\t") #write x coordinate for channel 2
									fh.write(str(y2[0]) + "\t") #write y coordinate for channel 2
									x2list.append(x2[0])
									y2list.append(y2[0])
								fh.write(str(1) + "\t")	#write width number (always set to 1)
								fh.write(str(1) + "\t")	#write a number (always set to 1)
								fh.write(str(1) + "\t")	#write theta number (always set to 1)
								fh.write(str(1) + "\t")	#write xS_pos number (always set to 1)
								fh.write(str(1) + "\t")	#write y_pos number (always set to 1)
								fh.write(str(sigma) + "\t")	#write sigma number
								fh.write(str(1) + "\t")	#write theta number (always set to 1)
								fh.write(str(1) + "\t")	#write xS_pos number (always set to 1)
								fh.write(str(1) + "\t")	#write xS_pos number (always set to 1)
								fh.write(str(sigma) + "\t")	#write sigma number
								fh.write(str(sigma) + "\n")	#write sigma number
					fh.close()			

##########################################################################################
		


