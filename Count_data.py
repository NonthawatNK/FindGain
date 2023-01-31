import numpy as np
from scipy import linalg


def Countdata(path):
    f=open(path,"r",encoding="utf-8")
    X=f.readlines()
        #เตรียม พื้นที่เพื่อเก็บผลการคำนวณแยกตาม class
    # f.close()

    # print(X)
    print("\n ",len(X))
    L=2 #col (2 class) // {0 ,1 }
    M=11 #row //  0-9 แบบ

    Attribute_1=np.zeros(2)
    Att_1CI=[[0 for i in range(M)] for j in range(L)] # zero matrix 11 rows 2 columns (class and info gain of Attribute_1)

    Attribute_2=np.zeros(2)
    Att_2CI=[[0 for i in range(M)] for j in range(L)] # zero matrix 11 rows 2 columns (class and info gain of Attribute_2)

    Attribute_3=np.zeros(2)
    Att_3CI=[[0 for i in range(M)] for j in range(L)] # zero matrix 11 rows 2 columns (class and info gain of Attribute_3)

    Attribute_4=np.zeros(2)
    Att_4CI=[[0 for i in range(M)] for j in range(L)] # zero matrix 11 rows 2 columns (class and info gain of Attribute_4)

    Attribute_5=np.zeros(2)
    Att_5CI=[[0 for i in range(M)] for j in range(L)] # zero matrix 11 rows 2 columns (class and info gain of Attribute_5)

    Attribute_6=np.zeros(2)
    Att_6CI=[[0 for i in range(M)] for j in range(L)] # zero matrix 11 rows 2 columns (class and info gain of Attribute_6)

    Attribute_7=np.zeros(2)
    Att_7CI=[[0 for i in range(M)] for j in range(L)] # zero matrix 11 rows 2 columns (class and info gain of Attribute_7)

    number_display = np.zeros(10)

        #วน loop เพื่อนับข้อมูล แยกตามรายละเอียด attb และ class
    """ ในที่นี้ข้อมูลเรามี Loop sample """
    for i in range(0,len(X)):
        #"""Attb 1"""
        if((X[i]).count('A') == 1):
            Attribute_1[0] += 1 
            if((X[i].count('A')==1)) and (X[i].count('0')==1):
                Att_1CI[0][0] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('1')==1):
                Att_1CI[0][1] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('2')==1):
                Att_1CI[0][2] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('3')==1):
                Att_1CI[0][3] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('4')==1):
                Att_1CI[0][4] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('5')==1):
                Att_1CI[0][5] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('6')==1):
                Att_1CI[0][6] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('7')==1):
                Att_1CI[0][7] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('8')==1):
                Att_1CI[0][8] +=1 
            elif((X[i].count('A')==1)) and (X[i].count('9')==1):
                Att_1CI[0][9] +=1 
        elif(X[i].count('B')==1):
            Attribute_1[1] +=1 
            if((X[i].count('B')==1)) and (X[i].count('0')==1):
                Att_1CI[1][0] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('1')==1):
                Att_1CI[1][1] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('2')==1):
                Att_1CI[1][2] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('3')==1):
                Att_1CI[1][3] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('4')==1):
                Att_1CI[1][4] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('5')==1):
                Att_1CI[1][5] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('6')==1):
                Att_1CI[1][6] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('7')==1):
                Att_1CI[1][7] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('8')==1):
                Att_1CI[1][8] +=1 
            elif((X[i].count('B')==1)) and (X[i].count('9')==1):
                Att_1CI[1][9] +=1 

    # """ Attb 2"""
        if((X[i]).count('C') == 1):
            Attribute_2[0] += 1 
            if((X[i].count('C')==1)) and (X[i].count('0')==1):
                Att_2CI[0][0] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('1')==1):
                Att_2CI[0][1] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('2')==1):
                Att_2CI[0][2] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('3')==1):
                Att_2CI[0][3] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('4')==1):
                Att_2CI[0][4] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('5')==1):
                Att_2CI[0][5] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('6')==1):
                Att_2CI[0][6] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('7')==1):
                Att_2CI[0][7] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('8')==1):
                Att_2CI[0][8] +=1 
            elif((X[i].count('C')==1)) and (X[i].count('9')==1):
                Att_2CI[0][9] +=1 
        elif(X[i].count('D')==1):
            Attribute_2[1] +=1 
            if((X[i].count('D')==1)) and (X[i].count('0')==1):
                Att_2CI[1][0] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('1')==1):
                Att_2CI[1][1] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('2')==1):
                Att_2CI[1][2] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('3')==1):
                Att_2CI[1][3] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('4')==1):
                Att_2CI[1][4] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('5')==1):
                Att_2CI[1][5] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('6')==1):
                Att_2CI[1][6] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('7')==1):
                Att_2CI[1][7] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('8')==1):
                Att_2CI[1][8] +=1 
            elif((X[i].count('D')==1)) and (X[i].count('9')==1):
                Att_2CI[1][9] +=1 

    # """ Attb 3"""
        if((X[i]).count('E') == 1):
            Attribute_3[0] += 1 
            if((X[i].count('E')==1)) and (X[i].count('0')==1):
                Att_3CI[0][0] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('1')==1):
                Att_3CI[0][1] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('2')==1):
                Att_3CI[0][2] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('3')==1):
                Att_3CI[0][3] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('4')==1):
                Att_3CI[0][4] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('5')==1):
                Att_3CI[0][5] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('6')==1):
                Att_3CI[0][6] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('7')==1):
                Att_3CI[0][7] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('8')==1):
                Att_3CI[0][8] +=1 
            elif((X[i].count('E')==1)) and (X[i].count('9')==1):
                Att_3CI[0][9] +=1 
        elif(X[i].count('F')==1):
            Attribute_3[1] +=1 
            if((X[i].count('F')==1)) and (X[i].count('0')==1):
                Att_3CI[1][0] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('1')==1):
                Att_3CI[1][1] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('2')==1):
                Att_3CI[1][2] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('3')==1):
                Att_3CI[1][3] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('4')==1):
                Att_3CI[1][4] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('5')==1):
                Att_3CI[1][5] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('6')==1):
                Att_3CI[1][6] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('7')==1):
                Att_3CI[1][7] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('8')==1):
                Att_3CI[1][8] +=1 
            elif((X[i].count('F')==1)) and (X[i].count('9')==1):
                Att_3CI[1][9] +=1 
    # """ Attb 4"""
        if((X[i]).count('G') == 1):
            Attribute_4[0] += 1 
            if((X[i].count('G')==1)) and (X[i].count('0')==1):
                Att_4CI[0][0] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('1')==1):
                Att_4CI[0][1] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('2')==1):
                Att_4CI[0][2] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('3')==1):
                Att_4CI[0][3] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('4')==1):
                Att_4CI[0][4] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('5')==1):
                Att_4CI[0][5] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('6')==1):
                Att_4CI[0][6] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('7')==1):
                Att_4CI[0][7] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('8')==1):
                Att_4CI[0][8] +=1 
            elif((X[i].count('G')==1)) and (X[i].count('9')==1):
                Att_4CI[0][9] +=1 
        elif(X[i].count('H')==1):
            Attribute_4[1] +=1 
            if((X[i].count('H')==1)) and (X[i].count('0')==1):
                Att_4CI[1][0] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('1')==1):
                Att_4CI[1][1] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('2')==1):
                Att_4CI[1][2] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('3')==1):
                Att_4CI[1][3] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('4')==1):
                Att_4CI[1][4] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('5')==1):
                Att_4CI[1][5] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('6')==1):
                Att_4CI[1][6] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('7')==1):
                Att_4CI[1][7] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('8')==1):
                Att_4CI[1][8] +=1 
            elif((X[i].count('H')==1)) and (X[i].count('9')==1):
                Att_4CI[1][9] +=1 

    # """Attb 5 "'"
        if((X[i]).count('I') == 1):
            Attribute_5[0] += 1 
            if((X[i].count('I')==1)) and (X[i].count('0')==1):
                Att_5CI[0][0] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('1')==1):
                Att_5CI[0][1] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('2')==1):
                Att_5CI[0][2] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('3')==1):
                Att_5CI[0][3] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('4')==1):
                Att_5CI[0][4] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('5')==1):
                Att_5CI[0][5] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('6')==1):
                Att_5CI[0][6] +=1
            elif((X[i].count('I')==1)) and (X[i].count('7')==1):
                Att_5CI[0][7] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('8')==1):
                Att_5CI[0][8] +=1 
            elif((X[i].count('I')==1)) and (X[i].count('9')==1):
                Att_5CI[0][9] +=1 
        elif(X[i].count('J')==1):
            Attribute_5[1] +=1 
            if((X[i].count('J')==1)) and (X[i].count('0')==1):
                Att_5CI[1][0] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('1')==1):
                Att_5CI[1][1] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('2')==1):
                Att_5CI[1][2] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('3')==1):
                Att_5CI[1][3] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('4')==1):
                Att_5CI[1][4] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('5')==1):
                Att_5CI[1][5] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('6')==1):
                Att_5CI[1][6] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('7')==1):
                Att_5CI[1][7] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('8')==1):
                Att_5CI[1][8] +=1 
            elif((X[i].count('J')==1)) and (X[i].count('9')==1):
                Att_5CI[1][9] +=1 
    # """Attb 6 "'"
        if((X[i]).count('K') == 1):
            Attribute_6[0] += 1 
            if((X[i].count('K')==1)) and (X[i].count('0')==1):
                Att_6CI[0][0] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('1')==1):
                Att_6CI[0][1] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('2')==1):
                Att_6CI[0][2] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('3')==1):
                Att_6CI[0][3] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('4')==1):
                Att_6CI[0][4] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('5')==1):
                Att_6CI[0][5] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('6')==1):
                Att_6CI[0][6] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('7')==1):
                Att_6CI[0][7] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('8')==1):
                Att_6CI[0][8] +=1 
            elif((X[i].count('K')==1)) and (X[i].count('9')==1):
                Att_6CI[0][9] +=1 
        elif(X[i].count('L')==1):
            Attribute_6[1] +=1 
            if((X[i].count('L')==1)) and (X[i].count('0')==1):
                Att_6CI[1][0] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('1')==1):
                Att_6CI[1][1] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('2')==1):
                Att_6CI[1][2] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('3')==1):
                Att_6CI[1][3] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('4')==1):
                Att_6CI[1][4] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('5')==1):
                Att_6CI[1][5] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('6')==1):
                Att_6CI[1][6] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('7')==1):
                Att_6CI[1][7] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('8')==1):
                Att_6CI[1][8] +=1 
            elif((X[i].count('L')==1)) and (X[i].count('9')==1):
                Att_6CI[1][9] +=1 
    # """Attb 7 "'"
        if((X[i]).count('M') == 1):
            Attribute_7[0] += 1 
            if((X[i].count('M')==1)) and (X[i].count('0')==1):
                Att_7CI[0][0] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('1')==1):
                Att_7CI[0][1] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('2')==1):
                Att_7CI[0][2] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('3')==1):
                Att_7CI[0][3] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('4')==1):
                Att_7CI[0][4] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('5')==1):
                Att_7CI[0][5] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('6')==1):
                Att_7CI[0][6] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('7')==1):
                Att_7CI[0][7] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('8')==1):
                Att_7CI[0][8] +=1 
            elif((X[i].count('M')==1)) and (X[i].count('9')==1):
                Att_7CI[0][9] +=1 
        elif(X[i].count('N')==1):
            Attribute_7[1] +=1 
            if((X[i].count('N')==1)) and (X[i].count('0')==1):
                Att_7CI[1][0] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('1')==1):
                Att_7CI[1][1] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('2')==1):
                Att_7CI[1][2] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('3')==1):
                Att_7CI[1][3] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('4')==1):
                Att_7CI[1][4] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('5')==1):
                Att_7CI[1][5] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('6')==1):
                Att_7CI[1][6] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('7')==1):
                Att_7CI[1][7] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('8')==1):
                Att_7CI[1][8] +=1 
            elif((X[i].count('N')==1)) and (X[i].count('9')==1):
                Att_7CI[1][9] +=1

        if (X[i].count('0')==1):
            number_display[0]+=1
        elif(X[i].count('1')==1):
            number_display[1]+=1
        elif(X[i].count('2')==1):
            number_display[2]+=1
        elif(X[i].count('3')==1):
            number_display[3]+=1
        elif(X[i].count('4')==1):
            number_display[4]+=1
        elif(X[i].count('5')==1):
            number_display[5]+=1
        elif(X[i].count('6')==1):
            number_display[6]+=1
        elif(X[i].count('7')==1):
            number_display[7]+=1
        elif(X[i].count('8')==1):
            number_display[8]+=1
        elif(X[i].count('9')==1):
            number_display[9]+=1


    returnAll = [
    Attribute_1,
    Att_1CI,
    Attribute_2,
    Att_2CI,
    Attribute_3,
    Att_3CI,
    Attribute_4,
    Att_4CI,
    Attribute_5,
    Att_5CI,
    Attribute_6,
    Att_6CI,
    Attribute_7,
    Att_7CI,
    number_display,
    X]
    return(returnAll)

