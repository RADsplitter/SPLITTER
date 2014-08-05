#!/usr/bin/env python
#module: samomod.py

# Copyright 2014 Arraiano-Castilho et al.


#######################################################
##                      SPLITTER                     ##
##             for high divergent genomes            ##
#######################################################




def sam (infile, seqList, out) :    
    rDic = dict()
    nmDic = dict()

    with open(infile, 'r') as infile, open(seqList, 'r') as RADlist :
        samples = [line.strip() for line in RADlist]
        lines = [line.strip() for line in infile]      
      
    #Create dictionaires with all the samples
        for i in samples:            
            rDic[i.replace(" ","")] = 0
            nmDic[i.replace(" ","")] = 0


        for k in lines:
            l1 = k.split()
            l2 = l1[0].split(";")
            if len(l1)<10:
                continue                              
            if "ZS:Z:R" in l1:
                for j in rDic.keys():
                    if j == l2[0]:
                        rDic[j] += 1
                          
            if "ZS:Z:NM" in l1 :
                for h in nmDic.keys():
                    if h == l2[0]:
                        nmDic[h] += 1
                           
                    


    f = open(out, "w")
    f.write("Sample"+"\t"+"R"+"\t"+"NM"+"\t"+"TOTAL"+"\t"+"%R"+"\t"+"%NM"+"\n")
    for i in samples:
        R = int()
        NM = int()
        for o, p in rDic.items():
            if o == i:
                R = p
        for y,u in nmDic.items():
            if y == i:
                NM = u
        TOTAL = int (R + NM)
        try:
         f.write(i+"\t"+str(R)+"\t"+str(NM)+"\t"+str(TOTAL)+"\t"+str(float(R) / TOTAL)+"\t"+str(float(NM) / TOTAL)+"\n")                
        except:
         f.write(i+"\t"+"ERROR: Sample missing in input"+"\n")
        

    f.close()



      
      
      
     

