# Listing_6-1_getting_input_using_buttons.py
# 使用按钮获得输入


import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
                  choices = ['Vanilla', 'Chocolate', 'Strawberry'] )  # List of choices
easygui.msgbox("You picked " + flavor)
