# -*- coding: utf-8 -*-
from tkinter import *
from LoginPage import *
root = Tk()
canvas = Canvas(root ,height = 90,width =300)
img_gif = PhotoImage(file = 'welcome1.gif')
image = canvas.create_image(0,0,anchor = 'nw',image = img_gif)
canvas.pack(side = 'top')
root.title('学生成绩管理系统by LinQiaojun ')
LoginPage(root)  
root.mainloop()  
