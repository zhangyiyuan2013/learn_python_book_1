#使用选择框获取输入
import easygui
flavor = easygui.choicebox("What is you favorite ice cream flavor?",
                choices = ['Vanilla','Chocolate','Strawberry'] )
easygui.msgbox("You picked " + flavor)
