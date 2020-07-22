# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:15:23 2019

@author: Tarun Acharya
"""

import matplotlib.pyplot as plt
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'qt')
from tkinter import StringVar
import tkinter as tk
from tkinter import ttk

x=[]
y=[]
sizes=[]
import pandas as pd

import os 
t=str(os.path.dirname(os.path.realpath(__file__)))
df=pd.read_csv(t+"\\fooddata.csv")
def abc():
    
     a=val.get()
     b=float(val1.get())
     x.append(a)
     y.append(b)
     

def submit(z1,z2,z3,z4,z5):
    global app
    x1=[]
    for i in x:
        c=0
        for j in df['Food(100gm)']:
            if i==j:
                x1.append(c)
            c=c+1
           
     
    tot_fat=0
    for i in range(0,len(x)):    
        tot_fat=tot_fat+df['Fat(gm)'][x1[i]]*y[i]/100
    sizes.append(round(tot_fat,2))
    tot_prot=0
    for i in range(0,len(x)):    
        tot_prot=tot_prot+df['Protein(gm)'][x1[i]]*y[i]/100
    sizes.append(round(tot_prot,2))
    tot_carb=0
    for i in range(0,len(x)):    
        tot_carb=tot_carb+df['Carbohydrate(gm)'][x1[i]]*y[i]/100
    sizes.append(round(tot_carb,2))
    tot_chol=0
    for i in range(0,len(x)):    
        tot_chol=tot_chol+df['Cholestrol'][x1[i]]*y[i]/100
    sizes.append(round(tot_chol,4))  
    tot_cal=0
    for i in range(0,len(x)):    
        tot_cal=tot_cal+df['Calories'][x1[i]]*y[i]
     
    
    if(tot_carb<=325 and tot_carb>=225):
        x5="You have an optimal carbohydrate intake."
    elif(tot_carb<225):
        x5="You are running low on carbohydrates."
    else:
        x5="Your carbohydrate intake is high."
    
    
    if(tot_fat<=77 and tot_fat>=44):
        x1="You have an optimal fat intake."
    elif(tot_fat<44):
        x1="You are running low on fat."
    else:
        x1="Your fat intake is high."
    
    
    if(tot_prot<=56 and tot_prot>=46):
        x2="You have an optimal protein intake."
    elif(tot_prot<46):
        x2="You are running low on proteins."
    else:
        x2="Your protein intake is high."
    
    
    if(tot_chol<=0.3 and tot_chol>=0.225):
        x3="You have an optimal cholestrol intake."
    elif(tot_chol<0.225):
        x3="You are running low on cholestrol."
    else:
        x3="Your cholestrol intake is high."
    
    
    if(tot_cal<=2500 and tot_cal>=1900):
        x4="You have an optimal calorie intake."
    elif(tot_cal<1900):
        x4="You are running low on calories."
    else:
        x4="Your calorie intake is high."
        
    
    '''lb1=tk.Label(app,textvariable=StringVar(x1)).pack()
    lb2=tk.Label(app,textvariable=StringVar(x2)).pack()
    lb3=tk.Label(app,textvariable=StringVar(x3)).pack()
    lb4=tk.Label(app,textvariable=StringVar(x4)).pack()
    lb5=tk.Label(app,textvariable=StringVar(x5)).pack()
    '''
    q=StringVar()
    q.set(x1)
    z1.config(textvariable=q)
    q=StringVar()
    q.set(x2)
    z2.config(textvariable=q)
    q=StringVar()
    q.set(x3)
    z3.config(textvariable=q)
    q=StringVar()
    q.set(x4)
    z4.config(textvariable=q)
    q=StringVar()
    q.set(x5)
    z5.config(textvariable=q)
    

def plot():
    
    labels = 'Fat','Protein','Carbohydrate','Cholestrol'
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal') 
    plt.show()
    sizes.clear()
    x.clear()
    y.clear()

def new():
    root=tk.Tk()
    root.title("Kost")
    #root.wm_iconbitmap('kost.ico')
    root.geometry("500x500")
    txt=tk.StringVar()
    txt1=tk.StringVar()
    txt2=tk.StringVar()
    txt3=tk.StringVar()
    txt4=tk.StringVar()
    txt5=tk.StringVar()
    l1=tk.Label(root,text="Food(100g)").pack()
    e1=tk.Entry(root,textvariable=txt)
    e1.pack()
    l2=tk.Label(root,text="Calories").pack()
    e2=tk.Entry(root,textvariable=txt1)
    e2.pack()
    l3=tk.Label(root,text="Protein").pack()
    e3=tk.Entry(root,textvariable=txt2)
    e3.pack()
    l4=tk.Label(root,text="Fat").pack()
    e4=tk.Entry(root,textvariable=txt3)
    e4.pack()
    l5=tk.Label(root,text="Carbohydrate").pack()
    e5=tk.Entry(root,textvariable=txt4)
    e5.pack()
    l6=tk.Label(root,text="Cholestrol").pack()
    e6=tk.Entry(root,textvariable=txt5)
    e6.pack()
    ttk.Button(root,text="submit",command=lambda:sub(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),root)).pack()
    def sub(m,m1,m2,m3,m4,m5,m6):
        global df
        m1=float(m1)    
        m2=float(m2)
        m3=float(m3)
        m4=float(m4)
        m5=float(m5)
        df2=pd.DataFrame([[m,m1,m2,m3,m4,m5]],columns=['Food(100gm)','Calories','Protein(gm)','Fat(gm)','Carbohydrate(gm)','Cholestrol'])
        def insert_row(idx, df, df_insert):
            return df.iloc[:idx, ].append(df_insert).append(df.iloc[idx:, ]).reset_index(drop = True)
        rc=int(df.shape[0])+1
        df = insert_row(rc, df, df2)
        df = df.sort_values(['Food(100gm)'])
        df.to_csv(t+"\\fooddata.csv", encoding='utf-8', index=False)
        m6.destroy()

k=list(df['Food(100gm)'])
app = tk.Tk() 
app.title("Kost")
app.geometry('500x500')
#app.wm_iconbitmap('kost.ico')
labelTop = tk.Label(app,
                    text = "Choose your type food intake today")
labelTop.pack()
val=StringVar()
val1=StringVar()
comboExample = ttk.Combobox(app,textvariable=val, 
                            values=k)


 
comboExample.pack()
comboExample.current(1)


lb=tk.Label(app,text="food intake(in grams):").pack()
en1=tk.Entry(app,textvariable=val1).pack()



tk.Button(app,text="Add",command=abc,width=10).place(x=200,y=85)
tk.Button(app,text="submit",command=lambda:submit(lb1,lb2,lb3,lb4,lb5),width=10).place(x=200,y=120)
tk.Button(app,text="plot",command=plot,width=10).place(x=200,y=150)
tk.Button(app,text="New",command=new,width=10).place(x=200,y=180)
q1=tk.StringVar()
q1.set("")
lb1=tk.Label(app,textvariable=q1)
lb1.place(x=160,y=210)
q2=tk.StringVar()
q2.set("")
lb2=tk.Label(app,textvariable=q2)
lb2.place(x=160,y=240)
q3=tk.StringVar()
q3.set("")
lb3=tk.Label(app,textvariable=q3)
lb3.place(x=160,y=270)
q4=tk.StringVar()
q4.set("")
lb4=tk.Label(app,textvariable=q4)
lb4.place(x=160,y=300)
q5=tk.StringVar()
q5.set("")
lb5=tk.Label(app,textvariable=q5)
lb5.place(x=160,y=330)



app.mainloop()