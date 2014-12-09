python-tutorial
===============

Code and IPython Notebooks for introductory Python lesson. Aimed at scientists familiar with C/FORTRAN (Slides not included).

* This tutorial uses IPython Notebooks stored in the notebooks directory for the introductory material, up to the Python functions part. After that the scripts directory should be used for examples on classes/modules and 3rd party libraries.
* These tutorials are written in Python 3 and so will not work corectly if your default Python install is Python 2.7.x as is often the case.
 
# Getting started on Linux (Ubuntu)
1. Make sure that Python 3 (or better yet Python 3.4), IPython 3 and IPython Notebooks are installed. They should be installable from packages similar to:
```
sudo apt-get install python3    
sudo apt-get install ipython3    
sudo apt-get install ipython3-notebook
```
2. Other 3rd party libraries like numpy, scipy, matplotlib can probably be installed from your operating system's package manager if they aren't already. If they can't be found there then you should already install the Python Intaller [pip](https://pypi.python.org/pypi/pip) which indexes and installs most of Python's 3rd party libraries. `sudo apt-get install python-pip`
3. To use the notebooks, move into the notebooks directory start up IPython 3 Notebook with
```
cd notebooks   
ipython3 notebook
```
You should automatically get either a new browser tab or your browser wil open up for you with the available notebooks to start. 
