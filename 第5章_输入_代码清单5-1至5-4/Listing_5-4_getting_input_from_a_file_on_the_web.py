# Listing_5-4_getting_input_from_a_file_on_the_web.py
#代码清单5-4 从互联网上的一个文件中获取输入
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

import urllib.request
file = urllib.request.urlopen('http://helloworldbook3.com/data/message.txt')
message = file.read().decode('utf-8')
print(message)
