import numpy as np 
import math 

def func(x):
    return x

def main() :
    a = int(input("Silahkan Masukkan Batas Bawah : "))
    b = int(input("Silahkan Masukkan Batas Atas : "))
    N = int(input("Silahkan Masukkan Banyak Check : "))
    q = 0
    i = 0
    x = np.linspace(a,b,N)
    fmin = min(func(x)) 
    fmax = max(func(x))
    area = (b-a)*(fmax-fmin)
    xrand = np.random.uniform(a,b,N) 
    yrand = np.random.uniform(fmin,fmax,N)
    
    while(i <=  N):
        if(yrand[i-1] <= func(xrand[i-1])):
            q += 1
            if(i == N):
                break
            else :
                i += 1
        else : 
            if(i == N):
                break
            else :
                i += 1

    print("Banyak Bilangan Random yang Hit : ",q)
    integralValue  = (np.sum(q)/N)*area
    print("Integral Value Is : ",integralValue)

if __name__ == '__main__':
    main()