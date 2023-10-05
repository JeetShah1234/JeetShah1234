
from math import pi
from math import log


try:
    Nmin=int(input('Enter the minimum speed \nNmin : '))
    Nmax=int(input('Enter the maximum speed \nNmax : '))
    z=int(input('Enter the Number of speed stages :  '))
    Vopt=int(input('Enter the optimum speed : '))

#AP
    ap=[]                               #ap is set of list of step speed according to arithmatic progression
    Da=[]                               #Da is set of list of diameter of gears according to arithmatic progression
    for i in range(z):
        def AP(*args):
            d=(Nmax-Nmin)/(z-1)
            b=Nmin + i*d
            di=int(1000*Vopt/(b*pi))
            return b,di
        b,di= AP()
        ap.append(int(b))
        Da.append(di)

#GP
    gp=[]                                #gp is set of list of step speed according to arithmatic progression
    Dg=[]                                #Da is set of list of diameter of gears according to geometric progression
    for i in range(z):
        def GP(*args):
            r=pow((Nmax/Nmin),(1/(z-1)))
            b=Nmin*pow(r,i)
            di=int(1000*Vopt/(b*pi))
            return b,di,r                
        b,di,r= GP()
        gp.append(int(b))
        Dg.append(di)

#prime number
    n=[]
    for i in range(2,100):
        a=0
        for j in range(2,100):
            if i%j==0:
                a=a+1
            elif i==j:
                break
        if a==1:
            n.append(i)        

# speed stage
    p=[]                         #p=number of speed steps in speed 
    a=z
    for i in n:
        while True:
            if a%i==0:
                a=a/i
                p.append(i)          
            else:
                break

# structural formula
    print('----------------------------------')
    print('   Structural formulas')
    if len(p)==2  :
        c=0
        S=[]
        while c<len(p):
            x1=1
            x2=p[0]
            x=[x1,x2]
            a=0
            print('---------------------------------')
            while a<len(p):
                print(f'{p[0]}({x1})  {p[1]}({x2})  ')    
                c1=x1
                x1=x2
                x2=c1
                a=a+1
            print('----------------------------------')
            c=c+1
            c1=p[1]
            p[1]=p[0]
            p[0]=c1
   
        for i in S:
            print(i)
    
    elif len(p)==3:
        c=0
        S=[]
        while c<len(p):
            x1=1
            x2=p[0]
            x3=p[0]*p[1]
            x=[x1,x2,x3]
            a=0
            print('----------------------------------')
            while a<len(p):
                print(f'{p[0]}({x1})  {p[1]}({x2})  {p[2]}({x3}) ')
                c1=x1
                x1=x2
                x2=x3
                x3=c1
                a=a+1
            print('----------------------------------')
            c=c+1
            c1=p[2]
            p[2]=p[0]
            p[0]=p[1]
            p[1]=c1
        for i in S:
            print(i)
    
# solution
    def step(z):
        if z==6:
            a='3(1) 2(3)\n2(1) 3(2)'
            return a
        elif z==8:
            a='2(1) 2(2) 2(4)'
            return a
        elif z==9:
            a='3(1) 3(3)'
            return a 
        elif z==12:
            a='3(1) 2(3) 2(6)\n2(1) 3(2) 2(6)\n2(1) 2(2) 3(4)'
            return a
        elif z==15:
            a='3(1) 5(3) '
            return a
        elif z==16:
            a='4(1) 2(4) 2(8)\n2(1) 4(2) 2(8)\n2(1) 2(2) 4(4) '
            return a
        elif z==18:
            a='3(1) 3(3) 2(9)\n3(1) 2(3) 3(6)\n2(1) 3(2) 3(6)'
            return a
        else:
            a='please enter the standard step value\n'
            return a
        
    
    print('structural formula that are feasible') 
    print('-----------------------------------') 
    print(step(z))
        
        
    print(f'\nNo. of shaft : {len(p)+1}')

#input speed
    if z%2==0:
        m=z/2
    else:
        m=z/2+1
    N=gp[int(m)]
    Ni=pow(10,log(N,10)+log(r/2,10))

    print(f'\nInput speed of gear box \nNi : {Ni:.2f} RPM')

# no. of pairs
    I=sum(p)
    print(f'\nTotal no. of pairs {I}')

#table  
    dt={}
    for i in range(1,z+1):
        dt[i]=[ap[i-1],Da[i-1],gp[i-1],Dg[i-1]]
    j=['step','N(AP)','D(AP)','N(GP)','D(GP)']
    print('\n-----------------------------------------------')
    print(f"{j[0]:<8} {j[1]:<10} {j[2]:<10} {j[3]:<10} {j[4]:<10}")
    print('-----------------------------------------------')

    for k, v in dt.items():
        r1,r2, r3,r4 = v
        print ("{:<8} {:<10} {:<10} {:<10} {:<10}".format(k, r1, r2,r3,r4))
    print('-----------------------------------------------')

except :
    print('enter the valid input')


    







    

