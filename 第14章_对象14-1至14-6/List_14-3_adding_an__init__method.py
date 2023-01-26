# Copyright zhangyiyuan, 2023
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

class Ball:
    # Here's the `\\__init__()` method: 2 underscores on either side of _init_. Total of 4 underscores, 2 on either side
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball("red", "small", "down")  # Attributes are passed in as arguments to `\\__init__().
print("I just created a ball.")

print("My ball is", myBall.size)
print("My ball's direction is ", myBall.direction)
print("Now I'm going to bounce the ball")
print()
myBall.bounce()
print("Now the ball's direction is", myBall.direction)

