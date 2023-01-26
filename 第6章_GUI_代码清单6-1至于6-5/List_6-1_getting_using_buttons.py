#使用按钮获得输入
import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?", choices = ['Vanilla','Chocolate','Strawberry'])  #List is choice
easygui.msgbox("You picked " + flavor)
