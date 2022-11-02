class DNAStrand:
    def __init__(self):
        self.dna = " "

    def isValidDNA(self,dna):
        """This functions returns statement Valid sequence if sequence is DNA and Invalid sequence if it's not"""
        base = ["A", "T", "C", "G"]
        for x in dna:
            if x not in base:
                return False

        return True

    def complementWC(self,dna):
        """Returns the Watson Crick complement, which is a string representing the complementary DNA strand"""
        valid_dna = self.isValidDNA(dna)
        if valid_dna:
            dna_complement = dna.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
            dna_complement = dna_complement.upper()
            return dna_complement
        else:
            return False

    def palindromeWC(self, dna):
        """Returns the Watson Crick Palindrome, which is the reversed sequence of the complement."""
        validDNA = self.isValidDNA(dna)
        if validDNA:
            dna_reverse = self.complementWC(dna)[::-1]
            return dna_reverse
        else:
            return False

    def containsSequence(self,dna,subseq):
        validDNA = self.isValidDNA(dna)
        if validDNA:
            if subseq in dna:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def summarise(dna):
        print("Original DNA Sequence: ",dna)
        if s.isValidDNA(dna):
            print("Is valid")
            print("Complement: ", s.complementWC(dna))
            print("WC Palindrome: ", s.palindromeWC(dna))
        else:
            print("Not Valid DNA")

s = DNAStrand()
seq1 = "AGCATTAGCTTACGCGGTGT"
subseq = "ATT"
s.summarise(seq1)



