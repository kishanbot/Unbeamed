'''
This is only the first release. Its far from being perfect, but it still does the job.
I won't do a lot of updates on this project since roblox is kinda gay
coded by your sexy man vesper#0003
'''
import requests,base64,pyperclip
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Unbeamed || vesper#0003")
window.geometry("728x500")
window.maxsize(728, 500)
window.minsize(728, 500)
window.iconbitmap("assets/mylogo.ico")
window.config(background='#222222')
bg = PhotoImage(file='assets/background.png')
reverse = PhotoImage(file='assets/img0.png')
class Unbeamed:
    def reverse(self):
        found = False
        link = self.link.get()
        try:
            if "discord.com" in self.A:
                N = "https://discord.com"+self.A.split("discord.com")[1].split("'")[0]
                q = messagebox.askquestion("Unbeamed || vesper#0003",f"Webhook : {N}\nClick [YES] To copy in clipboard",icon='info')
                if q == "yes":
                    pyperclip.copy(f"Webhook : {N}")
                    messagebox.showinfo('Unbeamed || vesper#0003','Copied.');found=True;Unbeamed()
            elif "discordapp.com" in self.A:
                N = "https://discord.com"+self.A.split("discordapp.com")[1].split("'")[0]
                q = messagebox.askquestion("Unbeamed || vesper#0003",f"Webhook : {N}\nClick [YES] To copy in clipboard",icon='info')
                if q == "yes":
                    pyperclip.copy(f"Webhook : {N}")
                    messagebox.showinfo('Unbeamed || vesper#0003','Copied.');found=True;Unbeamed()
        except:pass
        try:
            N = self.A.split("returnUrl=")[1].split('"')[0].split('status=')[1]
            N = base64.b64decode(N);N= str(N).split("b'")[1].split("'")[0]
            CONTROL = "https://"+link.split("https://")[1].split("/")[0] +"/controller/"
            q = messagebox.askquestion("Unbeamed || vesper#0003",f"Token : {N}\nDashboard : {CONTROL}\nClick [YES] To copy in clipboard",icon='info')
            if q == "yes":
                pyperclip.copy(f"Token : {N}\nDashboard : {CONTROL}")
                messagebox.showinfo('Unbeamed || vesper#0003','Copied.');found=True;Unbeamed()
        except:pass
        try:
            N = self.A.split("login?session=")[1].split('"')[0]
            N = base64.b64decode(N);N = base64.b64decode(N);N= str(N).split("b'")[1].split("'")[0]
            q = messagebox.askquestion("Unbeamed || vesper#0003",f"Webhook : {N}\nClick [YES] To copy in clipboard",icon='info')
            if q == "yes":
                pyperclip.copy(f"Webhook : {N}")
                messagebox.showinfo('Unbeamed || vesper#0003','Copied.');found=True;Unbeamed()
        except:pass
        if found==False:
            messagebox.showerror('Unbeamed || vesper#0003',"Couldn't Find Anything. Wait for new updates.");Unbeamed()
    def verify(self):
        yas = False
        link = self.link.get()
        while True:
            if link.startswith('https'):
                try:
                    R = requests.get(link);self.A = R.text;yas=True;break
                except:messagebox.showerror("Unbeamed || vesper#0003", 'Invalid Link Or Connection Lost.');break
            else:messagebox.showerror('Unbeamed || vesper#0003','Invalid URL');break
        if yas:
            self.reverse()
        else:Unbeamed()
    def __init__(self):
        bgg = Label(window, image=bg, borderwidth=0)
        bgg.place(x=0, y=0)
        self.link = Entry(window,font=('SeoulHangang',10),bg='#D9D9D9', fg='#002FD3',width=74,borderwidth=0)
        self.link.place(x=93, y=293)
        reversebu = Button(window, image=reverse,bg='#000957',borderwidth=0, activebackground="#000957",command=self.verify)
        reversebu.place(x=265,y=351)
Unbeamed()
window.mainloop()