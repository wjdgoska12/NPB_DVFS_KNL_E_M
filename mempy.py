import subprocess
import time
import sys
import re
import csv

LL=[]
second=0.0


eSUM1=0.0
eSUM2=0.0
eSUM3=0.0
eSUM4=0.0
eSUM5=0.0
eSUM6=0.0
eSUM7=0.0
eSUM8=0.0
eSUM9=0.0
eSUM10=0.0
eSUM11=0.0
eSUM12=0.0


LR=[]
p=[]
s=[]
k=[]
time=0

if __name__ == "__main__":
    f = open("/chome/wkucslab01/DVFS/milli_second/"+sys.argv[1],'r')
        re=csv.reader(f)
            #print(re[1000])
                for i in re:
                        p.append(i)
                            for x in p:
                                    if len(x) > 2 :
                                                time=float(x[0])
                                                            if "uncore_imc_0/event=0x03" in x :
                                                                           #print(x[1])
                                                                                          eSUM1+=float(x[1])

                                                                                                      if "uncore_imc_1/event=0x03" in x :
                                                                                                                     eSUM1+=float(x[1])

                                                                                                                                 if "uncore_imc_2/event=0x03" in x :
                                                                                                                                                eSUM1+=float(x[1])

                                                                                                                                                            if "uncore_imc_3/event=0x03" in x :
                                                                                                                                                                           eSUM1+=float(x[1])

                                                                                                                                                                                       if "uncore_imc_4/event=0x03" in x :
                                                                                                                                                                                                      eSUM1+=float(x[1])

                                                                                                                                                                                                                  if "uncore_imc_5/event=0x03" in x :
                                                                                                                                                                                                                                 eSUM1+=float(x[1])


                                                                                                                                                                                                                                 print(eSUM1)
                                                                                                                                                                                                                                 print(time)


                                                                                                                                                                                                                                 print(eSUM1/time)



