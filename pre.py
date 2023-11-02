DEBUG_MODE = True

class Debug:
    mode = DEBUG_MODE
    def print_debug(self, msg):
        if (self.mode): print("DEBUG: " + msg)