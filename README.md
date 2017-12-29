The code in this repository is available under the [Berkeley Software Distribution (BSD) license](https://en.wikipedia.org/wiki/BSD_licenses).This project is described in: Stefan Niekamp, Jongmin Sung, Walter Huynh, Ronald D. Vale, Nico Stuurman (2017). High accuracy measurements of nanometer-scale distances between fluorophores at the single-molecule level. [Biorxiv](https://doi.org/10.1101/234740) Department of Cellular and Molecular Pharmacology and Howard Hughes Medical Institute, University of California, San Francisco, 600 16th Street, San Francisco, CA 94158.-----------------This is a custom-written Python code for Monte Carlo simulations of nanometer distances under various perturbations.The script will generate .txt files that contain simulated data (Monte-Carlo simulation) where two dyes are a certain distance 'mu' appart. Here, we are assuming that the channels (channel 1 and 2) are registered and that no drift is accruing. Many parameters can be changed as listed below and the file can be 'dragged and dropped' into the mManager 'Data' window in the 'Localization Microscopy' plug-in for analysis. Files will be saved in the same folder the script is in.A Gaussian distribution is applied to the true position of channel 1 and 2 based on the variance in the fluorophores localization of the respective channel. Moreover a Gamma distribution is applied to the underlying distribution of the variance in the fluorophores localization for channel 1 and 2.In this script you can change the values for the expected distance (mu), for the standard deviation in fluorophores localization of channel 1 and 2 (sigmaloc1 and sigmaloc2) as well as the underlying distribution of the standard deviation in fluorophores localization of channel 1 and 2 (sigmasigmaloc1 and sigmasigmaloc2). Moreover, the number of spot pairs of channel 1 and channel 2 (numberofspots) as well as the number of frames / number of observations of each molecule (frames) can be set. In addition, a standard deviation for heterogeneous samples (mustd) can be chosen. Finally, you can decide how many data sets with a particular parameter set (numberofrepeats) you like to generate. You also have the option to simulate multiple combinations of parameters as once. For instance, if you select two different distances, it will carry out all simulations for the other parameters for both distances.Note: Values that are not needed for distance prediction in mManager (e.g. intensity, background, ...) are set to 1.If python 2.7 is alrady installed on a computer there is no installation time. Otherwise python 2.7 can be found [here](https://www.python.org/downloads/). This script was written and optimized for python 2.7 and test runs were performed on windows 7.0 and higher as well as Mac OS 10.9 and higher.

The run time for a single output file on a "normal" computer is less than a second. However, to generate all files as used in the manuscript for analysis (2160) takes about 12 hours on a "normal" computer.We also provide two example output files:

- *MCS_distance_10.0_sigmaloc1_10.0_sigmaloc2_10.0_sigmasigmaloc1_2.0_sigmasigmaloc2_2.0_frames_10_numberofspots_1000_sample-heterogeneity_0_repeat_1.txt*
- *MCS_distance_20.0_sigmaloc1_10.0_sigmaloc2_10.0_sigmasigmaloc1_2.0_sigmasigmaloc2_2.0_frames_10_numberofspots_1000_sample-heterogeneity_0_repeat_1.txt*