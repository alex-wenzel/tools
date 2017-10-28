"""
This cell implements a Bed and BedLine representation.
"""

#Global

#Local
import tools.io.file_iterator as file_iterator

class Bed:
    """A class representing a bed format file"""
    def __init__(self, bedpath):
        """Loads all lines in bedpath into BedLine objects."""
        self.lines = []
        if bedpath != None:
            for line in file_iterator.iterate(open(bedpath)):
                self.lines.append(BedLine(line))

    def __iter__(self):
        for line in self.lines:
            yield(line)
        
class BedLine:
    """A class representing a single line of bed file data"""
    def __init__(self, bedline):
        """Loads a line of text or if None, populates an empty
        object representing a single line of bed data"""
        self.chromosome = None
        self.start = None
        self.end = None
        self.data = []
        
        if bedline != None:
            self.load(bedline)
            
    def load(self, bedline):
        """Takes the text of a single bed line and parses it
        into four fields - all optional data is represented as a list
        of strings - no conditions are imposed"""
        vals = bedline.strip('\n').split('\t')
        self.chromosome = vals[0]
        try:
            self.start = int(vals[1])
        except ValueError:
            raise ValueError("BedLine: expected start to be an integer, got "+vals[1])
        try:
            self.end = int(vals[2])
        except ValueError:
            raise ValueError("BedLine: expected end to be an integer "+vals[2])
        if self.end <= self.start:
            raise ValueError("BedLine: end ("+str(self.end)+") was greater than or equal to start ("+str(self.start)+")")
        if len(vals) > 3:
            self.data = vals[3:]
            
    def __str__(self):
        """String representation - convert back to bed"""
        return '\t'.join([self.chromosome, str(self.start), str(self.end)]+self.data)+'\n'
