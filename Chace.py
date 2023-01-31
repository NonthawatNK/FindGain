import pandas as pd

filename = "instance.txt"

df = pd.read_csv(filename, delimiter=",")

df.replace()


df["Att_1"]=df["Att_1"].replace(1,"A")
df["Att_1"] =df["Att_1"].replace(0,"B")

df["Att_2"]=df["Att_2"].replace(1,"C")
df["Att_2"]=df["Att_2"].replace(0,"D")

df["Att_3"]=df["Att_3"].replace(1,"E")
df["Att_3"]=df["Att_3"].replace(0,"F")

df["Att_4"]=df["Att_4"].replace(1,"G")
df["Att_4"]=df["Att_4"].replace(0,"H")

df["Att_5"]=df["Att_5"].replace(1,"I")
df["Att_5"]=df["Att_5"].replace(0,"J")

df["Att_6"]=df["Att_6"].replace(1,"K")
df["Att_6"]=df["Att_6"].replace(0,"L")

df["Att_7"]=df["Att_7"].replace(1,"M")
df["Att_7"]=df["Att_7"].replace(0,"N")

compression_opts = dict(method='zip',
                        archive_name='out.csv')  

df.to_csv('out.zip', index=False,
          compression=compression_opts)  