# Listing_6-2_getting_input_using_a_choice_box.py
#使用选择框获得输入


import easygui
flavor = easygui.choicebox("What is your favorite ice cream flavor?",
                  choices = ['Vanilla', 'Chocolate', 'Strawberry'] )
easygui.msgbox("You picked " + flavor)
