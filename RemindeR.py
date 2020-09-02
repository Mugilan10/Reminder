from time import *                                                                                                                                                       # Required for using sleep()
import tkinter
from tkinter import messagebox
root=tkinter.Tk()
root.withdraw()                                                                                                                                                             # Creates a tkinter window in background.
x=True
current_time=asctime()                                                                                                                                                # Retrieves current day, date and time
print('Welcome to The RemindeR program')
sleep(1)
print('The current day and time is:', current_time)                                                                                                        # Displays current day, date and time
sleep(1)
Note=input('Enter what you would like to be reminded about : ')                                                                                 # Asks for the information; to be reminded.
sleep(1)
print('Ok. Noted')
while(x):
    sleep(1)
    menu_option=input('Do you like the default time interval(A or a) or want it customised(B or b) ? ')                         # Primary menu is displayed.
    sleep(1)
    print('Ok. Noted')
    if(menu_option=='A' or menu_option=='a'):
        print('The RemindeR is set to the default time interval that is 1 hour')
        print('You can minimise the program if you need to.')
        sleep(3600)
        messagebox.showinfo("Reminder",Note)                                                                                                              # Tkinter window displays the reminder.
        sleep(1)
        exit_option=input(print('Do you want to set another RemindeR ?(y/n) '))                                                             # Confirmation dialogue is being asked.
        if(exit_option=='Y' or exit_option=='y'):
            continue
        else:
            x=False
        sleep(1)
    elif(menu_option=='B' or menu_option=='b'):
        sleep(1)
        while(x):
            sub_menu_option=input('Do you want to input the time interval in minutes(M or m) or hours(H or h) ?')       # Secondary menu is displayed.
            if(sub_menu_option=='M' or sub_menu_option=='m'):
                sleep(1)
                minutes=eval(input('How many minutes after should I remind you ?'))
                sleep(1)
                print('Ok. The RemindeR is set for ',minutes,' minute(s)')
                print('You can minimise the program if you need to.')
                sleep(minutes*60)
                messagebox.showinfo("Reminder",Note)                                                                                                     # Tkinter window displays the reminder.
                sleep(1)
                exit_option=input(print('Do you want to set another RemindeR ?(y/n) "Please ignore the "None"" '))          # Confirmation dialogue is being asked.
                if(exit_option=='Y' or exit_option=='y'):
                    continue
                else:
                    x=False
                    sleep(1)
            elif(sub_menu_option=='h' or sub_menu_option=='H'):
                hours=eval(input('How many hours after should I remind you ? '))
                minutes1=hours*60
                seconds=hours*3600
                print('Ok. The RemindeR is set after ',int(hours),' hours ',int(minutes1),' minutes ',int(seconds),' seconds')
                print('You can minimise the program if you need to.')
                sleep(seconds)
                messagebox.showinfo("Reminder",Note)                                                                                                     # Tkinter window displays the reminder.
                sleep(1)
                exit_option=input(print('Do you want to set another RemindeR ?(y/n) "Please ignore the "None"" '))          # Confirmation dialogue is being asked.
                if(exit_option=='Y' or exit_option=='y'):
                    continue
                else:
                    x=False
                    sleep(1)
            else:
                print('The option you have entered is invalid.')
                sleep(1)
                print('Please enter only the given options.')
                sleep(1)                                                                                                                                                                
    else:
        print('The option you have entered is invalid.')
        sleep(1)
        print('Please enter only the given options.')
        sleep(1)                                                                                                                                                                #Returns user back to the primary menu.
print('Thank you for trying out the RemindeR')
print('Glad to be of your service')
