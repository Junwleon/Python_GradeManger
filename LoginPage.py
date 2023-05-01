# -*- coding: utf-8 -*-
from tkinter import *  
from tkinter.messagebox import *  
from tkinter import messagebox
from MainPage import *  
#初始化一个登陆界面
class LoginPage(object):  
    def __init__(self, master=None):  
        self.root = master #定义内部变量root  
        self.root.geometry('%dx%d' % (500, 300)) #设置窗口大小
        self.username = StringVar()  
        self.password = StringVar()  
        self.createPage()  
 #创建一个窗口
    def createPage(self):
        self.page = Frame(self.root) #创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text = '用户名: ',font=('仿宋',9)).grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username ,bg='#AFEEEE').grid(row=1, column=1, stick=E)
        Label(self.page, text = '密码: ',font=('仿宋',9)).grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*',bg='#AFEEEE').grid(row=2, column=1, stick=E)
        Button(self.page,bg='#90EE90',fg='#000000', text='登陆',font=('宋体',12), command=self.loginCheck).grid(row=3, column=0, pady=5)
        Button(self.page,bg='#90EE90',fg='#000000', text='注册',font=('宋体',12), command=self.register).grid(row=3, column=1, pady=5)
        Button(self.page,bg='#90EE90',fg='#000000', text='退出',font=('宋体',12), command=self.page.quit).grid(row=3, column=2, pady=5)
        
  #登陆检查，是否文件中存在
    def loginCheck(self):  
        name = self.username.get()  
        password = self.password.get()
        if self.isLegalUser(name,password):
            self.page.destroy()
            MainPage(self.root)  
        else:  
            showinfo(title='错误', message='您输入的账号或密码错误！')
#用户名只能是字母和数字
    def isLegal(self,string):
        alp = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
#判定文件中是否有用户名和密码
    def isLegalUser(self,name,password):
        f = open('账号密码.csv','r',encoding='UTF-8',errors = 'ignore')#打开文件流
        for line in f.readlines():#一行一行的读取
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()==name and  info[1].strip()==password :
                 f.close()
                 return True
        return False

                
    def register(self):
        name = self.username.get()  
        password = self.password.get()
        if len(name)==0 or len(password)==0:
            showinfo(title='错误警告', message='账号、密码不能为空!')
            return
        for i in password:
            if i == ',' or i == ' ':
                showinfo(title='错误警告', message='密码不能含有非法字符!')
                return
        if self.isLegal(name):
            pass
        else:
            showinfo(title='错误警告', message='账号不能含有非法字符,请使用数字字母!')
            return
        
        f = open('账号密码.csv','r',encoding='UTF-8',errors = 'ignore')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<2:
                break
            if info[0].strip()==name:
                 messagebox.showinfo(title='结果', message ="该用户已注册过，请换一个用户名！")
                 f.close()
                 return
        f.close()
        
        f = open('账号密码.csv','a',encoding='UTF-8',errors = 'ignore')
        f.write('{},{}\n'.format(name,password))
        f.close()
        messagebox.showinfo(title='提示', message ="注册成功")
