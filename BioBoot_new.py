"""
Модуль обработки данных
"""

def execute(fasta, l_spic_min, l_spic_max, missing_can):
    fasta_uni = []
    kod = ''
    for string_fasta in fasta:
        if string_fasta[0] == '>':
            fasta_uni.append(kod)
            fasta_uni.append(string_fasta)
            kod = ''
        else:
            kod += string_fasta
    fasta_uni.append(kod)
    fasta_uni=fasta_uni[1:]
    fasta_uni_big=[]
    for fasta_uni_num in range(0,len(fasta_uni),2):
        fasta_uni_big_sp=[]
        chr_fasta_uni_big=''
        for string_fasta_uni_sy in fasta_uni[fasta_uni_num][1:]:
            if string_fasta_uni_sy=='|':
                break
            chr_fasta_uni_big+=string_fasta_uni_sy
        for gg in fasta_uni[fasta_uni_num].split('|'):
          if gg[:8]=='EPI_ISL_':
            epi_fasta_uni_big=gg
        fasta_uni_big_sp.append(chr_fasta_uni_big)
        fasta_uni_big_sp.append(epi_fasta_uni_big)
        fasta_uni_big_sp.append(fasta_uni[fasta_uni_num])
        fasta_uni_big_sp.append(fasta_uni[fasta_uni_num+1])
        fasta_uni_big.append(fasta_uni_big_sp)
    #l_spic_min=int(input('Какое минимальное число нуклеотидов в спейсере? '))
    #l_spic_max=int(input('Какое максимальное число нуклеотидов в спейсере? '))
    #missing_can=int(input('Сколько ошибок допускается в спейсере? '))
    spays=[]
    v=0
    max_spey=[]
    while True:
        fasta_uni_big_new=[]
        n_spey1=0
        k=-1
        for l_spic in range(l_spic_min, l_spic_max+1):
            for fasta_uni_big_sp in fasta_uni_big:
                k+=1
                spic=''
                for n_start in range(0,len(fasta_uni_big_sp[3])):
                        if len(fasta_uni_big_sp[3][n_start:n_start+l_spic])==l_spic:
                            spey=fasta_uni_big_sp[3][n_start:n_start+l_spic]
                            #print(spey,end=' ')
                            org_minus={}
                            for fasta_uni_big_sp in fasta_uni_big:
                                for n_start in range(0, len(fasta_uni_big_sp[3])-len(spey)+1):
                                    nucl_num=0
                                    missing=0
                                    for nucl in fasta_uni_big_sp[3][n_start:n_start+len(spey)+1]:
                                        if nucl!=spey[nucl_num]:
                                            missing+=1
                                        if missing-1==missing_can:
                                            test=0
                                            break
                                        nucl_num+=1
                                        if nucl_num==len(spey):
                                            test=1
                                            break
                                    if test==1:
                                        org_minus[fasta_uni_big_sp[1]]=0
                            n_spey2=len(org_minus)
                            #print(n_spey2, end=' ')
                            if n_spey2>=n_spey1:
                                n_spey1=n_spey2
                                spey0=spey
                            v+=1
                            #print('Посчитано',' ',v,' ','спейсеров')
                            fasta_uni_big_sp=fasta_uni_big[k]
        #print('Max спейсер', ' ', spey0, ' ', n_spey1)
        max_spey = [spey0, n_spey1] #данные о максимальном спейсере
        spays.append(spey0+' '+str(n_spey1))
        org_minus0={}
        for fasta_uni_big_sp in fasta_uni_big:
          for n_start0 in range(0, len(fasta_uni_big_sp[3])-len(spey0)+1):
            nucl_num0=0
            missing0=0
            for nucl0 in fasta_uni_big_sp[3][n_start0:n_start0+len(spey0)+1]:
              if nucl0 != spey0[nucl_num0]:
                missing0+=1
              if missing0-1==missing_can:
                test0=0
                break
              nucl_num0+=1
              if nucl_num0==len(spey0):
                test0=1
                break
            if test0==1:
              org_minus0[fasta_uni_big_sp[1]]=0
        for fasta_uni_big_sp in fasta_uni_big:
              for org0 in org_minus0:
                haha=1
                if fasta_uni_big_sp[1]==org0:
                  haha=0
                  break
              if haha==1:
                fasta_uni_big_new.append(fasta_uni_big_sp)
        fasta_uni_big=fasta_uni_big_new
        if len(fasta_uni_big)==0:
          break
    #print(spays)
    return max_spey, spays