import sys
import threading
from .spinners import bar_counter_clockwise


class Spinner(object):
    def __init__(self, beep=False, disable=False, force=False, stream=sys.stdout, spinner=bar_counter_clockwise, delay=0.25):
        self.spinner = spinner
        self.disable = disable
        self.beep = beep
        self.force = force
        self.stream = stream
        self.stop_running = None
        self.spin_thread = None
        self.delay = delay
        self.tty_output = self.stream.isatty() or self.force

    def start(self):
        if self.disable:
            return
        if self.tty_output:
            self.stop_running = threading.Event()
            self.spin_thread = threading.Thread(target=self.init_spin)
            self.spin_thread.start()

    def stop(self):
        if self.spin_thread:
            self.stop_running.set()
            self.spin_thread.join()

    def init_spin(self):
        while not self.stop_running.is_set():
            self.stream.write(next(self.spinner))
            self.stream.flush()
            self.stop_running.wait(self.delay)
            self.stream.write('\b')
            self.stream.flush()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.disable:
            return False
        self.stop()
        if self.tty_output:
            if self.beep:
                self.stream.write('\7')
                self.stream.flush()
            self.stream.write(' \b')
            self.stream.flush()
        return False


def spinner(beep=False, disable=False, force=False, stream=sys.stdout, spinner=bar_counter_clockwise, delay=0.25):
    """This function creates a context manager that is used to display a
    spinner on stdout as long as the context has not exited.

    The spinner is created only if stdout is not redirected, or if the spinner
    is forced using the `force` parameter.

    Parameters
    ----------
    beep : bool
        Beep when spinner finishes.
    disable : bool
        Hide spinner.
    force : bool
        Force creation of spinner even when stdout is redirected.
    stream : IO
        Stream to write the spinner to.
    spinner : cycle[str]
        Spinner animation to display.
    delay : float
        Delay, in seconds, between spinner frames.

    Example
    -------

        with spinner():
            do_something()
            do_something_else()

    """
    return Spinner(beep, disable, force, stream, spinner, delay)


from . import _version
__version__ = _version.get_versions()['version']
