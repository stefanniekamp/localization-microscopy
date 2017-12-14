################################################################################
###        IMPORT PACKAGES      IMPORT PACKAGES       IMPORT PACKAGES        ###
################################################################################

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

################################################################################
###       READ ME      READ ME      READ ME      READ ME      READ ME        ###
################################################################################

"""The script will generate .txt files that contain simulated data (Monte-Carlo simulation) where two dyes are a certain distance 'mu' appart. Here, we are assuming that the channels (channel 1 and 2) are registered and that no drift is accruing. Many parameters can be changed as listed below and the file can be 'dragged and dropped' into the mManager 'Data' window in the 'Localization Microscopy' plug-in for analysis. Files will be saved in the same folder the script is in.

A Gaussian distribution is applied to the true position of channel 1 and 2 based on the variance in the fluorophores localization of the respective channel. Moreover a Gamma distribution is applied to the underlying distribution of the variance in the fluorophores localization for channel 1 and 2.

In this script you can change the values for the expected distance (mu), for the standard deviation in fluorophores localization of channel 1 and 2 (sigmaloc1 and sigmaloc2) as well as the underlying distribution of the standard deviation in fluorophores localization of channel 1 and 2 (sigmasigmaloc1 and sigmasigmaloc2). Moreover, the number of spot pairs of channel 1 and channel 2 (numberofspots) as well as the number of frames / number of observations of each molecule (frames) can be set. In addition, a standard deviation for heterogeneous samples (mustd) can be chosen. Finally, you can decide how many data sets with a particular parameter set (numberofrepeats) you like to generate. You also have the option to simulate multiple combinations of parameters as once. For instance, if you select two different distances, it will carry out all simulations for the other parameters for both distances.

Note: Values that are not needed for distance prediction in mManager (e.g. intensity, background, ...) are set to 1."""

mu = [10.0, 20.0]
sigmaloc1 = [5.0, 10.0] #sigmaloc1 and sigmaloc2 have to be same dimension
sigmaloc2 = [5.0, 10.0]
sigmasigmaloc1 = [2.0] #sigmasigmaloc1 and sigmasigmaloc2 have to be same dimension
sigmasigmaloc2 = [2.0]
numberofspots = [1000] 
frames = [10]
mustd = [0]  #sample heterogeneity (set to 0 for homogeneous sample)
numberofrepeats = 1

################################################################################
###                DO NOT MAKE ANY CHANGES BELOW HERE                        ###
################################################################################

channels = 2

#loop through all possible combinations of parameters
for x in range(numberofrepeats):
	for l in range(len(mu)):
		for m in range(len(frames)):
			for q in range(len(numberofspots)):
				for o in range(len(sigmaloc1)):
					for r in range(len(sigmasigmaloc1)):
						for s in range(len(mustd)):
							x1list = []
							x2list = []
							y1list = []
							y2list = []
							#create file
							fh = open("MCS_distance_" + str(mu[l]) + "_sigmaloc1_" + str(sigmaloc1[o]) + "_sigmaloc2_" + str(sigmaloc2[o]) + "_sigmasigmaloc1_" + str(sigmasigmaloc1[r]) + "_sigmasigmaloc2_" + str(sigmasigmaloc2[r]) + "_frames_" + str(frames[m]) + "_numberofspots_" + str(numberofspots[q]) + "_sample-heterogeneity_" + str(mustd[s]) + "_repeat_" + str(x+1) + ".txt", "w+")
							#write file header
							fh.write("application_id: 1	name: MCS_distance_" + str(mu[l]) + "_sigmaloc1_" + str(sigmaloc1[o]) + "_sigmaloc2_" + str(sigmaloc2[o]) + "_sigmasigmaloc1_" + str(sigmasigmaloc1[r]) + "_sigmasigmaloc2_" + str(sigmasigmaloc2[r]) + "_frames_" + str(frames[m]) + "_numberofspots_" + str(numberofspots[q]) + "_sample-heterogeneity_" + str(mustd[s]) + "_repeat_" + str(x+1) + ".txt	filepath: /Volumes/blank	nr_pixels_x: 512	nr_pixels_y: 512	pixel_size: 159.0	nr_spots: 1046	box_size: 12	nr_channels: 2	nr_frames: " + str(frames[m]) + "	nr_slices: 1	nr_pos: 400	location_units: NM	intensity_units: PHOTONS	fit_mode: 1	is_track: false	has_Z: false")
							fh.write("\n")
							fh.write("molecule	frame	slice	channel	pos	x_position	y_position	x(nm)	y(nm)	intensity	background	width	a	theta	sigma	int_ratio	alt_sigma	intensity_aperture	background_aperture")
							fh.write("\n")
							n = 0
							for i in range(numberofspots[q]):
								for j in range(channels):
									for k in range(frames[m]):
#set true position for channel 1 and 2 and account for potential heterogeneity
										mean1 = 12500
										if mustd[s] == 0:
											mean2 = 12500 + mu[l]
										if mustd[s] != 0:
											mulist = np.random.normal(mu[l], mustd[s], 1)
											mureg = mulist[0]
											mean2 = 12500 + mureg
										n = n + 1
										channel = j + 1
										frame = k + 1
										pos = i + 1
										fh.write(str(n) + "\t") 
										#write molecule number
										fh.write(str(frame) + "\t") 
										#write frame number
										fh.write(str(1) + "\t")	 
										#write slice number (always set to 1)
										fh.write(str(channel) + "\t") 
										#write channel number
										fh.write(str(pos) + "\t") 
										#write position number
										fh.write(str(1) + "\t")	
										#write x coordinate in pixel (always set to 1)
										fh.write(str(1) + "\t")	
										#write y coordinate in pixel (always set to 1)
										
									#apply Gaussian distribution to true position in channel 1 and 2 based on the variance in the fluorophores localization for channel 1
										if channel == 1:
											#apply underlying Gamma distribution to the variance in the fluorophores localization for channel 1
											sigmalist = np.random.gamma(float((sigmaloc1[o]**2)/sigmasigmaloc1[r]**2), float((sigmasigmaloc1[r]**2)/sigmaloc1[o]), 100)
											sigma = sigmalist[0]
											mean_1 = [mean1, 12500]
											cov = [[sigma**2, 0], [0, sigma**2]]  # diagonal covariance
											number = 1
											x1, y1 = np.random.multivariate_normal(mean_1, cov, number).T
											fh.write(str(x1[0]) + "\t") 
											#write x coordinate for channel 1
											fh.write(str(y1[0]) + "\t") 
											#write y coordinate for channel 1
											x1list.append(x1[0])
											y1list.append(y1[0])
										#apply Gaussian distribution to true position in channel 1 and 2 based on the variance in the fluorophores localization for channel 2	
										if channel == 2:
											#apply underlying Gamma distribution to the variance in the fluorophores localization for channel 2
											sigmalist = np.random.gamma(float((sigmaloc2[o]**2)/sigmasigmaloc2[r]**2), float((sigmasigmaloc2[r]**2)/sigmaloc2[o]), 100)
											sigma = sigmalist[0]
											mean_2 = [mean2, 12500]
											cov = [[sigma**2, 0], [0, sigma**2]]  					# diagonal covariance
											number = 1
											x2, y2 = np.random.multivariate_normal(mean_2, cov, number).T
											fh.write(str(x2[0]) + "\t") 
											#write x coordinate for channel 2
											fh.write(str(y2[0]) + "\t") 
											#write y coordinate for channel 2
											x2list.append(x2[0])
											y2list.append(y2[0])
										fh.write(str(1) + "\t")	
										#write intensity (always set to 1)
										fh.write(str(1) + "\t")	
										#write background (always set to 1)
										fh.write(str(1) + "\t")	
										#write width (always set to 1)
										fh.write(str(1) + "\t")	
										#write a (always set to 1)
										fh.write(str(1) + "\t")	
										#write theta (always set to 1)
										fh.write(str(sigma) + "\t")	
										#write sigma
										fh.write(str(1) + "\t")	
										#write Int. (ratio) (always set to 1)
										fh.write(str(1) + "\t")	
										#write xSigma-alt. (always set to 1)
										fh.write(str(1) + "\t")	
										#write Int (Apert.) (always set to 1)
										fh.write(str(1) + "\n")	
										#write Bkr (Apert.) (always set to 1)
							#save file
							fh.close()			

################################################################################
		


