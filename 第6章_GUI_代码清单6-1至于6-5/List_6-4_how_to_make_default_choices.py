#创建默认选项
import easygui
flavor = easygui.enterbox("What is you favorite ice cream flavor?",default = 'Vanilla')  # Here's the default
easygui.msgbox("You entered " + flavor)
