from generate_ino import generate_ino
import os
i=input('Which net do you want to check?\n 1.Basic_net_1.h5\n 2.Basic_net_2\n 3.Basic_net_3.h5\n(Enter 1,2 or 3)\n')
if(i=='1' or i=='2' or i=='3'):
    h5pth=os.getcwd()+'\\h5_files\\Basic_net_'+i+'.h5'
    afn=input('Enter the arduino file name you want to save as:')
    ardpth=os.getcwd()+'\\arduino_files\\'+afn+'.ino'
    generate_ino(h5pth,ardpth)
else:
    print('Invalid Entry')
    print('Exiting code')
