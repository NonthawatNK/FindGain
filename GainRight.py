from scipy import linalg
import numpy as np
from numpy import loadtxt
import math
from Dtreefunc import *
from Count_data import *

# เตรียมข้อมูล และ นับข้อมูล
path = "D:\data_mining\Dessiontree\L2\\NumDisplayL2right.csv"
# path = "D:\data_mining\Dessiontree\L2\DisplayL2left.csv"
allCount = Countdata(path)
# Attribute_1=allCount[0]
# Att_1CI=allCount[1]
Attribute_2=allCount[2]
Att_2CI=allCount[3]
Attribute_3=allCount[4]
Att_3CI=allCount[5]
Attribute_4=allCount[6]
Att_4CI=allCount[7]
Attribute_5=allCount[8]
Att_5CI=allCount[9]
Attribute_6=allCount[10]
Att_6CI=allCount[11]
Attribute_7=allCount[12]
Att_7CI=allCount[13]
NumberDisplay = allCount[14]
X = allCount[15]



"""calculate information gain of dataset and attb"""
""" info D,Att_2,Att_3,Att_4,Att_5,Att_6,Att_7"""

info = np.zeros(7) #7
InD=entropymany9(
NumberDisplay[0],
NumberDisplay[1],
NumberDisplay[2],
NumberDisplay[3],
NumberDisplay[4],
NumberDisplay[5],
NumberDisplay[6],
NumberDisplay[7],
NumberDisplay[8],
NumberDisplay[9],
)

# Att_1CI[0][10] = entropymany9(
#                 Att_1CI[0][0],
#                 Att_1CI[0][1],
#                 Att_1CI[0][2],
#                 Att_1CI[0][3],
#                 Att_1CI[0][4],
#                 Att_1CI[0][5],
#                 Att_1CI[0][6],
#                 Att_1CI[0][7],
#                 Att_1CI[0][8],
#                 Att_1CI[0][9],)
# Att_1CI[1][10] =entropymany9(
#                 Att_1CI[1][0],
#                 Att_1CI[1][1],
#                 Att_1CI[1][2],
#                 Att_1CI[1][3],
#                 Att_1CI[1][4],
#                 Att_1CI[1][5],
#                 Att_1CI[1][6],
#                 Att_1CI[1][7],
#                 Att_1CI[1][8],
#                 Att_1CI[1][9],)

Att_2CI[0][10] = entropymany9(
                Att_2CI[0][0],
                Att_2CI[0][1],
                Att_2CI[0][2],
                Att_2CI[0][3],
                Att_2CI[0][4],
                Att_2CI[0][5],
                Att_2CI[0][6],
                Att_2CI[0][7],
                Att_2CI[0][8],
                Att_2CI[0][9],)
Att_2CI[1][10] =entropymany9(
                Att_2CI[1][0],
                Att_2CI[1][1],
                Att_2CI[1][2],
                Att_2CI[1][3],
                Att_2CI[1][4],
                Att_2CI[1][5],
                Att_2CI[1][6],
                Att_2CI[1][7],
                Att_2CI[1][8],
                Att_2CI[1][9],)

Att_3CI[0][10] = entropymany9(
                Att_3CI[0][0],
                Att_3CI[0][1],
                Att_3CI[0][2],
                Att_3CI[0][3],
                Att_3CI[0][4],
                Att_3CI[0][5],
                Att_3CI[0][6],
                Att_3CI[0][7],
                Att_3CI[0][8],
                Att_3CI[0][9],)
Att_3CI[1][10] =entropymany9(
                Att_3CI[1][0],
                Att_3CI[1][1],
                Att_3CI[1][2],
                Att_3CI[1][3],
                Att_3CI[1][4],
                Att_3CI[1][5],
                Att_3CI[1][6],
                Att_3CI[1][7],
                Att_3CI[1][8],
                Att_3CI[1][9],)

Att_4CI[0][10] = entropymany9(
                Att_4CI[0][0],
                Att_4CI[0][1],
                Att_4CI[0][2],
                Att_4CI[0][3],
                Att_4CI[0][4],
                Att_4CI[0][5],
                Att_4CI[0][6],
                Att_4CI[0][7],
                Att_4CI[0][8],
                Att_4CI[0][9],)
Att_4CI[1][10] =entropymany9(
                Att_4CI[1][0],
                Att_4CI[1][1],
                Att_4CI[1][2],
                Att_4CI[1][3],
                Att_4CI[1][4],
                Att_4CI[1][5],
                Att_4CI[1][6],
                Att_4CI[1][7],
                Att_4CI[1][8],
                Att_4CI[1][9],)

Att_5CI[0][10] = entropymany9(
                Att_5CI[0][0],
                Att_5CI[0][1],
                Att_5CI[0][2],
                Att_5CI[0][3],
                Att_5CI[0][4],
                Att_5CI[0][5],
                Att_5CI[0][6],
                Att_5CI[0][7],
                Att_5CI[0][8],
                Att_5CI[0][9],)
Att_5CI[1][10] =entropymany9(
                Att_5CI[1][0],
                Att_5CI[1][1],
                Att_5CI[1][2],
                Att_5CI[1][3],
                Att_5CI[1][4],
                Att_5CI[1][5],
                Att_5CI[1][6],
                Att_5CI[1][7],
                Att_5CI[1][8],
                Att_5CI[1][9],)

Att_6CI[0][10] = entropymany9(
                Att_6CI[0][0],
                Att_6CI[0][1],
                Att_6CI[0][2],
                Att_6CI[0][3],
                Att_6CI[0][4],
                Att_6CI[0][5],
                Att_6CI[0][6],
                Att_6CI[0][7],
                Att_6CI[0][8],
                Att_6CI[0][9],)
Att_6CI[1][10] =entropymany9(
                Att_6CI[1][0],
                Att_6CI[1][1],
                Att_6CI[1][2],
                Att_6CI[1][3],
                Att_6CI[1][4],
                Att_6CI[1][5],
                Att_6CI[1][6],
                Att_6CI[1][7],
                Att_6CI[1][8],
                Att_6CI[1][9],)

Att_7CI[0][10] = entropymany9(
                Att_7CI[0][0],
                Att_7CI[0][1],
                Att_7CI[0][2],
                Att_7CI[0][3],
                Att_7CI[0][4],
                Att_7CI[0][5],
                Att_7CI[0][6],
                Att_7CI[0][7],
                Att_7CI[0][8],
                Att_7CI[0][9],)
Att_7CI[1][10] =entropymany9(
                Att_7CI[1][0],
                Att_7CI[1][1],
                Att_7CI[1][2],
                Att_7CI[1][3],
                Att_7CI[1][4],
                Att_7CI[1][5],
                Att_7CI[1][6],
                Att_7CI[1][7],
                Att_7CI[1][8],
                Att_7CI[1][9],)

""" หาค่า gain แบบไม่ใช้ และใช้ฟังก์ชัน"""
"""
การหาแบบไม่ใช้ฟังก์ชัน
Info_ageD = ((age[0]/14)*ageCI[0][2])+((age[1]/14)*ageCI[1][2])+((age[2]/14)*ageCI[2][2])
print("InfoD age is",Info_ageD)
print("Age Ci [:],[2] is",[ageCI[0][2],ageCI[1][2],ageCI[2][2]])
print("InfoD age is",Info_ageD)
"""
# ตัวคูณกับ ค่า Infor
# Info_Att1D = inforD(Attribute_1,[Att_1CI[0][10],Att_1CI[1][10]])
Info_Att2D = inforD(Attribute_2,[Att_2CI[0][10],Att_2CI[1][10]])
Info_Att3D = inforD(Attribute_3,[Att_3CI[0][10],Att_3CI[1][10]])
Info_Att4D = inforD(Attribute_4,[Att_4CI[0][10],Att_4CI[1][10]])
Info_Att5D = inforD(Attribute_5,[Att_5CI[0][10],Att_5CI[1][10]])
Info_Att6D = inforD(Attribute_6,[Att_6CI[0][10],Att_6CI[1][10]]) 
Info_Att7D = inforD(Attribute_7,[Att_7CI[0][10],Att_7CI[1][10]])



# แสดงผลการทำงานรอบแรก
"""
print("Age count is", age)
print("income count is",income)
print("student count is",stu)
print("credit rating count is",credit)
print("Buy computer count is",buy)
print("Age Info relate to class",ageCI)
print("Income Info relate to class",incomeCI)
print("Student Info relate to class",stuCI)
print("Credit rating Info relate to class",creditCI)

print("Info(D) is %5.3f" % InD)
print("Info(age <=30(2,3) is %5.3f" % ageCI[0][2])
print("Info(age 31...40(4,0) is %5.3f" % ageCI[1][2])
print("Info(age >40 (3,2) is %5.3f" % ageCI[2][2])

print("Info(income low(1,3) is %5.3f" % incomeCI[0][2])
print("Info(income medium(2,4) is %5.3f" % incomeCI[1][2])
print("Info(income high(2,2) is %5.3f" % incomeCI[2][2])

print("Info(student No (4,3) is %5.3f" % stuCI[0][2])
print("Info(student Yes (1,6) is %5.3f" % stuCI[1][2])

print("Info(credit fair(2,6) is %5.3f" % creditCI[0][2])
print("Info(credit excellent(3,3) is %5.3f" % creditCI[1][2])
print("Info age (D) is %5.3f" % Info_ageD)
print("Info income (D) is %5.3f" % Info_incomeD)
print("Info student (D) is %5.3f" % Info_studentD)
print("Info credit rating (D) is %5.3f" % Info_creditD)
"""
print("\n***Gain results of right dataset***")
gianInd = InD 
print("Ginn (Ind) is %5.3f"% gianInd)
# gainAtt1=InD-Info_Att1D
# print("Gain (Att_1) is %5.3f"% gainAtt1)
gainAtt2=InD-Info_Att2D
print("Gain (Att_2) is %5.3f"% gainAtt2)
gainAtt3=InD-Info_Att3D
print("Gain (Att_3) is %5.3f"% gainAtt3)
gainAtt4=InD-Info_Att4D
print("Gain (Att_4) is %5.3f"% gainAtt4)
gainAtt5=InD-Info_Att5D
print("Gain (Att_5) is %5.3f"% gainAtt5)
gainAtt6=InD-Info_Att6D
print("Gain (Att_6) is %5.3f"% gainAtt6)
gainAtt7=InD-Info_Att7D
print("Gain (Att_7) is %5.3f"% gainAtt7)

#rule of root node

Result_All=[gainAtt2,gainAtt3,gainAtt4,gainAtt5,gainAtt6,gainAtt7]
max_gain=max(Result_All)
pos=np.argmax(Result_All)
print("max gain of attb is %5.3f" % max_gain,"position is",pos)



f5=open("D:\data_mining\Dessiontree\mDisplayL2rightleft.csv","w")
f6=open("D:\data_mining\Dessiontree\mDisplayL2rightright.csv","w")

#นับจำนวน Attb ที่คัดออกไปเป็น Root คือ Att 2 C D
n = len(X)
for i in range(0,n):
    if ((X[i].count('C')==1)): 
        f5.write(str(X[i]))
    elif(X[i].count('D')==1):
        f6.write(str(X[i]))

