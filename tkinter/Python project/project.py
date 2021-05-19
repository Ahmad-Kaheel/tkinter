from tkinter import *
import sqlite3
import time;
from tkinter import StringVar
from tkinter import ttk
from tkinter import messagebox


class  restaurantProject:
    def __init__(self):
# -------------------------------# first window --------------------------------------------------------------------

        self.root = Tk()
        self.root.geometry("1600x800+0+0")
        self.root.title("restaurant order System")
        self.fr = Frame(self.root, width=1200, height=100, relief=SUNKEN).pack()
        logo = PhotoImage(file="qu.gif")# image name
        lbl_image = Label(self.fr, image=logo).pack()

        lbl_title = Label(self.fr, text=" University restaurant", font=('arial', 30, 'bold'),
                          fg="red", bd=10,bg="powder blue", anchor='w').pack()

        btnlogin = Button(self.fr, height=1, width=10, padx=2, pady=2, fg='blue', font=('arial', 14, 'bold'),
                          text="Login Page", bd=10, command=self.Fun_win_login).pack()





        # =========================Database orders ================

        self.db = sqlite3.connect("Students.db")
        self.db.row_factory = sqlite3.Row
        self.db.execute("create table if not exists  stud1(id integer primary key  autoincrement,"
                        "chicken integer,name text,m1 integer ,m2 integer ,m3 integer ,sum integer,ave float)")
        self.db.commit()
        # ========================End Database ======================

        self.win_students = Toplevel()
        self.win_students.withdraw()
        self.win_login = Toplevel()
        self.win_login.withdraw()




#-----------------------------------------------second window ----------------------------------------------------------
        # =====================================Start login=========================

        self.win_login.title("  Login Page  ")
        self.win_students.title(" Restaurant System ")
        width = 1200
        height = 800
        self.screen_width = self.win_login.winfo_screenwidth()  # width of the screen
        self.screen_height = self.win_login.winfo_screenheight()  # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (self.screen_width / 2) - (width / 2)
        y = (self.screen_height / 2) - (height / 2)
        self.win_login.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.win_login.resizable(0, 0)
        # ==============================VARIABLES======================================
        self.USERNAME = StringVar()
        self.PASSWORD = StringVar()
        self.USERNAME.set( 'admin' )
        # ==============================FRAMES=========================================
        Top = Frame(self.win_login, bd=2, relief=RIDGE)
        Top.pack(side=TOP, fill=X)
        Form = Frame(self.win_login, height=200)
        Form.pack(side=TOP, pady=20)

        # ==============================LABELS (login window )=========================================
        lbl_title = Label(Top, text=" Restaurant System ", font=('arial', 15) , fg = "red" , bg = "yellow")
        lbl_title.pack(fill=X)
        lbl_username = Label(Form, text="Username:", font=('arial', 14), bd=15)
        lbl_username.grid(row=0, sticky="e")
        lbl_password = Label(Form, text="Password:", font=('arial', 14), bd=15)
        lbl_password.grid(row=1, sticky="e")
        self.lbl_text = Label(Form)
        self.lbl_text.grid(row=2, columnspan=2)

        # ==============================ENTRY WIDGETS==================================
        username = Entry(Form, textvariable=self.USERNAME, font=(14))
        username.grid(row=0, column=1)
        password = Entry(Form, textvariable=self.PASSWORD, show="*", font=(14))
        password.grid(row=1, column=1)

        # ==============================BUTTON WIDGETS=================================
        btn_login = Button(Form, text="Login", width=45, command=self.Fun_Login)
        btn_login.grid(pady=25, row=3, columnspan=2)
        # btn_login.bind('<Return>', self.Fun_Login)



#------------------------------------------------third----------------------------------------------------------------
        # ============================begin of widgets restaurant =============
        self.f1 = Frame(self.win_students, width=1200, height=20, bg="powder blue", relief=SUNKEN)
        self.f1.grid(row=0, column=0)

        self.f2 = Frame(self.win_students, width=1200, height=100, relief=SUNKEN)
        self.f2.grid(row=2, column=0)

        self.f3 = Frame(self.win_students, width=1200, height=100, bg="yellow", relief=SUNKEN)
        self.f3.grid(row=3, column=0)

        self.localtime = time.asctime(time.localtime(time.time()))
        self.lbInfo = Label(self.f1, font=('arial', 50, 'bold'), text="Restaurant System", fg="red",
                            bd=10,
                            anchor='w')
        self.lbInfo.grid(row=0, column=0)
        self.lbInfo = Label(self.f1, font=('arial', 14, 'bold'), text=self.localtime, fg="Steel Blue", bd=10,
                            anchor='w')
        self.lbInfo.grid(row=1, column=0)

        self.no = StringVar()
        self.name = StringVar()
        self.m1 = StringVar()
        self.m2 = StringVar()
        self.m3 = StringVar()
        self.sum = StringVar()
        self.ave = StringVar()

        # ============================================================================

        self.lbNo = Label(self.f2, font=('arial', 10, 'bold'), text="Number", bd=10)
        self.lbNo.grid(row=0, column=0)
        self.EntryNo = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.no )
        self.EntryNo.grid(row=0, column=1, pady=1)
        self.EntryNo.focus()

        self.lbName = Label(self.f2, font=('arial', 10, 'bold'), text="Name", bd=10)
        self.lbName.grid(row=0, column=2)
        self.EntryName = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.name)
        self.EntryName.grid(row=0, column=3, pady=1)
        self.EntryName.focus()

        self.lbM1 = Label(self.f2, font=('arial', 10, 'bold'), text="Chicken", bd=10)
        self.lbM1.grid(row=1, column=0)
        self.EntryM1 = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.m1)
        self.EntryM1.grid(row=1, column=1, pady=1)
        self.EntryM1.focus()

        self.lbM2 = Label(self.f2, font=('arial', 10, 'bold'), text="Meat", bd=10)
        self.lbM2.grid(row=2, column=0)
        self.EntryM2 = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.m2)
        self.EntryM2.grid(row=2, column=1, pady=1)
        self.EntryM2.focus()

        self.lbM3 = Label(self.f2, font=('arial', 10, 'bold'), text="Rice", bd=10)
        self.lbM3.grid(row=3, column=0)
        self.EntryM3 = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.m3)
        self.EntryM3.grid(row=3, column=1, pady=1)
        self.EntryM3.focus()

        self.lbSum = Label(self.f2, font=('arial', 10, 'bold'), text="Total", bd=10)
        self.lbSum.grid(row=4, column=0)
        self.EntrySum = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.sum, state="readonly")
        self.EntrySum.grid(row=4, column=1, pady=1)

        self.lbAve = Label(self.f2, font=('arial', 10, 'bold'), text="After VAT", bd=10)
        self.lbAve.grid(row=5, column=0)
        self.EntryAve = ttk.Entry(self.f2, width=20, font=('Arial', 10), textvariable=self.ave, state="readonly")
        self.EntryAve.grid(row=5, column=1, pady=1)



#--------------------------------------------------Buttons-----------------------------------------------------------
        # ===============================================================================

        self.btnShow = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                              text="Show", bd=10, command=self.FunShow).grid(row=3, column=4)

        self.btnAdd = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                             text="Add", bd=10, command=self.FunAdd).grid(row=4, column=4)

        self.btnDel = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                             text="Delete", bd=10, command=self.FunDel).grid(row=3, column=3)

        self.btnUpdate = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                                text="Update", bd=10, command=self.FunUpdate).grid(row=4, column=3)
        self.btnClear = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                               text="Clear", bd=10, command=self.FunClear).grid(row=5, column=3)
        btn_back = Button(self.f2, height=1, width=10, padx=2, pady=2, fg='black', font=('arial', 10, 'bold'),
                          text="Back", bd=10, command=self.Back).grid(row=5, column=4)

        # ============================================================================

        self.tv = ttk.Treeview(self.f3)
        self.tv.grid(row=0, column=0)

        self.tv.heading('#0', text='ID')

        self.tv.configure(column=('#Number', '#Name', '#Chicken', '#Meat', '#Rice', '#Total', '#After VAT'))
        self.tv.column('#0', width=80, anchor='center')
        self.tv.column('#Number', width=80, anchor='center')
        self.tv.column('#Name', width=80, anchor='center')
        self.tv.column('#Chicken', width=80, anchor='center')
        self.tv.column('#Meat', width=80, anchor='center')
        self.tv.column('#Rice', width=80, anchor='center')
        self.tv.column('#Total', width=80, anchor='center')
        self.tv.column('#After VAT', width=80, anchor='center')



        self.tv.heading('#Number', text='Number')
        self.tv.heading('#Name', text='Name')
        self.tv.heading('#Chicken', text='Chicken')
        self.tv.heading('#Meat', text='Meat')
        self.tv.heading('#Rice', text='Rice')
        self.tv.heading('#Total', text='Total')
        self.tv.heading('#After VAT', text='After VAT')

# self.tv.bind("<<TreeviewSelect>>", self.on_tree_select2)
        self.binding()

        # ======================End widgets Students=========================
        self.root.mainloop()

    # ======================begin of login Funcations ===================

    def Fun_win_login(self):
        print("hhhhhhh")
        self.root.withdraw()
        # self.root.resizable(0,0)
        self.win_login.deiconify()


#-------------------------------------------username and paassword---------------------------------
    def Fun_Login(self, event=None):
        self.Database()
        if self.USERNAME.get() == "" or self.PASSWORD.get() == "":
            self.lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `users` WHERE `username` = ? AND `password` = ?",
                           (self.USERNAME.get(), self.PASSWORD.get()))
            if cursor.fetchone() is not None:
                self.HomeWindow()
                self.USERNAME.set("")
                self.PASSWORD.set("")
                self.lbl_text.config(text="")
            else:
                self.lbl_text.config(text="Invalid username or password", fg="red")
                self.USERNAME.set("")
                self.PASSWORD.set("")
        cursor.close()
        conn.close()
        # ==============================METHODS========================================

    def Database(self):
        global conn, cursor
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `users` (user_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `users` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `users` (username, password) VALUES('admin', 'admin')")
            conn.commit()

    def HomeWindow(self):
        messagebox.showinfo(title="Login!", message="Successfully Login!")
        self.page2()

        width = 1200
        height = 800
        x = (self.screen_width / 2) - (width / 2)
        y = (self.screen_height / 2) - (height / 2)

        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)

    def page2(self):
        # seems to just remove the window from the screen, after which the window has a state of "withdrawn"
        self.win_login.withdraw()
        self.win_students.deiconify()

    def Back(self):
        self.win_students.withdraw()
        self.root.deiconify()
        self.root.resizable(0, 0)


    def binding(self):
        self.tv.bind("<<TreeviewSelect>>", self.on_tree_select2)

    # ===============================================================================
    def on_tree_select(self, event):
        print("selected items:")
        for item in self.tv.selection():
            item_text = self.tv.item(item, "text")
            print(item_text)
            self.selected_item = item_text
            print(item_text)
        return item_text

    def FunAdd(self):
        no = self.EntryNo.get()
        name = self.EntryName.get()
        m1 = self.EntryM1.get()
        m2 = self.EntryM2.get()
        m3 = self.EntryM3.get()
        if (
                self.EntryNo.get() == "" or self.EntryName.get() == "" or self.EntryM1.get() == "" or self.EntryM2.get() == "" or self.EntryM3.get() == ""):
            messagebox.showinfo(title="Add info", message='Please Insert Data !!!!!')
        else:
            s = int(m1) + int(m2) + int(m3)
            av = float("{0:.2f}".format(s * 1.05))
            self.sum.set(str(s))
            self.ave.set(str(av))
            self.db.execute("insert into stud1(no,name, m1,m2,m3,sum,ave) values (?, ? , ? , ? , ?, ? , ?)",
                            (no, name, m1, m2, m3, s, av))
            self.db.commit()
            messagebox.showinfo(title="Add info", message='added')
            self.FunShow()
            self.FunClear()

    # ==================tree.delete(*tree.get_children())=============================================================

    def FunClear(self):
        self.EntryName.delete(0, 'end')
        self.EntryNo.delete(0, 'end')
        self.EntryM1.delete(0, 'end')
        self.EntryM2.delete(0, 'end')
        self.EntryM3.delete(0, 'end')
        self.EntrySum.delete(0, 'end')
        self.sum.set('')
        self.EntryAve.delete(0, 'end')
        self.ave.set('')

    def FunShow(self):
        # x = self.tv.get_children()        for item in x:            self.tv.delete(item)

        self.tv.delete(*self.tv.get_children())

        cursor = self.db.execute("select * from stud1")
        for row in cursor:
            self.tv.insert('', 'end', '{}'.format(row['id']), text=row['id'])
            self.tv.set('{}'.format(row['id']), '#Number', row['no'])  # x=id  y=#number  data= from row[no]
            self.tv.set('{}'.format(row['id']), '#Name', row['name'])
            self.tv.set('{}'.format(row['id']), '#Chicken', row['m1'])
            self.tv.set('{}'.format(row['id']), '#Meat', row['m2'])
            self.tv.set('{}'.format(row['id']), '#Rice', row['m3'])
            self.tv.set('{}'.format(row['id']), '#Total', row['sum'])
            self.tv.set('{}'.format(row['id']), '#After VAT', row['ave'])

        item_count = len(self.tv.get_children())
        print('item_count=', item_count)

    # ===============================================================================
    def on_tree_select2(self, event):

        selected_item = self.tv.selection()[0]
        cursor = self.db.execute("select * from stud1 where id=?", (selected_item,))

        for row in cursor:
            self.no.set(str(row['no']))
            self.name.set(str(row['name']))
            self.m1.set(str(row['m1']))
            self.m2.set(str(row['m2']))
            self.m3.set(str(row['m3']))
            self.sum.set(str(row['sum']))
            self.ave.set(str(row['ave']))

        # ======================================================

    def FunUpdate(self):

        selected_item = self.tv.selection()[0]
        if (
                self.EntryName.get() == "" or self.EntryNo.get() == "" or self.EntryM1.get() == "" or self.EntryM2.get() == "" or self.EntryM3.get() == ""):
            messagebox.showinfo(title="Add info", message='Please Insert Data !!!!!')
        else:
            no = self.EntryNo.get()
            name = self.EntryName.get()
            m1 = self.EntryM1.get()
            m2 = self.EntryM2.get()
            m3 = self.EntryM3.get()

            s = int(m1) + int(m2) + int(m3)
            av = float(s * 1.05)
            self.sum.set(str(s))
            self.ave.set(str(av))
            selected_item = self.tv.selection()[0]

            id = selected_item
            print("id=====", selected_item)

            self.db.execute('Update stud1 set no=? ,name=?, m1=?, m2=?, m3=?,'
                            'sum=?, ave= ?  where id=?', (no, name, m1, m2, m3, s, av, id))
            self.db.commit()
            messagebox.showinfo(title="Add info", message='Data is Updated')
            self.FunShow()
            self.FunClear()

    # ===============================================================================

    def FunDel(self):

        conn = sqlite3.connect("Students.db")
        self.db.row_factory = sqlite3.Row
        selected_item = self.tv.selection()[0]
        print('selected_item', selected_item)  # it prints the selected row id
        cur = conn.cursor()
        cur.execute("DELETE FROM stud1 WHERE id=?", (selected_item,))
        conn.commit()

        self.tv.delete(selected_item)
        messagebox.showinfo(title="Add info", message='Record is deleted')
        self.FunShow()
        self.FunClear()

    # =========================================

    def delete(self):

        id = self.tv.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.db.execute("DELETE FROM stud1 where id=?", (id))
        self.db.commit
        print(" DEL id=====", self.selected_item)
        self.FunShow()
        messagebox.showinfo(title="Add info", message='Record is deleted')

    def remove_item(self):
        selected_item = self.treeview.selection()[0]
        self.treeview.delete(selected_item)
        print("id=====", id)

    def update(self):

        id = selected_item = self.tv.selection()[0]
        self.db.execute("update stud set no=?, name=?,m1=?, m2=?,m3=? where id==?", (selected_item,))
        self.db.commit
        # self.FunShow()
        print("id=====", selected_item)
        messagebox.showinfo(title="Add info", message='Record is deleted')
        self.db.commit()
        self.FunShow()


def main():
    restaurantProject()


# ==============================INITIALIATION==================================
if __name__ == '__main__':
    main()

