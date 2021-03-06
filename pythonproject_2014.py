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
                matches=""
                for line in lines:#isolating matches, with their spaces
                        if line.startswith("CLUSTAL"):
                                continue
                        spaceind=0
                        if line.startswith("gi|"):
                                while spaceind==0:
                                        spaceindex=line.rindex(" ")
                                        spaceind=spaceind+spaceindex
                        else:
                                matches=matches+line[spaceind:-1].strip("\n")
                        
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
                return (aln,sequencenumber,seqdict,store,matches)
        else:           
                message="File might not be a valid fasta file, please enter a valid aln file"
                menu()
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
        for eachasq in read_aln_file(aln)[2].values():
                for nucleotide in eachsq:
                        if nucleotide=="C" or nucleotide=="G" or nucleotide=="A" or nucleotide=="T" and nucleotide!="-" :
                                lengthy=lengthy+1
                        else:
                                continue       
        print "Average Length:",lengthy/read_aln_file(aln)[1]
        stars=0
        for eachone in read_aln_file(aln)[3]:
                for one in eachone:
                        if one=="*":
                                stars=stars+1
        print "Number of [X] matches]:"
        print [read_aln_file(aln)[1]],":", stars
        for i in range(1, read_aln_file(aln)[1]-1):
                print [read_aln_file(aln)[1]-i],":"
        print "Percentage matches:",str(stars*100.0/lengthsq)+"%"
        exitsummary=raw_input("Press ENTER to return to menu ")
        if exitsummary==" ":
                menu()
        
#for option 3
def slicer(alnfile):
        startslice=input("Enter start position ")
        endslice=input("Enter end position ")
        print "Segment from",startslice,"to",endslice,"of sequences\n"
        for k in read_aln_file(aln)[2].keys():
                print k,":",
                print read_aln_file(aln)[2][k][startslice-1:endslice-1]
        print "Sequence identity or matches     :",
        print read_aln_file(aln)[4][startslice-1:endslice-1].lstrip()
        exitslice=raw_input("Press [enter] to display the menu again or E to select other segment: ")
        if exitslice==" ":
                menu()
        if exitslice=="e" or exitslice=="E":
                slicer(alnfile)
#for option 4
def seqisolate(alnfile):
        sequenceid=raw_input("Please enter sequence to analyse: ")
        seqinfo=read_aln_file(aln)[2][sequenceid]
        print "Sequence ID:",sequenceid
        seqlength=0
        SEQ=""
        for char in seqinfo:
                if char!="-":
                        seqlength=seqlength+1
                        SEQ=SEQ+char
        print "Sequence length:",seqlength
        print "A:",seqinfo.count("A")
        print "T:",seqinfo.count("T")
        print "G:",seqinfo.count("G")
        print "C:",seqinfo.count("C")
        for u in range(0,seqlength,60):
                print SEQ[u:u+60]
        print "*********************************************************************************"
        exitseqisolate=raw_input("Press enter to go to Menu or I to enter another sequence ID: ")
        if exitseqisolate==" ":
                menu()
        elif exitseqisolate=="i" or exitseqisolate=="I":
                seqisolate(alnfile)
#for option 5
def glycosig(aln):
        protdict={}
        for key,val in read_aln_file(aln)[2].items():
                protdict[key]=""
                rangelist=range(0,len(val),3)
                for r in rangelist:
                        aa=read_aln_file(aln)[2][key][r:r+3]
                        if aa=="ATG":
                                codon="M"                           
                        if aa=="ATT" or aa=="ATC" or aa=="ATA":
                                codon="I"                
                        if aa=="CTT" or aa=="CTC" or aa=="CTA" or aa=="CTG" or aa=="TTA" or aa=="TTG":
                                codon="L"                
                        if aa=="GTT" or aa=="GTC" or aa=="GTA" or aa=="GTG":
                                codon="V"                 
                        if aa=="TTT" or aa=="TTC":
                                codon="F"                
                        if aa=="TGT" or aa=="TGC":
                                codon="C"                
                        if aa=="GCT" or aa=="GCG" or aa=="GCA" or aa=="GCC":
                                codon="A"               
                        if aa=="GGT" or aa=="GGC" or aa=="GGA" or aa=="GGG":
                                codon="G"
                        if aa=="CCT" or aa=="CCC" or aa=="CCA" or aa=="CCG":
                                codon="P"
                        if aa=="ACT" or aa=="ACC" or aa=="ACA" or aa=="ACG":
                                codon="T"
                        if aa=="TCT" or aa=="TCC" or aa=="TCA" or aa=="TCG" or aa=="AGT" or aa=="AGC":
                                codon="S"
                        if aa=="TAT" or aa=="TAC":
                                codon="Y"
                        if aa=="TGG":
                                codon="W"
                        if aa=="CAG" or aa=="CAA":
                                codon="Q"
                        if aa=="AAT" or aa=="AAC":
                                codon="N"
                        if aa=="CAT" or aa=="CAC":
                                codon="H"
                        if aa=="GAA" or aa=="GAG":
                                codon="E"
                        if aa=="GAT" or aa=="GAG":
                                codon="D"
                        if aa=="AAA" or aa=="AAG":
                                codon="K"
                        if aa=="CGT" or aa=="CGC" or aa=="CGA" or aa=="CGG" or aa=="AGA" or aa=="AGG":
                                codon="R"
                        if aa=="TAG" or aa=="TAA" or aa=="TGA":
                                codon="*stop*" 
                        protdict[key]=protdict[key]+codon
        for key,val in protdict.items():
                import re
                regexobj=re.compile("N[^P][ST]")
                regexobj.findall(val)
                if regexobj.findall(val)!=[]:
                        print "Glycosylation Signatures found in", key
                        print val
        exitglysig=raw_input("Press enter for menu ")
        if exitglysig==" ":
                menu() 
        return protdict
#for option 6
def fastaexport(alnfile,):
        filewrite=open(file,"w+")
        filetype=raw_input("Do you want to create Multiple files(one per sequence) press M or press S for a single file that includes all the sequences ")
        if filetype=="S" or filetype=="S":
                filewrite.writelines()
                
        
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
                        #global aln
                        summary(aln)
                elif option==3:
                        slicer(aln)
                elif option==4:
                        seqisolate(aln)
                elif option==5:
                        import re
                        glycosig(aln)
                elif option==6:
                        fastaexport(aln,protdict)
                elif option==7: 
                        refresh=exitapp()                                
                else:
                        print "Invalid option entered, enter one value from 1 to 7"
message="No sequence loaded into memory"
refresh=0
menu()




