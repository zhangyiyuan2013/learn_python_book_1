# Listing_6-3_getting_input_using_an_enter_box.py
#使用输入框获得输入

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?")
easygui.msgbox("You entered " + flavor)
