# h5_to_ino
Obtaining an arduino code that allows the arduino to perform forward propagation on a specific neural net. The neural nets architecture and weights are obtained from .h5 file. 
# Installation guide
1. download and extract the zip file or clone this repository
2. Install Keras using pip
# Usage
1. Get or save keras model
2. Run the h52ino.py script
3. Input the path to the stored keras model
4. Input the file name of the output arduino file
5. The arduino file is generated
6. Open the arduino file
7. Specify how the input of the model is obtained
8. Specify what to do with the output of the model
# Files' explanantion
h52ino.py asks for the inputs:
  full path to  .h5 file
and 
  full path to where the arduino code is to be stored

generate_ino.py - contains the definition of a function used by other scripts. The function get input arguments as h5 file full path and arduino file full path. It then reads the h5 files and writes the arduino code. 

h52ino_examples.py - it used just get an idea of what the is the objective of the project. There are 3 basic h5 files provided. This program allows you to chose one of them. Then give a name for the arduino file to be stored. (Note: just the name not the full path and do not specify the extension '.ino') 
