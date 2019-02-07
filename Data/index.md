###This project is described in: Stefan Niekamp<sup>1</sup>, Jongmin Sung<sup>1</sup>, Walter Huynh<sup>1</sup>, Gira Bhabha<sup>2</sup>, Ronald D. Vale<sup>1</sup>, Nico Stuurman<sup>1</sup> (2018). High accuracy measurements of nanometer-scale distances between fluorophores at the single-molecule level, [BioRxiv](https://doi.org/10.1101/234740)

<sup>1</sup>Department of Cellular and Molecular Pharmacology and Howard Hughes Medical Institute, University of California, San Francisco, 600 16th Street, San Francisco, CA 94158.

<sup>2</sup>Skirball Institute of Biomolecular Medicine, New York University School of Medicine, New York, NY 10016

-------------------

-------------------

Here we provide example data that can be used to test run the 'Localization Microscopy' plug-in in micro-Manager [1]. A manuel for how to use the plug-in can be found [here](manual.pdf).

Moreover, we provide all negative stain electron microscopy micrographs that were used for the dynein data analysis.

-------------------

####Monte Carlo simulated data

Here are example Monte Carlo simulated distance files that were used in **Figure 3** to compare Sigma-P2D and P2D:

- <a href="data/Monte-Carlo-Data/Figure3.zip" download>Example Monte Carlo simulated distance files used in Figure 3</a> (a download  will start when clicking the link)

Here are example Monte Carlo simulated distance files that were used in **Figure 4** to compare Vector-P2D and Vector:

- <a href="data/Monte-Carlo-Data/Figure4.zip" download>Example Monte Carlo simulated distance files used in Figure 4</a> (a download  will start when clicking the link)

In order to analyze these files, just drag 'n drop them into the ‘Gaussian tracking data’ window of the 'Localization Microscopy' plug-in. These can then be treated as registrated image files. Thus, just continue in the 'Data analysis and distance determination' section of the [manual](manual.pdf).

-------------------

####Registration of two channels

For the registration data (as in **Figure 2**) we provide a file that can be used to create the map and a file that can be used to determine the target registration error. Use the parameters as shown in **Table S4**.


- <a href="data/Registration/Beads-to-create-and-test-map.zip" download>Example data to create the registration maps</a> (a download  will start when clicking the link)
	- To create the affine map, use positions 1-10 and for the piecewise affine map use positions 11-200. Otherwise follow instructions as given in the [manual](manual.pdf).
	- To test the map, use positions 201-400. This will ensure that not exactely the same fiducials, that were used to create the map, are used to evaluate the registration map (traget registration error (TRE)).
	- To evaluate the quality of the map, affine and piecewise affine correct the test map as described in the [manual](manual.pdf). 


As mentioned in the manuscript, we always acquiered fiducials to create the registration map ("set 1") before the distance measurement with the sample of interest and collected fiducials afterward to evaluate the stability of the map ("set 2"). While the manuscript is underreview, we found a way that can even further improve registration for maps that slightly shifted during aqcuisition. 

We noticed that, if shifts happen, then often more on a global and linear scale. Thus, we decided to use some of the first fiducials of set 1 as well as some of the last fiducials of set 2 and to combine those to create the affine map. In that way the effect of a shift can be minimized. For the piecewise affine map we then use the remaing fiducials of set 1 and set 2 and combine these. Below we will give an example for how this might work.

- <a href="data/Registration/Set1.zip" download>Set 1 to create the registration maps</a> (a download  will start when clicking the link)
- <a href="data/Registration/Set2.zip" download>Set 2 to create the registration maps</a> (a download  will start when clicking the link)
	- Use positions 1-10 of set 1 and position 391-400 of set 2 and combine both. Therefore select all files/rows and click ‘Combine’ in ‘General’ in the ‘Gaussian tracking data’ window of the plug-in. This combined set will then be used as affine map.
	- Use positions 11-200 of set 1 and position 201-390 of set 2 and combine both. This combined set can now be used to create the piecewise affine map as described in the [manual](manual.pdf). 
	- In order to evaluate the map we will not use the same fiducials that were used to create the map (TRE). Thus, in this particular example, fit positions 201-400 of set 1 and positions 1-200 of set 2, combine both, and affine as well as piecewise affine correct them as described in the [manual](manual.pdf).

-------------------

####Distance measurements

For the distance measurements we provide the registration maps (affine as well as piecewise affine maps) as '.txt' files. These can be loaded into the micro-Manager's 'Localization Microscopy' plug-in and used directly as described in the [manual](manual.pdf).

#####1. Kinesin 1 (Figure 3):

- [Example data for kinesin 1](data/Distance/Kinesin/) (a download  will start when clicking the link)
- [Affine map for kinesin 1](data/Distance/Maps/maps.html)
- [Piecewise affine map for kinesin 1](data/Distance/Maps/maps.html)
	- Follow the instructions as given in the [manual](manual.pdf). Use the parameters as shown in **Table S4** and **Table S6**.	

#####2. 10 nm DNA origami nanoruler (Figure 4):

- <a href="data/Distance/10nmOrigami/10nm-Origami-Combined.zip" download>Example data for 10 nm DNA origami nanoruler</a> (a download  will start when clicking the link)
- [Affine map for 10 nm DNA origami nanoruler](data/Distance/Maps/maps.html)
- [Piecewise affine map for 10 nm DNA origami nanoruler](data/Distance/Maps/maps.html)
	- Follow the instructions as given in the [manual](manual.pdf). Use the parameters as shown in **Table S4**.	

#####3. 20 nm DNA origami nanoruler (Figure 4):

- <a href="data/Distance/20nmOrigami/20nm-Origami-Combined.zip" download>Example data for 20 nm DNA origami nanoruler</a> (a download  will start when clicking the link)
- [Affine map for 20 nm DNA origami nanoruler](data/Distance/Maps/maps.html)
- [Piecewise affine map for 20 nm DNA origami nanoruler](data/Distance/Maps/maps.html)
	- Follow the instructions as given in the [manual](manual.pdf). Use the parameters as shown in **Table S4**.


#####4. 40 nm DNA origami nanoruler (Figure 4):

- <a href="data/Distance/40nmOrigami/40nm-Origami-Combined.zip" download>Example data for 40 nm DNA origami nanoruler</a> (a download  will start when clicking the link)
- [Affine map for 40 nm DNA origami nanoruler](data/Distance/Maps/maps.html)
- [Piecewise affine map for 40 nm DNA origami nanoruler](data/Distance/Maps/maps.html)
	- Follow the instructions as given in the [manual](manual.pdf). Use the parameters as shown in **Table S4**.

#####5. Dynein stalk (Figure 5):

- <a href="data/Distance/Dynein/Dynein-apo.zip" download>Example data for dynein stalk measurement in apo state</a> (a download  will start when clicking the link)
- <a href="data/Distance/Dynein/Dynein-ATPvi.zip" download>Example data for dynein stalk measurement in ATP-vi state</a> (a download  will start when clicking the link)
- [Affine map for dynein stalk measurement](data/Distance/Maps/maps.html)
- [Piecewise affine map for dynein stalk measurement](data/Distance/Maps/maps.html)
	- Follow the instructions as given in the [manual](manual.pdf). Use the parameters as shown in **Table S4** and **Table S6**.

-------------------

####Negative stain electron microscopy micrographs

Here are the raw electron microscopy micrographs of the yeast dynein monomer as .dm3 files:

- <a href="data/Electron-microscopy/apo.zip" download>electron microscopy micrographs of the yeast dynein monomer in the apo state</a> (a download  will start when clicking the link)
- <a href="data/Electron-microscopy/atp-vi.zip" download>electron microscopy micrographs of the yeast dynein monomer in the ATP-vi state</a> (a download  will start when clicking the link)



-------------------

####References

[1] Edelstein, A., Amodaj, N., Hoover, K., Vale, R. & Stuurman, N. Computer control of microscopes using µManager. Curr. Protoc. Mol. Biol. Chapter 14, Unit14.20 (2010)