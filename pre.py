import os

DEBUG_MODE = True
LEN = len(str(os.getcwd()))
LEN2 = lambda y: len(str(y))
PRINT_FILE = lambda x: x[LEN:LEN2(x)]

class Debug:
    mode = DEBUG_MODE
    def print_debug(self, file, line, msg):
        if (self.mode): print(f"DEBUG: {PRINT_FILE(file)} {line} {msg}")