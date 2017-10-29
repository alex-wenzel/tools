"""
A class that uses samtools commands to convert an input BAM/SAM
to fastq format (unaligned).  This is done with calls to samtools collate
to shuffle the reads in order to remove bias from previous alignments and
samtools fastq to perform the format conversion

Depends on samtools
"""

#Global
import subprocess

#Local

class Sam2Fastq:
    """Wrapper class around samtools commands to convert an input bam/sam
    file to fastq format"""
    def __init__(self, sampath, samtoolspath, outpath):
        """Takes an input sampath, the path to the samtools executable,
        and the output path and prepares to revert sampath to a fastq
        to save in outpath"""
        self.sampath = sampath
        self.samtoolspath = samtoolspath
        self.outpath = outpath
        self.collate_outpath = self.sampath.split('/')[-1].split('.')[0]+"_collated"

        self.collate()
        #self.fastq()
        #subprocess.call("rm "+self.collate_outpath, shell=True)
    
    """
    Collate wrapper
    """

    def collate(self):
        """Wrapper around the collate function"""
        cmd = self.samtoolspath+" collate -u --output-fmt SAM "
        cmd += self.sampath+" "+self.collate_outpath
        subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    print("sam2fastq.py")
