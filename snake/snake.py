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
        '''Initializes Snake Game'''
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
        '''Loads Images from the Disk'''

        try:
            self.idot = Image.open(
                "/Users/michaelcai/Desktop/Personal/Python_Programming/snake/dot.png")
            self.dot = ImageTk.PhotoImage(self.idot)
            self.ihead = Image.open(
                "/Users/michaelcai/Desktop/Personal/Python_Programming/snake/head.png")
            self.head = ImageTk.PhotoImage(self.ihead)
            self.iapple = Image.open(
                "/Users/michaelcai/Desktop/Personal/Python_Programming/snake/apple.png")
            self.apple = ImageTk.PhotoImage(self.iapple)
        except IOError as e:
            print(e)
            sys.exit(1)

    def createObjects(self):
        '''Creates Objects on Canvas'''
        self.create_text(30, 10, text="Score: {0}".format(
            self.score), tag="score", fill="white")

        self.create_image(self.appleX, self.appleY,
                          image=self.apple, anchor=NW, tag="apple")

        self.create_image(50, 50, image=self.head, anchor=NW, tag="head")
        self.create_image(30, 50, image=self.dot, anchor=NW, tag="dot")
        self.create_image(40, 50, image=self.dot, anchor=NW, tag="dot")

    def checkAppleCollision(self):
        '''Checks if the Head of the snake collides with apple'''
        apple = self.find_withtag("apple")
        head = self.find_withtag("head")

        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
