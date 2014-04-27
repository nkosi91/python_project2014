#for option 1
def read_aln_file(alnfile):
        aln=open(alnfile, "r")#opening the aln file
        aln.seek(0,0)
        if alnfile.endswith(".aln"):#checking if extension is correst
                lines=aln.readlines()
                aln.close()
        if lines[0].startswith("CLUSTAL"):#checking if it is a valid clustal file
                header=lines[0]
                print header
                seq=[]#making a list of everything found in the document
                for line in lines:
                        if line.startswith("CLUSTAL"):#excluding the header in the list
                                continue
                        else:
                                nline=line.strip()#removing "next lines" in the list
                                seq=seq+[nline]                               
                print seq                
                store=[]
                for item in seq:
                        if item=="":#removing the spaces from the list
                                continue
                        else:
                                store=store+[item]#file content with the ids, seqs and matches
                print "store==", store
                seqidsseq=[]
                for seqid in store:#removing the matches leaving the ids and sequences                                      
                        if seqid.startswith("gi|"):
                                seqidsseq=seqidsseq+[seqid]               
                print "seqidsseq==", seqidsseq
                n=0
                for each in store:#finding the number of sequences
                        if each.startswith("*"):
                                while n==0:
                                        sequencenumber=store.index(each)
                                        n=1
                print "There are", sequencenumber,"sequences"
                seqids=[]
                for each in seqidsseq:#Making a list with either seqs or seqids
                        seqids=seqids+each.split()
                print seqids
                seqidsonly=[]
                for j in range(0,len(seqids),2):#isolating sequence ids
                        seqidsonly=seqidsonly+[seqids[j]]
                print seqidsonly
                seqsonly=[]
                for i in range(1,len(seqids),2):#isolating sequences
                        seqsonly=seqsonly+[seqids[i]]
                print seqsonly
                print len(seqsonly)
                print len(seqidsonly)
                lengths=[]
                for fragment in seqsonly:
                        fraglen=len(fragment)
                        lengths=lengths+[fraglen]
                print lengths
                seqids_only=seqidsonly[0:sequencenumber]#narrowing down, eliminating repitition
                print seqids_only
                seqdict={}
                for o in range(0,sequencenumber):
                        seqs_only=seqids_only[o]+" "
                        print seqids_only[o]                        
                        for c in range(o,len(seqsonly),sequencenumber):
                                seqs_only=seqs_only+seqsonly[c]
                        seqs_only=seqs_only.split()
                        print seqs_only
                        seqdict[seqs_only[0]]=seqs_only[1]
                return seqdict
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
