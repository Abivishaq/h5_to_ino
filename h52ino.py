import keras
import os
from keras.models import Model,load_model
from keras.layers import Dense
def generate_ino(fp='',ip=''):
    if(fp==''):
        print('ERROR: Path to h5 file is missing')
        return(0)
    if(ip==''):
        print('ERROR: Path where ino file is to be saved is missing')
        return(0)
    try:
        m=load_model(fp)
        m.summary()
    except:
        if(os.path.exists(fp)):
            print("ERROR: When trying to load .h5 file")
            return(0)
        else:
            print("ERROR: h5 file not found")
            return (0)
    print('Model succefully read')
    m.summary()
    if(os.path.exists(ip)):
        while(1):
            print(ip)
            print('.ino file with same name and path already exists!!/nDo you want to replace it?(y/n)')
            inp=input()
            if(inp=='n' or inp=='N'):
                print('Exiting function')
                return(0)
            elif(inp=='y' or inp=='Y'):
                print('WARNING:Overwritting ino file')
                break
            else:
                print('Invalid Response!!')
    try:
        f=open(ip,'w')
    except:
        print('ERROR: Unable to create or open .ino file. Try verifying the path.')
        return(0)


    #Extracting weights and writing weights declarations
    wd=''
    lod=''
    ln=0
    act=[]
    for i in m.layers:
        ln+=1
        l_info=i.get_config()
        act.append(l_info['activation'])
        w=i.get_weights()
        wds='double w'+str(ln)+'['+str(len(w[0]))+']['+str(len(w[0][0]))+']={'
        lods='double a'+str(ln)+'['+str(len(w[0][0]))+'];\n'
        lod+=lods
        #print(w)
        #print('.......')
        #print(w[0])
        for j in w[0]:
            wds+='{'
            for k in j:
                wds+=str(k)+','
            wds=wds[:-1]+'},'
        wds=wds[:-1]+'}'
        #print(wds)
        wd+=wds+';\n'
    print(wd)
    f.write(wd)
    lid='double a0['+str(len(m.layers[0].get_weights()[0]))+'];\n'
    f.write(lid)
    f.write(lod)
    nol=len(m.layers)
    f.write('int nol='+str(nol)+';\n\n')

    # matrix_mul
    mm_f='double matmul(double w,double a)\n{\n\t//will add Deepak\'s function here\n}\n'
    f.write(mm_f)

    # relu
    relu_f='double relu(double z)\n{\n\t//will add Nithish\'s function here\n}\n'
    f.write(relu_f)

    # Writing execute code
    ex_f='void execute()\n{\n'
    for i in range(1,nol+1):
        ex_f+='\ta'+str(i)+'=matmul(w'+str(i)+',a'+str(i-1)+');\n'
        ex_f+='\ta'+str(i)+'='+act[i-1]+'(a'+str(i)+');\n'
    ex_f+='}\n'
    f.write(ex_f)

    # Writing setup function
    setup_str='void setup()\n{\n\t//Write your setup code here\n}\n'
    f.write(setup_str)


    # Writing loop function
    loop_str='\nvoid loop()\n{\n\t//Write your loop code here\n}\n'
    f.write(loop_str)



    f.close()

#h5_pth=r'C:\Users\Abi\Documents\academics\semesters\sem5\microcontrollers\project\Basic_net_3.h5'
#ino_pth=r'C:\Users\Abi\Documents\academics\semesters\sem5\microcontrollers\project\trial3.ino'
h5_pth=input('Enter the path of the h5 file:\n')
ino_pth=input('Enter the path where you want to store your ino/arduino file:\n')

generate_ino(h5_pth,ino_pth)