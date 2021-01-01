from time import *                                                                                                              # Required for using sleep()
import winsound
import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.withdraw()                                                                                                                 # Creates a tkinter window in background / Used to create a tkinter window.
a = True
note = 'STOP NOW. GO. TAKE A BREAK'
note1 = 'STOP NOW. GO. TAKE A BREAK FOR HALF AN HOUR.'

while a == True:
    print('Welcome to the Remindoro program')
    sleep(1)
    ans = input('Would you like to start the pomodoro session?(y/n)  ')
    if ans == 'y' or ans == 'Y':
        x = input('How much pomodoro sessions do you want?[Enter in numbers i.e. 2,5,etc.]')
        for a in (0,x):
            for i in (0,2):
                print('The timer is going to start. Be ready')
                sleep(3)
                print('START')
                winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
                sleep(1500)                                                                                                     # Timer set for 25 minutes.
                winsound.PlaySound('sound.wav',winsound.SND_FILENAME)                                                                                              
                messagebox.showinfo('Remindoro', note)                                                                          # Tkinter window displays alert for mini-break.
                sleep(300)                                                                                                      # Timer set for 5 minutes
            print('The timer is going to start. Be ready')
            sleep(3)
            print('START')
            winsound.PlaySound('sound.wav',winsound.SND_FILENAME)                                                                                    
            sleep(1500)                                                                                                         # Timer set for 25 minutes.
            winsound.PlaySound('sound.wav',winsound.SND_FILENAME)                                                                         
            messagebox.showinfo('Remindoro', note1)                                                                             # Tkinter window displays alert for large break.                                                     
            sleep(1800)
            print('CONGRATULATIONS !!!!')
            sleep(1)
    print('The pomodoro sessions have been finished successfully.')
    sleep(1)
    ans1 = input('Do you wish to take another pomodo session?(Y/N) :')
    if ans1 == 'n' or ans1 == 'N':
        a = False
    
print('Thank you for trying out the Remindoro program!')
