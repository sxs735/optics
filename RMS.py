import numpy as np
np.set_printoptions(precision=8)
with open('RMS0.txt','r') as Str:
    Str = Str.readlines()
    go = True
    while go:
        try:
            Str.remove(' \n')
        except ValueError:
            go = False
    for i,j in enumerate(Str):
        Str[i] = j.replace('\n', '')
    Str = Str[1:]
    RMS = []
    for i in range(81):
        List = Str[3+i*10].split('HBAR')[-1].split('GBAR')
        H,G = float(List[0]),float(List[1])
        value = []
        for j in Str[10+i*10].replace(' ', ',').split(','):
            try:
                value += [float(j)]
            except ValueError:
                pass
        RMS += [value[2]]
RMS = np.array(RMS).reshape(9,9).T
np.savetxt('Xpuls.txt',RMS)
#for i in RMS:
#    print('%.4f\t%.4f\t%.4f\t%.4f\t%.4f\t'%tuple(i),'%.4f\t%.4f\t%.4f\t%.4f'%tuple(i[:4][::-1]))

y0 = np.array([-3.28578198,-0.27027472,13.42655392,14.36531198])
