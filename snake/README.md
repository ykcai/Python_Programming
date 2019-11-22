# Snake in Tkinter

In this part of the Tkinter tutorial, we create a Snake game clone.

Snake is an older classic video game. It was first created in late 70s. Later it was brought to PCs. In this game the player controls a snake. The objective is to eat as many apples as possible. Each time the snake eats an apple, its body grows. The snake must avoid the walls and its own body.

## Development

The size of each of the joints of a snake is 10 px. The snake is controlled with the cursor keys. Initially, the snake has three joints. The game starts immediately. When the game is finished, we display game over message with the score in the center of the window.

We use the Canvas widget to create the game. The objects in the game are images. We use canvas methods to create image items. We use canvas methods to find items on the canvas using tags and to do collision detection.

```python
snake.py
#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

This is a simple Snake game
clone.

Author: Jan Bodnar
Website: zetcode.com
Last edited: April 2019
"""

import sys
import random
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW

class Cons:

    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27

class Board(Canvas):

    def __init__(self):
        super().__init__(width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT,
            background="black", highlightthickness=0)

        self.initGame()
        self.pack()


    def initGame(self):
        '''initializes game'''

        self.inGame = True
        self.dots = 3
        self.score = 0

        # variables used to move snake object
        self.moveX = Cons.DOT_SIZE
        self.moveY = 0

        # starting apple coordinates
        self.appleX = 100
        self.appleY = 190

        self.loadImages()

        self.createObjects()
        self.locateApple()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)


    def loadImages(self):
        '''loads images from the disk'''

        try:
            self.idot = Image.open("dot.png")
            self.dot = ImageTk.PhotoImage(self.idot)
            self.ihead = Image.open("head.png")
            self.head = ImageTk.PhotoImage(self.ihead)
            self.iapple = Image.open("apple.png")
            self.apple = ImageTk.PhotoImage(self.iapple)

        except IOError as e:

            print(e)
            sys.exit(1)


    def createObjects(self):
        '''creates objects on Canvas'''

        self.create_text(30, 10, text="Score: {0}".format(self.score),
                         tag="score", fill="white")
        self.create_image(self.appleX, self.appleY, image=self.apple,
            anchor=NW, tag="apple")
        self.create_image(50, 50, image=self.head, anchor=NW,  tag="head")
        self.create_image(30, 50, image=self.dot, anchor=NW, tag="dot")
        self.create_image(40, 50, image=self.dot, anchor=NW, tag="dot")


    def checkAppleCollision(self):
        '''checks if the head of snake collides with apple'''

        apple = self.find_withtag("apple")
        head = self.find_withtag("head")

        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for ovr in overlap:

            if apple[0] == ovr:

                self.score += 1
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.dot, anchor=NW, tag="dot")
                self.locateApple()


    def moveSnake(self):
        '''moves the Snake object'''

        dots = self.find_withtag("dot")
        head = self.find_withtag("head")

        items = dots + head

        z = 0
        while z < len(items)-1:

            c1 = self.coords(items[z])
            c2 = self.coords(items[z+1])
            self.move(items[z], c2[0]-c1[0], c2[1]-c1[1])
            z += 1

        self.move(head, self.moveX, self.moveY)


    def checkCollisions(self):
        '''checks for collisions'''

        dots = self.find_withtag("dot")
        head = self.find_withtag("head")

        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for dot in dots:
            for over in overlap:
                if over == dot:
                  self.inGame = False

        if x1 < 0:
            self.inGame = False

        if x1 > Cons.BOARD_WIDTH - Cons.DOT_SIZE:
            self.inGame = False

        if y1 < 0:
            self.inGame = False

        if y1 > Cons.BOARD_HEIGHT - Cons.DOT_SIZE:
            self.inGame = False


    def locateApple(self):
        '''places the apple object on Canvas'''

        apple = self.find_withtag("apple")
        self.delete(apple[0])

        r = random.randint(0, Cons.MAX_RAND_POS)
        self.appleX = r * Cons.DOT_SIZE
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.appleY = r * Cons.DOT_SIZE

        self.create_image(self.appleX, self.appleY, anchor=NW,
            image=self.apple, tag="apple")


    def onKeyPressed(self, e):
        '''controls direction variables with cursor keys'''

        key = e.keysym

        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY and self.moveX <= 0:

            self.moveX = -Cons.DOT_SIZE
            self.moveY = 0

        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY and self.moveX >= 0:

            self.moveX = Cons.DOT_SIZE
            self.moveY = 0

        RIGHT_CURSOR_KEY = "Up"
        if key == RIGHT_CURSOR_KEY and self.moveY <= 0:

            self.moveX = 0
            self.moveY = -Cons.DOT_SIZE

        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY and self.moveY >= 0:

            self.moveX = 0
            self.moveY = Cons.DOT_SIZE


    def onTimer(self):
        '''creates a game cycle each timer event'''

        self.drawScore()
        self.checkCollisions()

        if self.inGame:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()


    def drawScore(self):
        '''draws score'''

        score = self.find_withtag("score")
        self.itemconfigure(score, text="Score: {0}".format(self.score))


    def gameOver(self):
        '''deletes all objects and draws game over message'''

        self.delete(ALL)
        self.create_text(self.winfo_width() /2, self.winfo_height()/2,
            text="Game Over with score {0}".format(self.score), fill="white")


class Snake(Frame):

    def __init__(self):
        super().__init__()

        self.master.title('Snake')
        self.board = Board()
        self.pack()


def main():

    root = Tk()
    nib = Snake()
    root.mainloop()


if __name__ == '__main__':
    main()
```

####First we will define some constants used in our game.

```python
class Cons:

    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27
```

The BOARD_WIDTH and BOARD_HEIGHT constants determine the size of the Board. The DELAY constant determines the speed of the game. The DOT_SIZE is the size of the apple and the dot of the snake. The MAX_RAND_POS constant is used to calculate a random position of an apple.

The initGame() method initialises variables, loads images, and starts a timeout function.

```
self.createObjects()
self.locateApple()
```

The createObjects() method creates items on the canvas. The locateApple() puts an apple randomly on the canvas.

```python
self.bind_all("<Key>", self.onKeyPressed)
```

We bind the keyboard events to the onKeyPressed() method. The game is controlled with keyboard cursor keys.

```python
try:
self.idot = Image.open("dot.png")
self.dot = ImageTk.PhotoImage(self.idot)
self.ihead = Image.open("head.png")
self.head = ImageTk.PhotoImage(self.ihead)
self.iapple = Image.open("apple.png")
self.apple = ImageTk.PhotoImage(self.iapple)

except IOError as e:

    print(e)
    sys.exit(1)
```

In these lines, we load our images. There are three images in the Snake game: the head, the dot, and the apple.

```python
def createObjects(self):
'''creates objects on Canvas'''

    self.create_text(30, 10, text="Score: {0}".format(self.score),
                        tag="score", fill="white")
    self.create_image(self.appleX, self.appleY, image=self.apple,
        anchor=NW, tag="apple")
    self.create_image(50, 50, image=self.head, anchor=NW,  tag="head")
    self.create_image(30, 50, image=self.dot, anchor=NW, tag="dot")
    self.create_image(40, 50, image=self.dot, anchor=NW, tag="dot")
```

In the createObjects() method, we create game objects on the canvas. These are canvas items. They are given initial x and y coordinates. The image parameter provides the image to be displayed. The anchor parameter is set to NW; this way the coordinates of the canvas item are the top-left points of the items. This is important if we want to be able to display images next to the borders of the root window. Try to delete the anchor and see what happens. The tag parameter is used to identify items on the canvas. One tag may be used for multiple canvas items.

The checkAppleCollision() method checks if the snake has hit the apple object. If so, we increase score, add another snake joint and call the locateApple().

```python
apple = self.find_withtag("apple")
head = self.find_withtag("head")
```

The find_withtag() method finds an item on the canvas using its tag. We need two items: the head of the snake and the apple. Note that even if there is only one item with a given tag, the method returns a tuple. This is a case for the apple item. And later the apple item is accessed the following way: apple[0].

```python
x1, y1, x2, y2 = self.bbox(head)
overlap = self.find_overlapping(x1, y1, x2, y2)
```

The bbox() method returns the bounding box points of an item. The find_overlapping() method finds colliding items for the given coordinates.

```python
for ovr in overlap:

    if apple[0] == ovr:
        x, y = self.coords(apple)
        self.create_image(x, y, image=self.dot, anchor=NW, tag="dot")
        self.locateApple()
```

If the apple collides with the head, we create a new dot item at the coordinates of the apple object. We call the locateApple() method, which deletes the old apple item from the canvas and creates and randomly positions a new one.

In the moveSnake() method we have the key algorithm of the game. To understand it, look at how the snake is moving. We control the head of the snake. We can change its direction with the cursor keys. The rest of the joints move one position up the chain. The second joint moves where the first was, the third joint where the second was etc.

```python
z = 0
while z < len(items)-1:
c1 = self.coords(items[z])
c2 = self.coords(items[z+1])
self.move(items[z], c2[0]-c1[0], c2[1]-c1[1])
z += 1
```

This code moves the joints up the chain.

```python
self.move(head, self.moveX, self.moveY)
```

We move the head with the move() method. The self.moveX and self.moveY variables are set when the cursor keys are pressed.

In the checkCollisions() method, we determine if the snake has hit itself or one of the walls.

```python
x1, y1, x2, y2 = self.bbox(head)
overlap = self.find_overlapping(x1, y1, x2, y2)

for dot in dots:
for over in overlap:
if over == dot:
self.inGame = False
```

We finish the game if the snake hits one of its joints with the head.

```python
if y1 > Cons.BOARD_HEIGHT - Cons.DOT_SIZE:
self.inGame = False
```

We finish the game if the snake hits the bottom of the Board.

The locateApple() method locates a new apple randomly on the board and deletes the old one.

```python
apple = self.find_withtag("apple")
self.delete(apple[0])
```

Here we find and delete the apple that was eaten by the snake.

```python
r = random.randint(0, Cons.MAX_RAND_POS)
```

We get a random number from 0 to MAX_RAND_POS - 1.

```python
self.appleX = r _ Cons.DOT_SIZE
...
self.appleY = r _ Cons.DOT_SIZE
```

These lines set the x and y coordinates of the apple object.

In the onKeyPressed() method we react to the pressed keys during the game.

```python
LEFT_CURSOR_KEY = "Left"
if key == LEFT_CURSOR_KEY and self.moveX <= 0:

    self.moveX = -Cons.DOT_SIZE
    self.moveY = 0
```

If we hit the left cursor key, we set the self.moveX and self.moveY variables accordingly. These variables are used in the moveSnake() method to change coordinates of the snake object. Notice also that when the snake is heading to the right, we cannot turn immediately to the left.

```python
def onTimer(self):
'''creates a game cycle each timer event '''

    self.drawScore()
    self.checkCollisions()

    if self.inGame:
        self.checkAppleCollision()
        self.moveSnake()
        self.after(Cons.DELAY, self.onTimer)
    else:
        self.gameOver()
```

Every DELAY ms, the onTimer() method is called. If we are in the game, we call three methods that build the logic of the game. Otherwise the game is finished. The timer is based on the after() method, which calls a method after DELAY ms only once. To repeatedly call the timer, we recursively call the onTimer() method.

```python
def drawScore(self):
'''draws score'''

    score = self.find_withtag("score")
    self.itemconfigure(score, text="Score: {0}".format(self.score))
```

The drawScore() method draws score on the board.

```python
def gameOver(self):
'''deletes all objects and draws game over message'''

    self.delete(ALL)
    self.create_text(self.winfo_width() /2, self.winfo_height()/2,
        text="Game Over with score {0}".format(self.score), fill="white")
```

If the game is over, we delete all items on the canvas. Then we draw game over with the final score in the center of the screen.
