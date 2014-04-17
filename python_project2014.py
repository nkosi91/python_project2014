#menu 
#for option 1
def read_aln_file(alnfile):
        aln=open(alnfile, "r")
        aln.seek(0,0)
        for line in aln:
                if line.startswith("CLUSTAL"):
                        print line

#make a loop to refresh menu
refresh=0

while refresh==0:
        deco="*"*77
        print deco
        print deco, "\n"
        print "* \t \t \t \t****Seq_Al_Analyser****\t \t \t *"
        option1="*      1) Open a Multiple Alignment File                                    *"
        print option1
        option2="*      2) Alignment Information                                             *"
        print option2
        option3="*      3) Alignment Explorer                                                *"
        print option3
        option4="*      4) Information per Sequence                                          *"
        print option4
        option5="*      5) Analysis of Glycosylation Signatures                              *"
        print option5
        option6="*      6) Export to Fasta                                                   *"
        print option6
        option7="*      7) Exit                                                              *"
        print option7
        print "\n", deco
        print deco
        option=input("Please enter chosen option ")
        if option==1:
                aln=raw_input("Enter path to aln file ")
                read_aln_file(aln)
               
                refresh=0
        elif option==2:
                print "option not entered or option invalid"
                menu(option)
                
                refresh=0
        elif option==3:
                
                refresh=0     
        elif option==4:
                
                
                refresh=0       
        elif option==5:
                
                refresh=0
        elif option==6:
                
                refresh=0
        
        elif option==7:
                exit()

        else:
                print "Invalid option entered, enter one value from 1 to 7"
        

