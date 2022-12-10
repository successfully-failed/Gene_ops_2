import string

class Powerobject ():

    def __init__ (self):
        self.choice = ""
        self.string = ""
        self.reformed = ""
        self.prerep = ""
        self.replicated = ""
        self.transcripted = ""
        self.error = 0
        self.codons = []
        self.protein = []
        self.opt_a = ""
        self.opt_b = ""
        self.repl_out = ""
        self.transc_out = ""
        self.transl_out = ""
        self.temp1 = ""
        self.temp2 = ""

    def __del__ (self):
        del self.choice 
        del self.string 
        del self.reformed 
        del self.prerep 
        del self.replicated
        del self.transcripted
        del self.error 
        del self.codons 
        del self.protein 
        del self.opt_a 
        del self.opt_b
        del self.repl_out 
        del self.transc_out
        del self.transl_out
        del self.temp1
        del self.temp2

    def string (self):
        self.string = input("Please input gene code string to analyse")
        return self.string

    def check_string (self):
        for i in range (len(self.string)):
            if( self.string[i] == "a" or self.string[i] == "A"):
                self.reformed += "A"
            elif( self.string[i] == "t" or self.string[i] == "T"):
                self.reformed += "T"
            elif( self.string[i] == "c" or self.string[i] == "C"):
                self.reformed += "C"
            elif( self.string[i] == "g" or self.string[i] == "G"):
                self.reformed += "G"
            elif(self.string[i] == "U" or self.string[i] == "u"):
                self.reformed += "U"
            else:
                print("Error: wrong sequence")
                self.error = 1
                exit()
        return self.reformed

    def return_sequences (self):
        return self.reformed


    def replication (self):
        for i in range (len(self.reformed)):
            if( self.reformed[i] == "A"):
                self.replicated  += "T"
            elif( self.reformed[i] == "T"):
                self.replicated += "A"
            elif( self.reformed[i] == "C"):
                self.replicated += "G"
            elif( self.reformed[i] == "G"):
                self.replicated += "C"
            else:
                self.error = 1
                exit()
        return self.replicated

    def transcription (self):
        for i in range (len(self.reformed)):
            if( self.reformed[i] == "A"):
                self.transcripted += "U"
            elif( self.reformed[i] == "T"):
                self.transcripted += "A"
            elif( self.reformed [i] == "C"):
                self.transcripted += "G"
            elif( self.reformed[i] == "G"):
                self.transcripted += "C"
            else:
                self.error = "Ooops, this string propably isn't DNA"
                return self.error
                exit()
        return self.transcripted





    def find_codons (self):
        self.reformed = "$"+self.reformed
        for i in range (len(self.reformed)):
                if(i == 1):
                    self.codons.append (self.reformed[i] + self.reformed[i + 1] + self.reformed[i + 2])
                elif(i > 3 and i%3 == 0):
                    self.codons.append (self.reformed[i - 2] + self.reformed[i - 1] + self.reformed[i])
        self.reformed = self.reformed.removeprefix('$')
        return self.codons


    def return_codons (self):
        return self.codons


    def translator (self):
        for i in range (len(self.codons)):
            if(self.codons[i] == "AUG"):
                self.protein.append("Met")
            elif(self.codons[i] == "UUU" or self.codons[i] == "UUC"):
                self.protein.append ("Phe")
            elif(self.codons[i] == "UUA" or self.codons[i] == "UUG" or self.codons[i] == "CUU" or self.codons[i] == "CUC" or self.codons[i] == "CUA" or self.codons[i] == "CUG"):
                self.protein.append("Leu")
            elif(self.codons[i] == "AUU" or self.codons[i] == "AUC" or self.codons[i] == "AUA"):
                self.protein.append("Ile")
            elif(self.codons[i] == "GUU" or self.codons[i] == "GUC" or self.codons[i] == "GUA" or self.codons[i] == "GUG"):
                self.protein.append ("Val")
            elif(self.codons[i] == "UCU" or self.codons[i] == "UCC" or self.codons[i] == "UCA" or self.codons[i] == "UCG"):
                self.protein.append("Ser")
            elif(self.codons[i] == "CCU" or self.codons[i] == "CCC" or self.codons[i] == "CCA" or self.codons[i] == "CCG"):
                self.protein.append("Pro")
            elif(self.codons[i] == "ACU" or self.codons[i] == "ACC" or self.codons[i] == "ACA" or self.codons[i] == "ACG"):
                self.protein.append("Thr")
            elif(self.codons[i] == "GCU" or self.codons[i] == "GCC" or self.codons[i] == "GCA" or self.codons[i] == "GCG"):
                self.protein.append("Ala")
            elif(self.codons[i] == "UAU" or self.codons[i] == "UAC"):
                self.protein.append("Tyr")
            elif(self.codons[i] == "UAA" or self.codons[i] == "UAG"):
                self.protein.append("STOP")
            elif(self.codons[i] == "CAU" or self.codons[i] == "CAC"):
                self.protein.append("His")
            elif(self.codons[i] == "CAA" or self.codons[i] == "CAG"):
                self.protein.append("Gln")
            elif(self.codons[i] == "AAU" or self.codons[i] == "AAC"):
                self.protein.append("Asn")
            elif(self.codons[i] == "AAA" or self.codons[i] == "AAG"):
                self.protein.append("Lys")
            elif(self.codons[i] == "GAU" or self.codons[i] == "GAC"):
                self.protein.append("Asp")
            elif(self.codons[i] == "GAA" or self.codons[i] == "GAG"):
                self.protein.append("Glu")
            elif(self.codons[i] == "UGU" or self.codons[i] == "UGC"):
                self.protein.append("Cys")
            elif(self.codons[i] == "UGG"):
                self.protein.append("Trp")
            elif(self.codons[i] == "CGU" or self.codons[i] == "CGC" or self.codons[i] == "CGA" or self.codons[i] == "CGG"):
                self.protein.append("Arg")
            elif(self.codons[i] == "GGU" or self.codons[i] == "GGC" or self.codons[i] == "GGA" or self.codons[i] == "GGG"):
                self.protein.append("Gly")
            else:
                self.protein.append("-RRR-")

        return self.protein



    def refresh (self):
        self.choice = ""
        self.string = ""
        self.reformed = ""
        self.prerep = ""
        self.replicated = ""
        self.transcripted = ""
        self.error = 0
        self.codons = []
        self.protein = []
        self.opt_a = ""
        self.opt_b = ""
        self.repl_out = ""
        self.transc_out = ""
        self.transl_out = ""
        self.temp1 = ""
        self.temp2 = ""


    def do_all_replication (self):
        if(self.error == 1):
            self.repl_out = "Error somenthing went wrong, try again"
            return self.repl_out
            exit()
        if(self.choice == "1"):
            self.string()
        self.check_string()
        if(self.opt_a == "1"):
            self.return_sequences()
            self.repl_out += (self.reformed)
        self.replication()
        self.repl_out += ("\n\n")
        self.repl_out += (self.replicated)
    

    def do_all_transcription (self):
        if(self.error == 1):
            self.transc_out = "Error somenthing went wrong, try again"
            return self.transc_out
            exit()
        if(self.choice == "1"):
            self.string()
        self.check_string()
        if(self.opt_a =="1"):
            self.return_sequences()
            self.transc_out += (self.reformed)
        self.transcription()
        self.transc_out += ("\n\n")
        self.transc_out +=(self.transcripted)

    def do_all_translation (self):
        #if(self.error == 1):
         #   self.transl_out = "Error somenthing went wrong, try again"
          #  return self.trans_out
           # exit()
        if(self.choice == "1"):
            self.string()
        self.check_string()
        if(self.opt_a == "1"):
            self.return_sequences()
            self.transl_out += (self.string)
        self.find_codons()
        if(self.opt_b == "1"):
            self.temp1 = self.temp1.join(self.codons)
            self.transl_out += ("\n\n")
            self.transl_out += self.temp1
        self.translator()
        self.temp2 = self.temp2.join(self.protein)
        self.transl_out += ("\n\n")
        self.transl_out += self.temp2
    


