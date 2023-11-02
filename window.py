from tkinter import Tk, BOTH, Canvas
from pre import DEBUG_MODE, Debug
debug = Debug()

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas()
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def close(self):
        self.__running = False

    def wait_for_close(self):
        self.__running = True
        while(self.__running): self.redraw()
        if (debug.mode): debug.print_debug("self.__running = " + str(self.__running))
