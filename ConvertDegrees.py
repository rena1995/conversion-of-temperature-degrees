#Converts temprature degrees from one scale to another

def Celcius_to_Farenhait(c):
    c=float(c)
    f=c*(9/5)+32
    return f

def Celcius_to_Kelvin(c):
    c=float(c)
    k=c+273.15
    return k

def Celcius_to_Rankine(c):
    c=float(c)
    r=(c+273.15)*(9/5)
    return r

def Farenhait_to_Celcius(f):
    f=float(f)
    c=(f-32)*5/9
    return c

def Farenhait_to_Kelvin(f):
    f=float(f)
    k=(f+459.67)*5/9
    return k

def Farenhait_to_Rankine(f):
    f=float(f)
    r=f+459.67
    return r

def Kelvin_to_Celcius(k):
    k=float(k)
    c=k-273.15
    return c

def Kelvin_to_Farenhait(k):
    k=float(k)
    f=k*9/5-459.67
    return f

def Kelvin_to_Rankine(k):
    k=float(k)
    r=k*9/5
    return r

def Rankine_to_Celcius(r):
    r=float(r)
    c=(r-491.67)*5/9
    return c

def Rankine_to_Farenhait(r):
    r=float(r)
    f=r-459.67
    return f

def Rankine_to_Kelvin(r):
    r=float(r)
    k=r*5/9
    return k

