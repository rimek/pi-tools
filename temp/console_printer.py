
import cusrses

class ConsolePrinter(object):
    def __init__(self):
        self.window = curses.initscr()

    def print(self, data):
        window.clear()

        window.addstr("{:<8} {:<15} \n".format('Room','Temperature'))
        for k,v in data.iteritems():
            window.addstr("{:<8} {:<15} \n".format(k, v))

        window.refresh()

    def end(self):
        curses.endwin()
