
import os
import tqdm

cnt = 0
cnt0 = 0
for i in os.listdir(os.path.join("january")) :
    f = open(os.path.join('january' , i), "r", encoding='UTF-8')
    lines = f.readlines()
    f.close()
    cnt+=1
    #print(cnt)
    Xindex , Yindex, Xlast, Ylast = 0, 0, 0, 0
    for line in lines:
        content = line.split()
        Xindex+=1
        Yindex = 0
        for element in content:
            Yindex +=1
            if element == 'REFERENCES' or element == 'References' or \
                (len(element) >= 10 and element[0]=='R' and element[1]=='e' and element[2]=='f' and element[3]== 'e' and element[4]== 'r' and element[5]== 'e' and element[6] == 'n' and element[7] == 'c' and element[8] == 'e' and element[9] == 's'):
                Xlast = Xindex
                Ylast = Yindex
    if Xlast == 0 :
        cnt0+=1

#

#'''
    newContain = []
    Xindex, Yindex = 0, 0           
    for line in lines:
        Xindex+=1
        if Xindex < Xlast:
            newContain.append(line)
            continue
        content = line.split()
        for element in content:
            Yindex +=1
            if Yindex < Ylast:
                newContain.append(element)
            else:
                break
        break
    f = open(os.path.join('feburary' , i), "w", encoding='UTF-8')
    f.write(' '.join(newContain))
    f.close()
    
#'''

print(cnt0)