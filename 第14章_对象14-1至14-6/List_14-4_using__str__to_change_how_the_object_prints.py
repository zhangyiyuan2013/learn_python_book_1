# Copyright zhangyiyuan,2023
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    # Here's the `\\__str__()` method.
    def __str__(self):
        msg = "Hi, I'm a " + self.size + " " + self.color + "ball!"
        return msg
myBall = Ball("red", "small","down")
print(myBall)
