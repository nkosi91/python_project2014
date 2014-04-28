#for option 1
def read_aln_file(alnfile):
        aln=open(alnfile, "r")#opening the aln file
        aln.seek(0,0)
        if alnfile.endswith(".aln"):#checking if extension is correct
                lines=aln.readlines()
                aln.close()#closing aln file
        if lines[0].startswith("CLUSTAL"):#checking if it is a valid clustal file
                seq=[]#making a list of everything found in the document
                for line in lines:
                        if line.startswith("CLUSTAL"):#excluding the header in the list
                                continue
                        else:
                                nline=line.strip()#removing "next lines" in the list
                                seq=seq+[nline]                                              
                store=[]
                for item in seq:
                        if item=="":#removing the spaces from the list
                                continue
                        else:
                                store=store+[item]#file content with the ids, seqs and matches
                seqidsseq=[]
                for seqid in store:#removing the matches leaving the ids and sequences                                      
                        if seqid.startswith("gi|"):
                                seqidsseq=seqidsseq+[seqid]            
                                n=0
                for each in store:#finding the number of sequences
                        if each.startswith("*"):
                                while n==0:
                                        sequencenumber=store.index(each)
                                        n=1
                seqids=[]
                for each in seqidsseq:#Making a list with both seqs or seqids in a list
                        seqids=seqids+each.split()
                seqidsonly=[]
                for j in range(0,len(seqids),2):#isolating sequence ids
                        seqidsonly=seqidsonly+[seqids[j]]
                seqsonly=[]
                for i in range(1,len(seqids),2):#isolating sequences
                        seqsonly=seqsonly+[seqids[i]]
                lengths=[]
                for fragment in seqsonly:
                        fraglen=len(fragment)#fragment lengths
                seqids_only=seqidsonly[0:sequencenumber]#narrowing down, eliminating repitition
                seqdict={}
                for o in range(0,sequencenumber):
                        seqs_only=seqids_only[o]+" "                       
                        for c in range(o,len(seqsonly),sequencenumber):
                                seqs_only=seqs_only+seqsonly[c]
                        seqs_only=seqs_only.split()
                        seqdict[seqs_only[0]]=seqs_only[1]
                dashes=0
                for each in seqdict.values():
                        dashes=dashes+each.count("-")
                print dashes
                return (aln,sequencenumber,seqdict)
        else:           
                message="File might not be a valid fasta file, please enter a valid aln file"
                refresh=0
        menu()

#for option 2
def summary(alnfile):
        print "File loaded:", read_aln_file(aln)[0]
        print "Number of sequences loaded to memory:", read_aln_file(aln)[1]
        print "Sequences loaded to memory:"
        for each in read_aln_file(aln)[2].keys():
                print "-", each
        for eachsq in read_aln_file(aln)[2].values():
                lengthsq=len(eachsq)
        print "Length:",lengthsq
        lengthy=0
        dashy=0
        for eachasq in read_aln_file(aln)[2].values():
                for nucleotide in eachsq:
                        if nucleotide=="C" or nucleotide=="G" or nucleotide=="A" or nucleotide=="T" :
                                lengthy=lengthy+1
                        elif nucleotide=="-":
                                continue 
                        else:
                                continue       
        print "Average Length:",lengthy
        print "Number of [X] matches]:" 
        
        exitsummary=raw_input("Press ENTER to return to menu ")
        if exitsummary==" ":
                menu()
        
#for option 3

#for option 4

#for option 5

#for option 6

#for option 7
def exitapp():
        confirm=raw_input("Are you sure you want to exit? Press Y to exit and N to continue ")
        if confirm== "Y" or confirm=="y":
                print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*Exiting*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
                return 1
        elif confirm=="N"or confirm=="n":
                return 0 
        else:
                print "Invalid option chosen, exiting anyways"
                return 1
#menu
def menu():
        global refresh
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
                global message
                print message
                print deco
                option=input("Please enter the number of chosen option ")
                if option==1:
                        aln=raw_input("Enter path to aln file ")
                        message="Sequence loaded successfully into memory"
                        read_aln_file(aln)
                elif option==2:
                        global aln
                        summary(aln)
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
                        refresh=exitapp()                                
                else:
                        print "Invalid option entered, enter one value from 1 to 7"
message="No sequence loaded into memory"
refresh=0
menu()



