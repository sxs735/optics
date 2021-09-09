import numpy as np
np.set_printoptions(precision=8)
with open('MTF0.txt','r') as Str:
    Str = Str.readlines()
    go = True
    while go:
        try:
            Str.remove(' \n')
        except ValueError:
            go = False
    for i,j in enumerate(Str):
        Str[i] = j.replace('\n', '')
    Str = Str[8:]
    MTF = []
    Field = ''
    for g in range(5):
        for i in range(5):
            mtf = []
            field = Str[(i+5*g)*30+7*g][55:].replace('  ', ',').split(',')
            Field += '%s,%s '%(float(field[0]),float(field[1]))
            freq = []
            for j in range(22):
                value = []
                for k in Str[8+j+(i+5*g)*30+7*g].replace(' ', ',').split(','):
                    try:
                        value += [float(k)]
                    except ValueError:
                        pass
                freq += [value[0]]
                mtf += [0.5*(value[1]+value[2])]
            MTF += [mtf]

MTF = np.vstack((freq,np.array(MTF))).T
np.savetxt('MTF_center.txt',MTF, header=Field)
#for i in RMS:
#    print('%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t'%tuple(i),'%.4f\t%.4f\t%.4f\t%.4f'%tuple(i[:4][::-1]))

y0 = np.array([-3.28578198,-0.27027472,13.42655392,14.36531198])
