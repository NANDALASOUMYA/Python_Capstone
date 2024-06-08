import random  # Importing the random module to generate random numbers
import smtplib  # Importing the smtplib module to send emails
from tkinter import *  # Importing the entire tkinter module for GUI development

# Function to generate a 6-digit OTP (One-Time Password)
def generateOTP():
    randomCode = ''.join(str(random.randint(0, 9)) for i in range(6))  # Generating a random 6-digit code
    return randomCode  # Returning the generated OTP

# Email credentials and OTP generation
sender = 'nandalasoumya69@gmail.com'  # Sender's email address
password = 'xuwp bzro fnut qfia'  # Sender's email password (Note: For security, use environment variables or secure storage for passwords)
code = generateOTP()  # Generating OTP using the generateOTP() function

# Function to connect to SMTP server and send email with OTP
def connectingSender():
    receiver = receiverMail.get()  # Getting receiver's email address from the GUI Entry widget
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connecting to Gmail SMTP server on port 587
    server.starttls()  # Starting TLS encryption for secure communication
    server.login(sender, password)  # Logging in to the SMTP server using sender's credentials
    sendingMail(receiver, server)  # Calling sendingMail() function to send the OTP email

# Function to send the OTP email
def sendingMail(receiver, server):
    msg = 'Hello! \n This is your OTP is ' + code  # Composing the email message with the OTP
    server.sendmail(sender, receiver, msg)  # Sending the email to the receiver
    server.quit()  # Closing the SMTP server connection

# Function to check the entered OTP and display verification result
def checkOTP():
    if code == codeEntry.get():  # Checking if the entered OTP matches the generated OTP
        accept = Label(otp, text='Successful Verification!', fg='green', font=('Arial', 20))  # Label for successful verification message
        accept.place(x=230, y=350)  # Placing the label in the GUI window
    else:
        refuse = Label(otp, text='Unsuccessful Verification!', fg='red', font=('Arial', 20))  # Label for unsuccessful verification message
        refuse.place(x=230, y=350)  # Placing the label in the GUI window

# Creating the main GUI window
otp = Tk()  # Creating a tkinter window
otp.title('OTP Verification')  # Setting the title of the window
otp.geometry('750x400')  # Setting the size of the window
otp.config(bg='#FFF1DC')  # Setting the background color of the window

# Creating and placing GUI elements (labels, entry widgets, and buttons) in the window
mailMsg = Label(otp, text="E-Mail", justify=LEFT, bg='#FFF1DC', font=("Arial", 16))  # Label for email message
mailMsg.place(x=15, y=40)  # Placing the label at specific coordinates in the window

receiverMail = Entry(otp, text='mail.gmail.com', width=35, font=("Arial", 20), borderwidth=0)  # Entry widget for entering receiver's email
receiverMail.place(x=100, y=40)  # Placing the entry widget at specific coordinates in the window

sendOTP = Button(otp, text="send OTP", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#AA5656", fg="black", command=connectingSender)  # Button to send OTP
sendOTP.place(x=280, y=100)  # Placing the button at specific coordinates in the window

otpMsg = Label(otp, text="OTP", bg='#FFF1DC', font=('Arial', 16))  # Label for OTP message
otpMsg.place(x=15, y=210)  # Placing the label at specific coordinates in the window

codeEntry = Entry(otp, width=6, font=("Arial", 20), borderwidth=0)  # Entry widget for entering OTP
codeEntry.place(x=100, y=210)  # Placing the entry widget at specific coordinates in the window

verify = Button(otp, text="Verify", width=8, height=1, font=("Arial", 20), borderwidth=0, bg="#AA5656", fg="black", command=checkOTP)  # Button to verify OTP
verify.place(x=280, y=280)  # Placing the button at specific coordinates in the window

otp.mainloop()  # Starting the main event loop of the GUI window to handle user interactions
