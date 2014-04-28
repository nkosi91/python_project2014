#for option 1
def read_aln_file(alnfile):
        aln=open(alnfile, "r")
        aln.seek(0,0)
        if alnfile.endswith(".aln"):
                lines=aln.readlines()
                aln.close()
        if lines[0].startswith("CLUSTAL"):
                header=lines[0]
                print header
                seq=[]
                for line in lines:
                        if line.startswith("CLUSTAL"):
                                continue
                        else:
                                nline=line.strip()
                                seq=seq+[nline]                               
                print seq                
                store=[]
                for item in seq:
                        if item=="":
                                continue
                        else:
                                store=store+[item]
                print "store==", store
                seqids=[]
                for seqid in store:                                        
                        if seqid.startswith("gi|"):
                                seqids=seqids+[seqid]               
                print "seqids==", seqids
                indices=[]
                for Seqid in seqids:
                        ind=Seqid.index(" ")
                        indices=indices+[ind]
                print "indices==", ind
                        #if line.startswith("gi|") or line.startswith(" "):
                                
                                #return 0  
                
        else:           
                message="File might not be a valid fasta file, please enter a valid aln file"
                return 0
#for option 2
#def summary():
        
        
        
        
#for option 7
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
#menu
while refresh==0:        
        deco="*"*77
        print deco
        print deco, "\n"
        print "*"*30, "Seq_Al_Analyser", "*"*30,"\n"
        print "*      1) Open a Multiple Alignment File                                    *"
        print "*      2) Alignment Information                                             *"
        print "*      3) Alignment Explorer                                                *"
        print "*      4) Information per Sequence                                          *"
        print "*      5) Analysis of Glycosylation Signatures                              *"
        print "*      6) Export to Fasta                                                   *"
        print "*      7) Exit                                                              *"
        print "\n", deco
        message="No sequence loaded into memory"
        print message
        print deco
        option=input("Please enter the number of chosen option ")
        if option==1:
                aln=raw_input("Enter path to aln file ")
                refresh=read_aln_file(aln)
        elif option==2:
                refresh=summary()
        elif option==3:
                startslice=input("Enter start position ")
                endslice=input("Enter end position ")
                refresh=slicer()
        elif option==4:
                sequenceid=raw_input("Please enter sequence to analyse ")
                refresh=seqisolate()
        elif option==5:
                refresh=glycosig()
        elif option==6:
                refresh=fastaexport()
        elif option==7:
                confirm=raw_input("Are you sure you want to exit? Press Y to exit and N to continue ")
                refresh=exitapp()                                
        else:
                print "Invalid option entered, enter one value from 1 to 7"