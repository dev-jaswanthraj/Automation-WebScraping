from xl import XlDataBase
import tkinter as tk
from tkinter import CENTER, StringVar, messagebox

class App(tk.Tk):
    def __init__(self) -> None:

        self.xlobj = XlDataBase()


        super().__init__()

        self.geometry("800x400")
        self.title("Get Data From Website")

        self.label = tk.Label(self, text="WELCOME", font=('Helvetica', 20))
        self.label.pack(pady=50)

        self.home_page = tk.Frame(self)
        

        self.sign_in_btn = tk.Button(self.home_page, text=" Sign In ", font=("Helvetica", 18), border=0, background="#2BC0E4", foreground="white", command=self.signin)
        self.sign_in_btn.grid(row=0, column=0, pady=10, sticky=tk.W+tk.E)

        self.sign_up_btn = tk.Button(self.home_page, text="Sign Up", font=("Helvetica", 18), border=0, background="#2BC0E4", foreground="white", command=self.signup)
        self.sign_up_btn.grid(row=1, column=0, pady=10, sticky=tk.W+tk.E)

        self.sign_up_btn = tk.Button(self.home_page, text="Exit", font=("Helvetica", 18), border=0, background="#f64f59", foreground="white", command=self.exit)
        self.sign_up_btn.grid(row=2, column=0, pady=20, sticky=tk.W+tk.E)

        self.home_page.pack()

    def exit(self):
        if messagebox.askokcancel("Exit", "Are you Sure?"):
            self.destroy()

    def signin(self):
        print("Sign In Page")
        self.signin_page = tk.Toplevel(self)
        self.signin_page.geometry("600x400")

        self.signin_label = tk.Label(self.signin_page, text="SIGN IN", font=('Helvetica', 20), pady=20)
        self.signin_label.pack()

        self.signinform = tk.Frame(self.signin_page)
        self.username = tk.Label(self.signinform, text="Full Name", font=('Helvetica', 16))
        self.username.grid(row=0, column=0, pady=10)
        self.password = tk.Label(self.signinform, text="Password", font=('Helvetica', 16))
        self.password.grid(row=1, column=0, pady=10)

        self.username_data = StringVar()
        self.password_data = StringVar()

        self.username_field = tk.Entry(self.signinform, textvariable=self.username_data, justify=CENTER, border=0)
        self.username_field.grid(row=0, column=1, padx=5)
        self.password_field = tk.Entry(self.signinform, textvariable=self.password_data, justify=CENTER, border=0)
        self.password_field.grid(row=1, column=1, padx=5)

        self.signinform.pack()

        self.submit = tk.Button(self.signin_page, text="Sign In", foreground="White", bg="#96c93d", font=('Helvetica', 20), border=0, command=self.auth_user)
        self.submit.pack(pady=20)


    def signup(self):
        print("Sign Up Page")
        self.signup_page = tk.Toplevel(self)
        self.signup_page.geometry("600x400")

        self.signup_label = tk.Label(self.signup_page, text="SIGN UP", font=('Helvetica', 20), pady=20)
        self.signup_label.pack()

        self.form = tk.Frame(self.signup_page)
        self.fullname = tk.Label(self.form, text="Full Name", font=('Helvetica', 16))
        self.fullname.grid(row=0, column=0, pady=10)
        self.pwd1 = tk.Label(self.form, text="Password", font=('Helvetica', 16))
        self.pwd1.grid(row=1, column=0, pady=10)
        self.pwd2 = tk.Label(self.form, text="Confirm Password", font=('Helvetica', 16))
        self.pwd2.grid(row=2, column=0, pady=10)

        self.fullname_data = StringVar()
        self.pwd1_data = StringVar()
        self.pwd2_data = StringVar()

        self.fullname_field = tk.Entry(self.form, textvariable=self.fullname_data, justify=CENTER, border=0)
        self.fullname_field.grid(row=0, column=1, pady=10)
        self.pwd1_field = tk.Entry(self.form, textvariable=self.pwd1_data, justify=CENTER, border=0)
        self.pwd1_field.grid(row=1, column=1, pady=10)
        self.pwd2_field = tk.Entry(self.form, textvariable=self.pwd2_data, justify=CENTER, border=0)
        self.pwd2_field.grid(row=2, column=1, pady=10, padx=5)

        

        self.form.pack()

        self.submit = tk.Button(self.signup_page, text="Register", foreground="White", bg="#96c93d", font=('Helvetica', 20), border=0, command=self.get_data_sign_up)
        self.submit.pack(pady=20)

    def get_data_sign_up(self):
        if self.fullname_data.get() != "" and self.pwd1_data.get() != "" and self.pwd2_data.get() != "":
            print("Something")
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
                    pass
                else:
                    self.password_data.set("")
                    self.password_field.focus_set()
                    messagebox.showinfo("Error", "Incorrect Password", parent=self.signin_page)
            elif not self.username_token:
                self.username_data.set("")
                self.password_data.set("")
                self.username_field.focus_set()
                messagebox.showinfo("Error", "Invalid UserName", parent=self.signin_page)
            
        
                    




if __name__ == "__main__":
    app = App()
    app.mainloop()




