"""
This file contains a class defining a standard console logging interface
"""

#Global
import datetime
import sys

#Local

class Log:
    """This class defines functions to print formatted output to
    stdout or stderr with timestamps and identations for nested messages"""

    """
    Timestamp functions
    """

    def get_ts(self):
        """Returns the current time (in 24 hour format)"""
        return "["+str(datetime.datetime.now()).split()[1].split('.')[0]+"]"
    
    """
    Logging functions
    """

    def log(self, m, tabs=0):
        """Writes a normal log to stdout"""
        print(self.get_ts()+": "+'\t'*tabs+m)

    def warn(self, m, tabs=0):
        """Writes a warning message to stdout"""
        print(self.get_ts()+": "+'\t'*tabs+"===WARNING=== "+m)

    def error(self, m, tabs=0, die=True, code=1):
        """Writes an error message to stderr, calls sys.exit() if
        die is True
        TODO: Make this actually write to stderr"""
        sys.stderr.write(self.get_ts()+": "+'\t'*tabs+"===ERROR=== "+m+'\n')
        if die:
            print("\tExiting with code "+str(code)+"...")
            sys.exit(code)

if __name__ == "__main__":
    print("Log.py")
    l = Log()
    l.log("This is a routine message", tabs=0)
    l.log("This is a routine message in some subroutine", tabs=1)
    l.warn("This is a warning message in that subroutine", tabs=1)
    l.error("This is a nonfatal error in that subroutine", tabs=1, die=False)
    l.warn("This is a warning message", tabs=0)
    l.error("This is an error", die=False)
    l.error("This is a fatal error", die=True)
