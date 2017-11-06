# import tkinter
# from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import requests

# 1.添加多个账号，分不同的vip可以添加的账号有限制
# 2.浏览时间
# 3.添加收藏和购物车需要添加多个账号，不添加账号只是浏览，清楚cookie
# 4.云任务、本地任务


class Window:
    def __init__(self):
        master = Tk()
        master.title('全自动淘宝助shou')
        master.geometry('500x700+300+100')

        userframe= Frame(master, bd=1)

        userstatus = Label(userframe, text='未登录', bd=1)
        userstatus.grid(row=0, column=0)

        loginbtn = Button(userframe, text='登录', command=self.login_btn_click)
        loginbtn.grid(row=0, column=1)
        registerbtn = Button(userframe, text='注册', command=self.login_btn_click)
        registerbtn.grid(row=0, column=2)

        userframe.pack(side=TOP, fill=X)

        blank1 = Canvas(master, width=200, height=30, bg="white", bd=0)
        blank1.pack()

        img = ImageTk.PhotoImage(file='taobaologo.jpg')
        Label(master, text="abc", image=img).pack(side="top")
        # img = PhotoImage(file='taobaologo.jpg')

        frame2 = Frame(master)
        frame2.pack()
        Label(frame2, text='').grid(row=1, sticky=W)
        Label(frame2, text="搜索关键词:").grid(row=2, sticky=W)
        Label(frame2, text="掌柜名称:").grid(row=3, sticky=W)

        e1 = Entry(frame2)
        e2 = Entry(frame2)

        e1.grid(row=2, column=1)
        e2.grid(row=3, column=1)
        shoucangcheckBtn = Checkbutton(frame2, text='收藏')
        gouwuchecheckBtn = Checkbutton(frame2, text='购物车')
        shoucangcheckBtn.grid(row=4, column=1, sticky=W)
        gouwuchecheckBtn.grid(row=5, column=1, sticky=W)
        shoucangcheckBtn.config(state="disabled")
        gouwuchecheckBtn.config(state="disabled")
        daorubtn = Button(frame2, text='导入淘宝账号')
        daorubtn.grid(row=6, column=1, sticky=W)
        Label(frame2, text="已导入账号：0个").grid(row=7, column=1, sticky=W)

        line3 = Canvas(master, width=200, height=20, bg="white", bd=0)
        line3.pack()

        frame3 = Frame(master)
        frame3.pack()
        timesL = Label(frame3, text='次数:').grid(row=0, column=0)
        timesE = Entry(frame3, width=5).grid(row=0, column=1)
        liulantimeL = Label(frame3, text='浏览时间:').grid(row=1, column=0)
        liulantimeE = Entry(frame3, width=5).grid(row=1, column=1)

        yuncheckbtn = Checkbutton(master, text='云任务(高速云任务，云端自动执行，高速便捷)')
        yuncheckbtn.pack()

        self.surebtn = Button(master, text='启动', command=self.printstr)
        self.surebtn.config(bd=2, relief=RAISED)
        self.surebtn.config(bg='red', fg='white')
        # self.surebtn.grid(row=3, columnspan=2)
        self.surebtn.pack()
        line4 = Canvas(master, width=200, height=20, bg="white", bd=0)
        line4.pack()

        # frame4 = Frame(master)

        # loginbtn = Button(frame4, text='登录')
        # loginbtn.grid(row=0, column=1, sticky=E)

        # frame4.pack(side=BOTTOM)

        text = Text(master, bg='black', fg='yellow')
        text.insert(END, "初始化完成...")
        text.insert(END, "\n当前状态:未登录")
        # text.config(width=50)
        text.config(state="disabled")
        text.pack(side=BOTTOM, fill=X)

        master.mainloop()

    def printstr(self):
        self.surebtn.config(state="disabled")
        # if self.username.get():
        #     print(self.username.get())
        # else:
        #     print('222')
        # print(self.username.get())

    def login_btn_click(self):
        login_top = Toplevel()
        blank1 = Canvas(login_top, width=200, height=15, bg="white", bd=0)
        blank1.pack(fill=X, side=TOP)
        frame_login = Frame(login_top)
        frame_login.pack()
        Label(frame_login, text='会员登录').grid(row=0, columnspan=2)
        Label(frame_login, text="用户名:").grid(row=1, sticky=W)
        Label(frame_login, text="密码:").grid(row=3, sticky=W)
        e1 = Entry(frame_login)
        e2 = Entry(frame_login)
        e1.grid(row=2, column=0, sticky=W)
        e2.grid(row=4, column=0, sticky=W)
        Label(frame_login, text='请确认登录名和密码正确', fg='SlateGray').grid(row=5, column=0, sticky=W)

        jizhumimabtn = Checkbutton(frame_login, text='记住密码')
        autobtn = Checkbutton(frame_login, text='自动登录')
        jizhumimabtn.grid(row=6, column=0, sticky=W)
        autobtn.grid(row=7, column=0, sticky=W)

        login_btn = Button(frame_login, text='登录')
        login_btn.grid(row=8, column=0)

        blank3 = Canvas(login_top, width=200, height=30, bg="white", bd=0)
        blank3.pack(fill=X, side=BOTTOM)

Window()