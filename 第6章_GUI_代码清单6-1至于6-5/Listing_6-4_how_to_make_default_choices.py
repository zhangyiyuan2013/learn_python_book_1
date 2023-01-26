# Listing_6-4_how_to_make_default_choices.py
#创建默认选项


import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                           default = 'Vanilla')  # Here’s the default
easygui.msgbox("You entered " + flavor)
