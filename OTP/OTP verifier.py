from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox


class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450")
        self.resizable(False, False)
        self.n = random.randint(1000,9999)
        self.client=Client("ACf4120e8589af590857551fed0d10198a","62beed498df3e30f7eef6047307de95b") #api and api secret key
        self.client.messages.create(to =["+916000798277"], from_ = "+17079408179", body=self.n) #write phone numbers to and from sections


    def Labels(self):
        self.c=Canvas(self, bg="#D9D9D6", width=400, height=280)
        self.c.place(x=100, y=60)

        self.Login_Title=Label(self, text="OTP Verification", font="bold, 20", bg="white")
        self.Login_Title.place(x=210,y=90)

    def Entry(self):
        self.User_Name=Text(self,borderwidth=2, wrap="word", width=29, height=2)
        self.User_Name.place(x=190, y=160)

    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit.png")
        self.submitButton=Button(self, image=self.submitButtonImage, command=self.checkOTP, border=0)
        self.submitButton.place(x=230, y= 200)

        self.resendOTPImage=PhotoImage(file="resend.png")
        self.resendOTP=Button(self, image=self.resendOTPImage, command=self.resendOTP, border=0)
        self.resendOTP.place(x=220, y=280)

    def checkOTP(self):
        try:
            self.userInput=int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo", "Login Success!")
                self.n="done"

            elif self.n== "done":
                messagebox.showinfo("showinfo", "Already Login.")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP!")
        except:
            messagebox.showinfo("showinfo", "Invalid OTP!")

    def resendOTP(self):
        self.n = random.randint(1000,9999)
        self.client=Client("ACf4120e8589af590857551fed0d10198a","62beed498df3e30f7eef6047307de95b")
        self.client.messages.create( to =["+916000798277"], from_="+17079408179", body=self.n)



window=otp_verifier()
window.Labels()
window.Entry()
window.Buttons()
window.mainloop()

