"""
Converts the coordinates in a SAM/BAM file to a sorted and merged
bed file.  Depends on pysam
"""

#Global
import pysam

#Local
import tools.formats.Bed as Bed

class Sam2Bed:
    def __init__(self, sampath, isbam=False):
        """Takes an input sam/bam file and the location to the bedtools2
        scripts and constructs a bed file with the regions formed by the sam regions. Use isbam
        to specify if the file is binary or not
        Note: results are unsorted and unmerged.  Bedtools2 can be used to do both of these"""
        self.sampath = sampath
        self.isbam = isbam
        self.sam = None
        self.bed = None

        self.load_sam()
        self.convert()

    """
    Loading data
    """

    def load_sam(self):
        """Loads either a bam or sam file with pysam depending on the
        isbam input"""
        if self.isbam:
            self.sam = pysam.AlignmentFile(self.sampath, mode='rb')  #load with binary option
        else:
            self.sam = pysam.AlignmentFile(self.sampath, mode='r')  #load with ascii text option

    """
    Converting regions to tools.formats.Bed representation
    """
    
    def convert(self):
        """Builds a tools.formats.Bed object and populates it with new tools.formats.BedLine objects
        corresponding to each record from the sam file"""
        self.bed = Bed.Bed(None)
        for rec in self.sam.fetch():
            new_bedline = Bed.BedLine(None)
            new_bedline.chromosome = rec.reference_name
            if "chr" not in new_bedline.chromosome:
                new_bedline.chromosome = "chr"+new_bedline.chromosome
            new_bedline.start = rec.reference_start
            new_bedline.end = rec.reference_end
            self.bed.append(new_bedline)

    """
    Save the converted file
    """

    def save(self, outpath):
        open(outpath, 'w').write(str(self.bed))

if __name__ == "__main__":
    print("sam2bed.py")
    newbed = Sam2Bed("/home/alexw/ucsd/rotations/bansal/hpileup/data/input_reads_aligned.sam", isbam=False)
    newbed.save("test.bed")
