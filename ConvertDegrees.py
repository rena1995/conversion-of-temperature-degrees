#Converts temprature degrees from one scale to another
 
def Celcius_to_Fahrenheit(degrees):
    f_degrees=degrees*(9/5)+32
    print("{} Celsius degrees are equal to {} Fahrenheit degrees ".format(degrees,f_degrees))

def Celcius_to_Kelvin(degrees):
    k_degrees=degrees+273.15
    print("{} Celsius degrees are equal to {} Kelvin degrees ".format(degrees,k_degrees))

def Celcius_to_Rankine(degrees):
    r_degrees=(degrees+273.15)*(9/5)
    print("{} Celsius degrees are equal to {} Rankine degrees ".format(degrees,r_degrees))

def Fahrenheit_to_Celcius(degrees):
    c_degrees=(degrees-32)*5/9
    print("{} Fahrenheit degrees are equal to {} Celcius degrees ".format(degrees,c_degrees))

def Fahrenheit_to_Kelvin(degrees):
    k_degrees=(degrees+459.67)*5/9
    print("{} Fahrenheit degrees are equal to {} Kelvin degrees ".format(degrees,k_degrees))

def Fahrenheit_to_Rankine(degrees):
    r_degrees=degrees+459.67
    print("{} Fahrenheit degrees are equal to {} Rankine degrees ".format(degrees,r_degrees))

def Kelvin_to_Celcius(degrees):
    c_degrees=degrees-273.15
    print("{} Kelvin degrees are equal to {} Celcius degrees ".format(degrees,c_degrees))

def Kelvin_to_Fahrenheit(degrees):
    f_degrees=degrees*9/5-459.67
    print("{} Kelvin degrees are equal to {} Fahrenheit degrees ".format(degrees,f_degrees))

def Kelvin_to_Rankine(degrees):
    r_degrees=degrees*9/5
    print("{} Kelvin degrees are equal to {} Rankine degrees ".format(degrees,r_degrees))

def Rankine_to_Celcius(degrees):
    c_degrees=(degrees-491.67)*5/9
    print("{} Rankine degrees are equal to {} Celcius degrees ".format(degrees,c_degrees))

def Rankine_to_Fahrenheit(degrees):
    f_degrees=degrees-459.67
    print("{} Rankine degrees are equal to {} Fahrenheit degrees ".format(degrees,f_degrees))

def Rankine_to_Kelvin(degrees):
    k_degrees=degrees*5/9
    print("{} Rankine degrees are equal to {} Kelvin degrees ".format(degrees,k_degrees))

answer="Y"
data=""
while(answer=="Y"):
    if(data=="wrong input"):data=input()
    else:data=input("Give degrees, their scale and the scale you want to convert to.\nChoose between C,F,K,R.\n(ex.35 C F)\n")
    if (len(data.split())<3):
        print("Wrong input.Please enter the data as the example shows.")
        data = "wrong input"
        continue
    degrees=data.split()[0]
    scale=data.split()[1].upper()
    convertedScale=data.split()[2].upper()
    if (degrees[0]=="-" or degrees.find("-")==-1):
        if (degrees.replace('-','',1).replace('.','',1).isdigit()):
            degrees=float(degrees)
        else:
            print("Wrong input.Please enter a number")
            data="wrong input"
            continue
    else:
        print("Wrong input.Please enter a number")
        data="wrong input"
        continue
    if((scale!="C" and scale!="F" and scale!="K" and scale!="R") or (convertedScale!="C" and convertedScale!="F" and
       convertedScale!="K" and convertedScale!="R")):
        print("Wrong input.Please choose one of C,F,K,R")
        data="wrong input"
        continue
    elif(scale=="C"):
        if(convertedScale=="F"):
            Celcius_to_Fahrenheit(degrees)
        elif (convertedScale=="K"):
            Celcius_to_Kelvin(degrees)
        elif (convertedScale=="R"):
            Celcius_to_Rankine(degrees)
        elif(convertedScale=="C"):print("{} Celcius degrees are equal to {} Celcius degrees ".format(degrees,degrees))
    elif(scale=="F"):
        if(convertedScale=="C"):
            Fahrenheit_to_Celcius(degrees)
        elif (convertedScale=="K"):
            Fahrenheit_to_Kelvin(degrees)
        elif (convertedScale=="R"):
            Fahrenheit_to_Rankine(degrees)
        elif (convertedScale == "F"):
            print("{} Fahrenheit degrees are equal to {} Fahrenheit degrees ".format(degrees, degrees))
    elif(scale=="K"):
        if(convertedScale=="C"):
            Kelvin_to_Celcius(degrees)
        elif (convertedScale=="F"):
            Kelvin_to_Fahrenheit(degrees)
        elif (convertedScale=="R"):
            Kelvin_to_Rankine(degrees)
        elif (convertedScale == "K"):
            print("{} Kelvin degrees are equal to {} Kelvin degrees ".format(degrees, degrees))
    elif(scale=="R"):
        if(convertedScale=="C"):
            Rankine_to_Celcius(degrees)
        elif (convertedScale=="F"):
            Rankine_to_Fahrenheit(degrees)
        elif (convertedScale=="K"):
            Rankine_to_Kelvin(degrees)
        elif (convertedScale == "R"):
            print("{} Rankine degrees are equal to {} Rankine5 degrees ".format(degrees, degrees))
    answer=input("Do you want another conversion? (y/n) ").upper()