#menu 
#for option 1
def read_aln_file(alnfile):
        aln=open(alnfile, "r")
        aln.seek(0,0)
        if alnfile.endswith(".aln"):
                ext="correct"
        else:
                return 0
        alnseq=open(alnfile, "r").readlines()
        
        save=[]
        for line in alnseq:
                i=0
                if line.startswith("CLUSTAL") and i==0:
                        i=i+1
                        Clustal="present"
                        print line
                        return 0
                
                elif Clustal=="present" and (line.startswith("gi|") or line.startswith(" ")):
                        save=save+[line.strip()]
                        
                #print save
                
                else: 
                        Clustal="not present"
                        return 0
        
        aln.close()  
        
                        
# for option 2
# for option 3
# for option 4
# for option 5
# for option 6
# for option 7 for exit
import sys
def exitapp():
        if confirm== "Y" or confirm=="y":
                print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*Exiting*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
                return 1
        elif confirm=="N"or confirm=="n":
                return 0 
        else:
                print "Invalid option chosen, exiting anyways"
                return 1



#make a loop to refresh menu
refresh=0
barrier=0
ext=0
while refresh==0:
        
        deco="*"*77
        print deco
        print deco, "\n"
        print "******************************Seq_Al_Analyser********************************\n"
        print "*      1) Open a Multiple Alignment File                                    *"
        print "*      2) Alignment Information                                             *"
        print "*      3) Alignment Explorer                                                *"
        print "*      4) Information per Sequence                                          *"
        print "*      5) Analysis of Glycosylation Signatures                              *"
        print "*      6) Export to Fasta                                                   *"
        print "*      7) Exit                                                              *"
        print "\n", deco
        if ext=="correct" and barrier=="passed":
                print "Sequence has been loaded successfully "
        else:
                print "No sequence loaded "
        print deco
        option=input("Please enter the number of chosen option ")
        if option==1:
                aln=raw_input("Enter path to aln file ")
                read_aln_file(aln)
                refresh=read_aln_file(aln)       
                
        elif option==7:
                confirm=raw_input("Are you sure you want to exit? Press Y to exit and N to continue ")
                refresh=exitapp()                                
        else:
                print "Invalid option entered, enter one value from 1 to 7"
                
     

        


        