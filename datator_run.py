#Script realizzato da Nicholas Giordano - Python3
#www.nicholasgiordano.it
#Distribuito sotto licenza GNUv3.0
#Data Studio output to R Statistic input
def run():
    #--SELECT FILE
    file_name=str(input('Inserisci nome del file da trattare: ')).replace('.txt','')
    try:
        file_o=open(file_name+'.txt','r')
        print('file aperto...inizio analisi...\n')
        l=file_o.readlines()
        file_o.close()
        #--END FILE
        #--SETTING NAME
        t1=input('nome prima variabile: ')
        t1=t1+'<-'+t1[0].lower()+'('
        t2=input('nome seconda variabile: ')
        t2=t2+'<-'+t2[0].lower()+'('
        #--END NAME
        #--START ANALYSIS
        valid_char=[1,2,3,4,5,6,7,8,9,',']
        for k in l:
            t=','
            if k==l[len(l)-1]:
                t=')'
            r_list=k.split()
            if k[0] and k[1] in valid_char:
                t1=t1+r_list[0]+t
                t2=t2+r_list[1]+t
        #--END ANALYSIS
        #--WRITE OUTPUT_FILE
        file_w=open('AUT_'+file_name+'.txt','w')
        file_w.write(t1+'\n'+t2)
        file_w.close()
        #--END WRITE
        input('Processo completato!\nPremere un tasto per ricominciare, CTRL+C per uscire')
    except:
        print("Errore elaborazione file")
    run()
print('#Script realizzato da Nicholas Giordano\n#www.nicholasgiordano.it\n#Distribuito sotto licenza GNU3.0\n')
print('Supporta input di due colonne')
run()
