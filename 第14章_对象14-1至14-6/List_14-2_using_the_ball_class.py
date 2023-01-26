# Copyright zhangyiyuan, 2023
# Released under MIT license  htt://opensource.org/licenses.php
# ------------

# Here's our class, same as before
class Ball:

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()  # Makes an instance of our class
# Sets some attributes
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"

# Prints the object's attributes
print("I just created a ball.")
print("My ball is", myBall.size)
print("My ball is", myBall.color)
print("My ball's direction is", myBall.direction)
print("Now I'm going to bounce the ball")
print()
myBall.bounce()  # Uses a method
print("Now the ball's direction is", myBall.direction)
