#!/usr/bin/env python
#module: novomod.py

# Copyright 2014 Arraiano-Castilho et al.


#######################################################
##                      SPLITTER                     ##
##             for high divergent genomes            ##
#######################################################


def novo (infile, seqList, out) :

    uDic = dict()
    rDic = dict()
    nmDic = dict()

    with open(infile, 'r') as infile, open(seqList, 'r') as RADlist :
        samples = [line.strip() for line in RADlist]
        lines = [line.strip() for line in infile]      
      
    #Create dictionaires with all the samples
        for i in samples:
            uDic[i.replace(" ","")] = 0
            rDic[i.replace(" ","")] = 0
            nmDic[i.replace(" ","")] = 0


        for k in lines:
            l1 = k.split("\t")
            l2 = l1[0].split(";")
            l3 = l2[0].replace(">","")
            if len(l1)<2:
                continue
            if l1[4] == "U":
                for k in uDic.keys():
                    if k == l3:
                        uDic[k] += 1
                  
            if l1[4] == "R":
                for j in rDic.keys():
                    if j == l3:
                        rDic[j] += 1
                          
            if l1[4] == "NM":
                for h in nmDic.keys():
                    if h == l3:
                        nmDic[h] += 1
                           
                    


    f = open(out, "w")
    f.write("Sample"+"\t"+"R"+"\t"+"U"+"\t"+"NM"+"\t"+"TOTAL"+"\t"+"%R"+"\t"+"%U"+"\t"+"%NM"+"\n")
    for i in samples:
        U = int()
        R = int()
        NM = int ()
        for k, j in uDic.items():
            if k == i:
                U = j
        for o, p in rDic.items():
            if o == i:
                R = p
        for y,u in nmDic.items():
            if y == i:
                NM = u
        TOTAL = int(U + R + NM) 
        try:
         f.write(i+"\t"+str(R)+"\t"+str(U)+"\t"+str(NM)+"\t"+str(TOTAL)+"\t"+str(float(R) / TOTAL)+"\t"+str(float(U) / TOTAL)+"\t"+str(float(NM) / TOTAL)+"\n")        
        except:
         f.write(i+"\t"+"ERROR: Sample missing in input"+"\n")

    f.close()



      
      
      
     
