#menu 
#for option 1
def read_aln_file(alnfile):
        aln=open(alnfile, "r")
        aln.seek(0,0)
        i=0
        for line in aln:
                i=i+1
                if i==1:
                        if line.startswith("CLUSTAL"):
                                print line
        
                elif line=="\n":
                        continue
                elif line!=" ":
                        print line
                else:
                        print "This may not be a valid CLUSTAL file."
                        
# for option 2
# for option 7 for exit
import sys
def exitapp():
        if confirm== "Y":
                print "Exiting"
                return 1
        if confirm=="N":
                return 0        



#make a loop to refresh menu
refresh=0
while refresh==0:
        
        deco="*"*77
        print deco
        print deco, "\n"
        print "* \t \t \t******Seq_Al_Analyser*******\t \t \t *"
        print "*      1) Open a Multiple Alignment File                                    *"
        print "*      2) Alignment Information                                             *"
        print "*      3) Alignment Explorer                                                *"
        print "*      4) Information per Sequence                                          *"
        print "*      5) Analysis of Glycosylation Signatures                              *"
        print "*      6) Export to Fasta                                                   *"
        print "*      7) Exit                                                              *"
        print "\n", deco
        print deco
        option=input("Please enter the number of chosen option ")
        if option==1:
                aln=raw_input("Enter path to aln file ")
                read_aln_file(aln)
                        
        
                
        elif option==7:
                confirm=raw_input("Are you sure you want to exit? Press Y to exit and N to continue ")
                refresh=exitapp()
                                
        else:
                print "Invalid option entered, enter one value from 1 to 7"
                


                                
                                
