class _Getch:

    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException

_getch = _Getch()

def get_input(timeout):
	import signal
	signal.signal(signal.SIGALRM, alarmHandler)
	signal.setitimer(signal.ITIMER_REAL, timeout, timeout)
	try:
		text = _getch()
		signal.alarm(0)	
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return ''
