# Chiu_AuAc
"A warm rain parameterization using aircraft observation and Machine Learning technique"

Please read [Chiu et al., 2020]() for more information.

Contact
=======

* [Christine Chiu](https://www.atmos.colostate.edu/people/faculty/chiu/): `Christine.Chiu@colostate.edu`
* C.Kevin Yang: `yang0920@rams.colostate.edu` for any issues related to the source codes or pacakge

Installation (.py | Python)
===========================
*Caution*: 
> In `v1.0.0`, only the `Source code` option is avilable

Environment
-----------
Check your environement before using the below options to access the code:

1. Programming language: `Python3` ([sunsetting Python 2](https://www.python.org/doc/sunset-python-2/#:~:text=We%20have%20decided%20that%20January,as%20soon%20as%20you%20can.))
2. Python packages: 
* [Numpy](https://numpy.org/)
* [scikit-learn](https://scikit-learn.org/stable/)
* [PyTorch](https://pytorch.org/)
* pickle (standard python library)

*Note*: 
> No package version conflict deteced at this point (i.e., no specific version required at this point), but please do report if you encounter one

Source code
-----------
```bash
cd $....
```

Check out the below example 1...

PyPI (pip)
----------
coming soon...

Anaconda (conda)
----------------
coming soon...

Installation (.f90 |Fortran 90)
===============================
For any 

Performance
===========

Examples
========

Example 1
---------
Start from scratch (using Anaconda environment).

1. Download Anaconda
2. Open the Anaconda prompt
3. make sure all the necessary libarires are installed: numpy, sklearn, pytorch, pickle? (using xxx command to check)
4. the source code and the related files should be stored in the working directory
5. >>> load Chiu_AuAc
6. >>> ....the input data has to be numpy array and the output data is also a numpy array, can input one sample or up to a thousand sample (for this version, and depemnds on your RAM)
7. >>> 


Example 2
---------
coming soon...

Example 3
---------
coming soon...

Example 4
---------
coming soon...

Autoconversion rate
-------------------
coming soon...

Accretion rate
--------------
coming soon...

Release version and note
========================

* `v1.0.0`: released on 11/24/2020 --> first release
* `v1.0.1`: deal with outside the range (infinity)
* `v1.0.2`: coming soon --> allowing to input more than 1,000 samples at once
* `v1.0.3`: coming soon --> ouput both "truth" and "prediction"
* `v1.0.4`: coming soon --> time elpased
* 'v1.0.5`: coming soon --> saving the result to an output file
* `v1.1.0`: coming soon --> including error statistics
* ??? : coming soon --> mixing ratio, and air density version
* `v1.2.0`: coming soon --> adding warning or error message to guide the user
* `v1.3.0': coming soon --> from module to a package
* `v1.4.0': coming soon --> automatically download the neede packages
* `v2.0.0`: coming soon --> a Keras version of the model
* `v3.0.0`: coming soon --> a Fortran version of the model

Reference
=========
Some useful pages: 

1. Github
  * [Hello World](https://guides.github.com/activities/hello-world/)
  * [Basic writing and formatting syntax](https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax#links)
  * [Licensing a repository](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/licensing-a-repository)
  * [Choose an open source license](https://choosealicense.com/)
  * [Setting guidelines for repository contributors](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/setting-guidelines-for-repository-contributors)
  * [Adding a code of conduct to your project](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/adding-a-code-of-conduct-to-your-project)
  * [About READMEs](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/about-readmes)
  
2. [Software versioning](https://en.wikipedia.org/wiki/Software_versioning)
3. Python
   * [Modules](https://docs.python.org/3/tutorial/modules.html)
   * [Packaging Python Project](https://packaging.python.org/tutorials/packaging-projects/)
   * []()
4. StackOverflow
   * [Saving StandardScaler() model for use on new datasets](https://stackoverflow.com/questions/53152627/saving-standardscaler-model-for-use-on-new-datasets/53153373#53153373)
   * []()
