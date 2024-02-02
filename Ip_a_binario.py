def int32_to_ip(int32):
    l=[]
    #convertidos de decimal a binario
    b=''
    while int32 >1:
        b+=str(int(int32)%2)
        int32/=2
    b+=str(int(int32)%2)#toma el residuo de la vicion entre 2 
    b=b[::-1]
    b[1:]
    #n = format(int32,'b')
    #n=b
    n2= int(b)
    try:#toma cada parte de la IP
        n3= int(f'{b[-32:-24]:.8}')
        n3=int(str(n3),2)
    except:
        n3=0
    try:
        n4= int(f'{b[-24:-16]:.8}')
        n4=int(str(n4),2)
    except:
        n4=0
    try:
        n5=int(f'{b[-16:-8]:.8}')
        n5=int(str(n5),2)
    except:
        n5=0
    try:
        n6=int(f'{b[-8:]:.8}')
        n6=int(str(n6),2)
    except:
        if n5==0 and n4 !=0:
            n6=n4
            n4=0
            n5=n3
            n3=0
        elif n4==0 and n5==0:
            n6=n3
            n3=0
        else:
            n6=n5
            n5=n4
            n4=n3
            n3=0
            
    l.append(str(n3)) 
    l.append(str(n4)) 
    l.append(str(n5))  
    l.append(str(n6)) 
    cadena = ".".join(l) 
    return cadena
int32_to_ip(1614999753)
