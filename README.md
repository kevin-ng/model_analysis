# model_analysis
Code included in the book "Introduction to the Modeling and Analysis of Complex Systems" translated from Python2 to Python3.

### About the files here
This repository contains all codes from the book "Introduction to the Modeling and Analysis of Complex Systems" by Hiroki Sayama (sayama@binghamton.edu), translated from Python2.7 to Python3. The book can be freely downloaded from http://bingweb.binghamton.edu/~sayama/textbook/

### Why the translation
The original codes were written in Python 2.7.
It is now translated to Python3 using the tool "2to3" (see https://docs.python.org/2/library/2to3.html )
The reason why I am doing this is Python2 is to become end of life by 2020 according to https://legacy.python.org/dev/peps/pep-0373/

### How the translation is done
The command line I used for the translation is 
"2to3 -w -n -o \<code3>  \<code>"

where <br/>
\<code> is the name of the folder containing the original code, <br/>
\<code3> is the name of the foldder containing the translated code.

### Disclaimer
I have NOT yet tested if the translation works. <br/>
But the following scripts had been tested to run without syntax error in Python3: <br/>

chaotic-behavior-butterfly-effect.py <br/>
communities.py <br/>
chaotic-behavior.py <br/>

I hope you find this work useful.
