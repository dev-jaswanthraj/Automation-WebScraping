from tkinter import ttk
from test_selenium import  open_browser_with_amazon
from xl import XlDataBase
import tkinter as tk
from tkinter import messagebox, StringVar, CENTER
from tkinter.ttk import *
from PIL import Image, ImageTk
import pandas as pd
class App(tk.Tk):
    def __init__(self) -> None:

        self.xlobj = XlDataBase()
    
        super().__init__()

        self.geometry("800x400")
        self.title("Get Data From Website")

        self.label = tk.Label(self, text="WELCOME", font=('Helvetica', 20))
        self.label.pack(pady=50)

        self.home_page = tk.Frame(self)
        

        self.sign_in_btn = tk.Button(self.home_page, text=" Sign In ", font=("Helvetica", 18), border=0, background="#2BC0E4", foreground="white", command=self.signin, name="signin")
        self.sign_in_btn.grid(row=0, column=0, pady=10, sticky=tk.W+tk.E)

        self.sign_up_btn = tk.Button(self.home_page, text="Sign Up", font=("Helvetica", 18), border=0, background="#2BC0E4", foreground="white", command=self.signup)
        self.sign_up_btn.grid(row=1, column=0, pady=10, sticky=tk.W+tk.E)

        self.sign_up_btn = tk.Button(self.home_page, text="Exit", font=("Helvetica", 18), border=0, background="#f64f59", foreground="white", command=self.exit)
        self.sign_up_btn.grid(row=2, column=0, pady=20, sticky=tk.W+tk.E)

        self.back_img = Image.open("images/back-btn.png")
        self.new_back_img = ImageTk.PhotoImage(self.back_img.resize((80, 40), resample=1))

        self.home_page.pack()

    def exit(self):
        if messagebox.askokcancel("Exit", "Are you Sure?"):
            self.destroy()

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you Sure?", parent=self.scrapingpage):
            self.scrapingpage.destroy()
            self.deiconify()

    def signin(self):
        
        self.signin_page = tk.Toplevel(self, name = "signpage")
        self.signin_page.geometry("600x400")

        self.signin_label = tk.Label(self.signin_page, text="SIGN IN", font=('Helvetica', 20), pady=20)
        self.signin_label.pack()

        self.signinform = tk.Frame(self.signin_page)
        self.username = tk.Label(self.signinform, text="Full Name*", font=('Helvetica', 16))
        self.username.grid(row=0, column=0, pady=10)
        self.password = tk.Label(self.signinform, text="Password*", font=('Helvetica', 16))
        self.password.grid(row=1, column=0, pady=10)

        self.username_data = StringVar()
        self.password_data = StringVar()

        self.username_field = ttk.Entry(self.signinform, textvariable=self.username_data, justify=CENTER, font=('Helvetica', 14))
        self.username_field.focus_force()
        self.username_field.grid(row=0, column=1, padx=5, ipady=10, ipadx=16, pady=10)
        self.password_field = ttk.Entry(self.signinform, textvariable=self.password_data, justify=CENTER, font=('Helvetica', 14))
        self.password_field.grid(row=1, column=1, padx=5, ipady=10, ipadx=16, pady=10)

        self.signinform.pack()

        self.submit = tk.Button(self.signin_page, text="Sign In", foreground="White", bg="#96c93d", font=('Helvetica', 20), border=0, command=self.auth_user)
        self.submit.pack(pady=20)

        # self.back_img = Image.open("images/back-btn.png")
        # self.new_back_img = ImageTk.PhotoImage(self.back_img.resize((80, 40), resample=1))
        self.back_btn = tk.Button(self.signin_page, image=self.new_back_img, border=0, command=lambda:self.signin_page.destroy())
        self.back_btn.place(x = 0, y = 0)
        
    def signup(self):

        self.signup_page = tk.Toplevel(self)
        self.signup_page.geometry("600x400")

        self.signup_label = tk.Label(self.signup_page, text="SIGN UP", font=('Helvetica', 20), pady=20)
        self.signup_label.pack()

        self.form = tk.Frame(self.signup_page)
        self.fullname = tk.Label(self.form, text="Full Name*", font=('Helvetica', 16))
        self.fullname.grid(row=0, column=0, pady=10)
        self.pwd1 = tk.Label(self.form, text="Password*", font=('Helvetica', 16))
        self.pwd1.grid(row=1, column=0, pady=10)
        self.pwd2 = tk.Label(self.form, text="Confirm Password*", font=('Helvetica', 16))
        self.pwd2.grid(row=2, column=0, pady=10)

        self.fullname_data = StringVar()
        self.pwd1_data = StringVar()
        self.pwd2_data = StringVar()

        self.fullname_field = ttk.Entry(self.form, textvariable=self.fullname_data, justify=CENTER,font=('Helvetica', 14))
        self.fullname_field.grid(row=0, column=1, padx=5, ipady=10, ipadx=16, pady=10)
        self.pwd1_field = ttk.Entry(self.form, textvariable=self.pwd1_data, justify=CENTER,font=('Helvetica', 14))
        self.pwd1_field.grid(row=1, column=1, padx=5, ipady=10, ipadx=16, pady=10)
        self.pwd2_field = ttk.Entry(self.form, textvariable=self.pwd2_data, justify=CENTER,font=('Helvetica', 14))
        self.pwd2_field.grid(row=2, column=1, padx=5, ipady=10, ipadx=16, pady=10)

        

        self.form.pack()

        self.submit = tk.Button(self.signup_page, text="Register", foreground="White", bg="#96c93d", font=('Helvetica', 20), border=0, command=self.get_data_sign_up)
        self.submit.pack(pady=20)

        self.back_img = Image.open("images/back-btn.png")
        self.new_back_img = ImageTk.PhotoImage(self.back_img.resize((80, 40), resample=1))
        self.back_btn = tk.Button(self.signup_page, image=self.new_back_img, border=0, command=lambda: self.signup_page.destroy())
        self.back_btn.place(x = 0, y = 0)

    def get_data_sign_up(self):
        if self.fullname_data.get() != "" and self.pwd1_data.get() != "" and self.pwd2_data.get() != "":
            if self.pwd1_data.get() == self.pwd2_data.get():
                
                self.username = self.xlobj.set_data(self.fullname_data.get(), self.pwd1_data.get())
                self.signup_page.destroy()
                messagebox.showinfo("Success", "Successful Registred! \nYour Username : {}".format(self.username))
            else:
                messagebox.showinfo("Error", "Password is not match with Confirm Password", parent=self.signup_page)
                self.pwd1_field.focus_set()
                self.pwd1_data.set("")
                self.pwd2_data.set("")
        else:
            messagebox.showinfo("Error", "All Fields Should be Filled", parent=self.signup_page)
            #signup_page.after(10000, lambda:signup_page.destroy())

    def auth_user(self):
    
        if self.username_data.get() == "" or self.password_data.get() == "":
            messagebox.showinfo("Error", "All field are to be filled.", parent=self.signin_page)
        else:    
            self.username_token = False
            for item in self.xlobj.get_data():
                if self.username_data.get() in item.values():
                    self.username_token = True
                    break
            if self.username_token:
                if item['Password'] == self.password_data.get():
                    self.signin_page.destroy()
                    self.webScraping(item)
                else:
                    self.password_data.set("")
                    self.password_field.focus_set()
                    messagebox.showinfo("Error", "Incorrect Password", parent=self.signin_page)
            elif not self.username_token:
                self.username_data.set("")
                self.password_data.set("")
                self.username_field.focus_set()
                messagebox.showinfo("Error", "Invalid UserName", parent=self.signin_page)

    def get_data_selenium(self, website):

        self.result_page = tk.Toplevel(self.data_input_area)
        self.result_page.geometry('800x400')
        self.data_input_area.withdraw()
    
        self.label = tk.Label(self.result_page, text= website+" Result Page", font=('Helvetica', 20), pady=20)
        self.label.pack()
        
        self.back_btn = tk.Button(self.result_page, image=self.new_back_img, border=0, command=lambda:self.scrapingpage.wm_deiconify() or self.result_page.destroy())
        self.back_btn.place(x = 0, y = 0)
        
        self.result_area = tk.Frame(self.result_page)

        if website == "Amazon":
            try:
                self.file_name = open_browser_with_amazon(self.input_data.get())
                self.scrapingpage.withdraw()
                self.suc_label = tk.Label(self.result_area, text= "Successfully completed ✔", font=('Helvetica', 20), pady=20, foreground="#96c93d")
                self.suc_label.grid(column=0, row=0, pady=20)
                self.open_btn = tk.Button(self.result_area, text="Open {}".format(self.file_name), foreground="White", bg="#96c93d", font=('Helvetica', 20), border=0, command=self.tkexcel)
                self.open_btn.grid(column=0, row=1, pady=50)
                
            except:
                self.error_label = tk.Label(self.result_area, text="Something Went Wrong",font=('Helvetica', 20), foreground="#f64f59")
                self.error_label.grid(column=0, row=0, pady=100)

        self.result_area.pack()


    def tkexcel(self):

        self.win = tk.Toplevel(self.result_page)
        self.win.geometry("900x450")

        self.back_img = Image.open("images/back-btn.png")
        self.new_back_img = ImageTk.PhotoImage(self.back_img.resize((80, 40), resample=1))
        self.back_btn = tk.Button(self.win, image=self.new_back_img, border=0, command=lambda:self.scrapingpage.wm_deiconify() or self.result_page.destroy())
        self.back_btn.place(x = 0, y = 0)

        self.frame = tk.Frame(self.win)
        self.frame.pack(pady=20)

        
        self.file = pd.read_excel(self.file_name)
        self.tree = ttk.Treeview(self.frame, height='900')

        self.tree['columns'] = list(self.file)
        self.tree['show'] = 'headings'

        for col in self.tree['column']:
            self.tree.heading(col, text=col)

        self.data = self.file.to_numpy().tolist()
        for row in self.data:
            self.tree.insert("", "end", values=row)
        
        self.tree.pack(ipady='800')

    def test(self, website):
            if self.input_data.get() == "":
                messagebox.showinfo(title="Error", message="Field Can't Empty", parent = self.data_input_area)
            else:
                self.get_data_selenium(website)
    
    def Generic_Data_Scrping(self, website:str):
        self.data_input_area = tk.Toplevel(self.scrapingpage)
        self.data_input_area.geometry('800x400')

        self.label = tk.Label(self.data_input_area, text= website.upper(), font=('Helvetica', 20), pady=8)
        self.label.pack()

        self.back_img = Image.open("images/back-btn.png")
        self.new_back_img = ImageTk.PhotoImage(self.back_img.resize((80, 40), resample=1))
        self.back_btn = tk.Button(self.data_input_area, image=self.new_back_img, border=0, command=lambda:self.data_input_area.destroy())
        self.back_btn.place(x = 0, y = 0)

        self.input_frame = tk.Frame(self.data_input_area)

        self.input_label = tk.Label(self.input_frame, text="Search for product*",font=('Helvetica', 20), pady=30)
        self.input_label.grid(column=0, row=0)

        self.input_data = StringVar()
        self.input_field = ttk.Entry(self.input_frame, textvariable=self.input_data, justify=CENTER, font=('Helvetica', 20))
        self.input_field.grid(column=0, row=1, pady=20, ipadx=50, ipady=18)

        self.input_frame.pack()
        
        self.search_btn = tk.Button(self.data_input_area, text="Search",foreground="White", bg="#96c93d", font=('Helvetica', 20), border=0, command=lambda:self.test(website = website))
        self.search_btn.pack()
    
    def webScraping(self, userData):
        self.withdraw()
        self.scrapingpage = tk.Toplevel(self)
        self.scrapingpage.geometry('800x400')

        
        # self.user_img = Image.open("images/usericon.jpg")
        # self.new_user_img = ImageTk.PhotoImage(self.user_img.resize((25, 25), Image.Resampling.LANCZOS))
        # self.user_label = tk.Label(self.scrapingpage, image = self.new_user_img)
        # self.user_label.place(x = 10, y = 15)

        self.icon = tk.Label(self.scrapingpage, text="🐍", font=('Helvetica', 20), foreground="#96c93d")
        self.icon.place(x=10, y = 5)
        
        self.username_label = tk.Label(self.scrapingpage, text="Hello, {}!".format(userData['FullName']), font=('Helvetica', 20))
        self.username_label.place(x = 42, y = 10)

        self.logout_btn = tk.Button(self.scrapingpage, text="Logout",font=("Helvetica", 18), border=0, background="#f64f59", foreground="white", command=self.logout)
        self.logout_btn.place(x = 700, y = 10 )

        self.hr = tk.Canvas(self.scrapingpage,width=700, height=2, bg="#bdc3c7").pack(pady=70)
        
        self.apps = tk.Frame(self.scrapingpage)

        self.amazon_img = Image.open("images/amazon.jpg")
        self.new_amazon_img = ImageTk.PhotoImage(self.amazon_img.resize((75, 75), Image.Resampling.LANCZOS))
        self.amazon_btn = tk.Button(self.apps, image = self.new_amazon_img, border=0, command=lambda: self.Generic_Data_Scrping("Amazon"))
        self.amazon_btn.grid(column=0, row=0, pady=6, padx=10)

        # self.flipkart_img = Image.open("images/flipcart.webp")
        # self.new_flipkart_img = ImageTk.PhotoImage(self.flipkart_img.resize((75, 75), Image.Resampling.LANCZOS))
        # self.flipkart_btn = tk.Button(self.apps, image = self.new_flipkart_img, border=0, pady=20, command=lambda: self.Generic_Data_Scrping("Flipkart"))
        # self.flipkart_btn.grid(column=2, row=0, pady=10, padx=10)

        self.apps.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()