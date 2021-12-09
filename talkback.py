import tkinter
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import os

def comfortinput1():
    input1.insert(END, "···")

def comfortinput2():
    input2.insert(END, "?!")

def printest():
    #root.wm_attributes('-transparentcolor', root['bg'])
    imglabel = Label(root, image=talkback)
    imglabel.place(x=0,y=0)
    textoutput1 = Label(root, text=input1.get(), font=("./나눔고딕BOLD.TTF", 40), bg='white')
    textoutput1.place(x=100, y=70)
    textoutput2 = Label(root, text=input2.get(),font=("./나눔고딕BOLD.TTF", 40), bg='white')
    textoutput2.place(x=100, y=465)

def save():
    img = Image.open("template.png")
    write = ImageDraw.Draw(img)
    font = ImageFont.truetype("./나눔고딕BOLD.TTF", 50)
    write.text((120, 70), input1.get(), font=font, fill="black")
    write.text((120, 465), input2.get(), font=font, fill="black")

    for i in range(0, 99999999):
        if os.path.exists("./말대꾸{}.png".format(i)):
            i=i+1
        else:
            img.save("./말대꾸{}.png".format(i), 'PNG')
            break


root = Tk()


root.title("말대꾸 제작기")
root.geometry("425x675+500+50")
root.resizable(False, False)

talkback = PhotoImage(file="template.png")
imglabel = Label(root, image=talkback)
imglabel.place(x=0,y=0)


textlabel1 = Label(root, text="첫번째 대사 : ")
textlabel1.place(x=0, y=610)
textlabel2 = Label(root, text="두번째 대사 : ")
textlabel2.place(x=0, y=640)

input1=Entry(root)
input1.place(x=80, y=610)
input2=Entry(root)
input2.insert(0, "말대꾸?!")
input2.place(x=80, y=640)


btn0 = Button(root, width=6, height=3, text="미리보기", command=printest)
btn0.place(x=315, y=610)

btn1 = Button(root, width=6, height=3, text="저장", command=save)
btn1.place(x=370, y=610)

btn2 = Button(root, width=3, height=1, text="…", command=comfortinput1)
btn2.place(x=282, y=610)

btn3 = Button(root, width=3, height=1, text="?!", command=comfortinput2)
btn3.place(x=282, y=640)

root.mainloop()