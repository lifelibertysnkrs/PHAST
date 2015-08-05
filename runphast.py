#### PRECISION HIGH ALTITUDE STAR TRACKER ###
##########DEVELOPED AT NASA GODDARD##########


 
import subprocess
import serial 
def focusCam(ms, increments): #ms indicates shutter speed, increments indicates how many steps the motor takes to turn the focus all the way
    focused = False; #Starts with assumption that camera is not focused
    ser = serial.Serial('/dev/tty.usbserial', 9600) #Sets up Arduino
    ser.write("0") #Causes Arduino to reset focus
    while focused ==0 and increments != 0:
        #Takes picture
        subprocess.check_output(["./TakePic/bin", str(ms)]) 
        #Runs astrometry
        subprocess.check_output(["solve-field", "/TakePic/pics/img-"+ str(ms) +".png", ">", "focus.txt"]) 
        #If astrometry solved, returns true
        focusfile = open("focus.txt", "r")
        for line in focusfile:
            if "solved with index" in line: focused = True
        if focused == 0:
            ser.write('1') #In arduino code, recieving 1 causes motor two turn focus by one increment
            increment = increment -1
    focusfile.close()

    return focused

def getLoc(ms):
    subprocess.check_output(["./TakePic/bin", str(ms)])

    subprocess.check_output(["solve-field", "/TakePic/pics/img-"+ str(ms) +".png", ">", "results.txt"])

    results = open("focus.txt", "r")
    for line in results:
            
        if "Field center: (RA,Dec)" in line: return line
        
    focusfile.close()

    return(1)

def runPhast(ms, increment):
    focused = focusCam(ms, increment)
    loc = getLoc(ms)
    
    

    

    

