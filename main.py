from tkinter import *
from PIL import Image, ImageTk

def image(filename, width, heigh):
    photo = Image.open(filename).resize((width, heigh))
    return ImageTk.PhotoImage(photo)

def BMI_check():
# 1.输入身高(cm)、体重(kg) ，转换为浮点类型数据
        height = float(text1.get())*0.01
        weight = float(text2.get())
# 2.计算BMI值 计算公式：BMI = 体重 / 身高^2
        BMI = round(weight / height ** 2, 1)
        text3.insert(INSERT, BMI)
# 3.判断BMI值对应的结果
        if BMI < 18.5:
                text4.insert(INSERT, '消瘦')
                text5.insert(INSERT, '您的体重消瘦，该增重了!\n'\
                                     '饮食调理:\n'\
                                     '    日常饮食中除选用含动物性蛋白质丰富的食物，如禽肉、畜肉、蛋 类、奶类、鱼类外，可适当多吃些豆制品、赤豆、薏苡仁、百合、蔬菜和瓜果等。')
        elif BMI <= 23.9:
                text4.insert(INSERT, '正常')
                text5.insert(INSERT, '您的体重正常，请继续保持!')
        elif BMI <= 27:
                text4.insert(INSERT, '超重')
                text5.insert(INSERT,'您的体重超重，需要适当减肥~\n'\
                                    '饮食调理:\n'\
                                    '   要少吃高热量高脂肪高蛋白食物,少喝饮料。少吃甜食。要锻练身体,要多运动。不能吃太饱太多。慢慢地运动加减食量。')
        elif BMI <= 32:
                text4.insert(INSERT, '肥胖')
                text5.insert(INSERT, '您的体重肥胖，请及时减肥~\n' \
                                     '饮食调理:\n'\
                                     '   在饮食上要做到合理的搭配，膳食的调整，营养要均衡。少吃一些油炸、油腻、辛辣、刺激性的食物，搭配含'\
                                     '膳食纤维比较高，维生素比较高的，新鲜的蔬菜和水果。选择少食多餐，每天要定时定量的做运动，能够保持良好的心态。')
        else:
                text4.insert(INSERT, '非常肥胖')
                text5.insert(INSERT, '您的体重非常肥胖，请及时减肥~')
        #生成主窗口
def delete():
        text1.delete(0, END)
        text2.delete(0, END)
        text3.delete('1.0', END)
        text4.delete('1.0', END)
        text5.delete('1.0', END)

root=Tk()
root.title('BMI测试')
root.geometry('400x600')

canvas = Canvas(root, width=400, height=600)
image1 = image('BMI_image1.png', 400, 600)
canvas.create_image(200, 300, image=image1)
canvas.pack()

label = Label(root, text='你的身体健康吗？')  # 生成标签
label.pack()
#第一个语言提示
label1 = Label(root, text='请输入你的身高(cm)：', font='Arial 10 bold', fg='#696969', bg='#b5dafa')
label1.place(relx=10/400, rely=40/600, relwidth=145/400, relheight=40/600)
#第一个文本框输入身高
text1 = Entry(root)
text1.place(relx=160/400, rely=40/600, relwidth=150/400, relheight=40/600)
#第二个语言提示
label2 = Label(root, text='请输入你的体重(kg)：', font='Arial 10 bold', fg='#696969', bg='#b5dafa')
label2.place(relx=10/400, rely=100/600, relwidth=130/400, relheight=40/600)
#第二个文本框输入身高
text2 = Entry(root)
text2.place(relx=160/400, rely=100/600, relwidth=150/400, relheight=40/600)
#第一个按钮
button = Button(root, text='确定', command=BMI_check)
button.place(relx=325/400, rely=70/600, relwidth=65/400, relheight=40/600)

#第三个语言提示
label3 = Label(root, text='您的BMI是：', font='Arial 10 bold', fg='#696969', bg='#d3d6ef')
label3.place(relx=20/400, rely=160/600, relwidth=80/400, relheight=35/600)
#第三个文本框输出BMI
text3 = Text(root)
text3.place(relx=110/400, rely=160/600, relwidth=40/400, relheight=30/600)

#第四个语言提示
label4 = Label(root, text='您的体重：', font='Arial 10 bold', fg='#696969', bg='#d3d6ef')
label4.place(relx=190/400, rely=160/600, relwidth=75/400, relheight=35/600)
#第四个文本框输出体重
text4 = Text(root)
text4.place(relx=275/400, rely=160/600, relwidth=40/400, relheight=30/600)

#第五个文本框输出建议
text5 = Text(root)
text5.place(relx=20/400, rely=200/600, relwidth=350/400, relheight=300/600)

#第二个按钮清空
button1 = Button(root, text='清空', command=delete)
button1.place(relx=30/400, rely=520/600, relwidth=80/400, relheight=40/600)

root.mainloop()

