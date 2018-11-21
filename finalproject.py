# Importing Necessary Libraries
from tkinter import *
from tkinter import messagebox
import csv
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Reading CSV File
df=pd.read_csv('pythonproject.csv', index_col=False) # With Pandas


with open('pythonproject.csv', newline='') as f:    # With CSV
    reader = csv.reader(f)
    content1 = list(reader)
    
#print("content1 is",content1)
flag=0

# Creating Class 
class Interface:
    
    def __init__(self, master):   # Init Function
        self.master = master
        master.title('Student Record Manager')

        #Declaration of Variables used in  Entry Widget
        Roll_No = StringVar()
        Name = StringVar()
        Email = StringVar()
        Python_Marks = StringVar()
        ADBMS_Marks = StringVar()      
        DS_Marks = StringVar()
        Section = StringVar()
        Year = StringVar()
        Mobile = StringVar()
        State = StringVar()
         
# Creating My GUI

        #Frame
        self.f1 = Frame(self.master, bg="#FFFFFF").grid()
                          
        #Labels For Various Enteries
        l1 =  Label(self.f1, text = "Roll No. Of Student : ",bd=5).grid(row = 0, column = 0)
        l2 =  Label(self.f1, text = "Name Of Student : ",bd=5).grid(row = 3, column = 0)
        l3 =  Label(self.f1, text = "Email ID Of Student : ",bd=5).grid(row = 4, column = 0)
        l4 =  Label(self.f1, text = "Python Marks Of Student : ",bd=5).grid(row = 5, column = 0)
        l5 =  Label(self.f1, text = "ADBMS Marks Of Student : ",bd=5).grid(row = 6, column = 0)
        l6 =  Label(self.f1, text = "DS Marks Of Student : ",bd=5).grid(row = 7, column = 0)
        l7 =  Label(self.f1, text = "Section Of Student : ",bd=5).grid(row = 8, column = 0)
        l8 =  Label(self.f1, text = "Year Of Student : ",bd=5).grid(row = 9, column = 0)
        l9 =  Label(self.f1, text = "Mobile Of Student : ",bd=5).grid(row = 10, column = 0)
        l10 = Label(self.f1, text = "State Of Student : ",bd=5).grid(row = 11, column = 0)


        #Entry Widget 
        e1 = Entry(self.f1, textvariable = Roll_No,bd=5).grid(row = 0, column = 1)
        e2 = Entry(self.f1, textvariable = Name,bd=5).grid(row = 3, column = 1)
        e3 = Entry(self.f1, textvariable = Email,bd=5).grid(row = 4, column = 1)
        e4 = Entry(self.f1, textvariable = Python_Marks,bd=5).grid(row = 5, column = 1)
        e5 = Entry(self.f1, textvariable = ADBMS_Marks,bd=5).grid(row = 6, column = 1)
        e6 = Entry(self.f1, textvariable = DS_Marks,bd=5).grid(row = 7, column = 1)
        e7 = Entry(self.f1, textvariable = Section,bd=5).grid(row = 8, column = 1)
        e8 = Entry(self.f1, textvariable = Year,bd=5).grid(row = 9, column = 1)
        e9 = Entry(self.f1, textvariable = Mobile,bd=5).grid(row = 10, column = 1)
        e10 = Entry(self.f1, textvariable = State,bd=5).grid(row = 11, column = 1)

                 
#Function To Check Whether A Record Exist Or Not
        def check(event):
            searchThis=Roll_No.get() # Stores The Roll No. That User Wanna Check
            print(searchThis) # Just For Checking Purpose
            msg=StringVar()
            msg2=StringVar()
            for i in range(0,len(content1)): # Loop To Check In CSV
                if(content1[i][0]==searchThis):
                    flag=1
                    m=Message(inf,textvariable=msg) # Message Box Pop Up When Record Found
                    msg.set("RECORD FOUND")
                    m.grid(row=2,column=3,columnspan=2)
                    break
                else:
                    flag=0
        
            if(flag==0):
                m2=Message(inf,textvariable=msg2)
                msg2.set("   RECORD NOT FOUND")  # Message Box Pop Up When Record Not Found
                m2.grid(row=2,column=3,columnspan=2)
             
 # Function To Close GUI            
        def close(event):
            master.destroy()

# Function To Add New Record In Data
        def save(event):
            data = [[Roll_No.get(), Name.get(), Email.get(),  # Data Retrieval From Tkinter
                     Python_Marks.get(),ADBMS_Marks.get(), DS_Marks.get(),
                     Section.get(), Year.get(),Mobile.get(), State.get()]]
    
            df1 = pd.DataFrame(data, columns =[Roll_No, Name, Email, Python_Marks,
                                               ADBMS_Marks,DS_Marks, Section,
                                               Year, Mobile, State])
        # Addition Of Record In CSV    
            df1.to_csv("pythonproject.csv", mode='a', index=False,header=False)
            msg3=StringVar()
            m3=Message(inf,textvariable=msg3) #Message Box Pop To Inform User
            msg3.set("RECORD ADDED IN DATA")
            m3.grid(row=11,column=3,columnspan=2)
            #print(data)
 
# Function To Calculate Average           
        def average(event):
            avg=df["Total_Marks"].mean()
            msg4=IntVar()
            m4=Message(inf,textvariable=msg4) # Message To Display Average
            msg4.set(avg)
            m4.grid(row=15,column=0)
            
# Function To Calculate Mode            
        def mode(event):
            mod=df["Total_Marks"].mode()
            msg5=IntVar()
            m5=Message(inf,textvariable=msg5) # Message To Display Mode
            msg5.set(mod)
            m5.grid(row=15,column=1)
            
# Function To Calculate Median           
        def median(event):
            med=df["Total_Marks"].median()
            msg6=IntVar()
            m6=Message(inf,textvariable=msg6) # Message To Display Median
            msg6.set(med)
            m6.grid(row=15,column=2)

# Function To Calculate Lowest Marks In Python                    
        def pylow(event):
            pyl=df["Python_Marks"].min() 
            msg7=IntVar()
            m7=Message(inf,textvariable=msg7) # Message To Display Lowest Marks In Py
            msg7.set(pyl)
            m7.grid(row=17,column=0)
            
# Function To Calculate Lowest Marks In DS                    
        def dslow(event):
            dsl=df["DS_Marks"].min()
            msg8=IntVar()
            m8=Message(inf,textvariable=msg8) # Message To Display Lowest Marks In DS
            msg8.set(dsl)
            m8.grid(row=17,column=1)
            
# Function To Calculate Lowest Marks In ADBMS                    
        def adbmslow(event):
            adbl=df["ADBMS_Marks"].min() # Message To Display Lowest Marks In ADBMS
            msg9=IntVar()
            m9=Message(inf,textvariable=msg9)
            msg9.set(adbl)
            m9.grid(row=17,column=2)
            
 # Function To Calculate Highest Marks In Python                       
        def pyhigh(event):
            pyh=df["Python_Marks"].max() # Message To Display Highest Marks In Py
            msg10=IntVar()
            m10=Message(inf,textvariable=msg10)
            msg10.set(pyh)
            m10.grid(row=19,column=0)
            
 # Function To Calculate Highest Marks In DS                               
        def dshigh(event):
            dsh=df["DS_Marks"].max()
            msg11=IntVar()
            m11=Message(inf,textvariable=msg11) # Message To Display Highest Marks In DS
            msg11.set(dsh)
            m11.grid(row=19,column=1)
            
 # Function To Calculate Highest Marks In ADBMS                          
        def adbmshigh(event):
            adbh=df["ADBMS_Marks"].max()
            msg12=IntVar()
            m12=Message(inf,textvariable=msg12) # Message To Display Highest Marks In ADBMS
            msg12.set(adbh)
            m12.grid(row=19,column=2)
   
# Function For First Graph          
        def graph1(event):
            x=df["Name"]
            y=df["Total_Marks"]
            g1=Tk()
            figure = plt.Figure(figsize=(12,6), dpi=100) # Calling Figure
            ax = figure.add_subplot(111) # Plotting Bar Graph
            chart_type = FigureCanvasTkAgg(figure, g1)
            chart_type.get_tk_widget().pack(side = LEFT ,fill = BOTH) # Positioning
            df.plot(kind='bar',x="Name",y= "Total_Marks" ,ax=ax)
            ax.set_title('Student Wise Total Marks')# Setting title of graph
            g1.mainloop()
            
        def graph2(event):
            g2=Tk()
            x=df["Name"]
            figure = plt.Figure(figsize=(12,5), dpi=100) # Calling Figure
            ax2 = figure.add_subplot(111) # Plotting Mutiple Line Graph
            chart_type = FigureCanvasTkAgg(figure, g2)
            chart_type.get_tk_widget().pack(side = LEFT ,fill = BOTH) # Positioning
            df.plot(kind='line',x="Name",y= "Python_Marks" ,legend=True,ax=ax2) # line 1
            df.plot(kind='line',x="Name",y= "ADBMS_Marks" ,legend=True,ax=ax2) # line 2
            df.plot(kind='line',x="Name",y= "DS_Marks" ,legend=True,ax=ax2) # line 3
            ax2.set_title('Student\'s Marks In Respective Subjects') # Setting title of graph
            g2.mainloop()
            
        def graph3(event):
            g3=Tk()
            figure = plt.Figure(figsize=(11,5), dpi=100) # Calling Figure
            ax3 = figure.add_subplot(111) # Plotting Scatter Graph
            chart_type = FigureCanvasTkAgg(figure, g3)
            chart_type.get_tk_widget().pack(side = LEFT ,fill = BOTH) # Positioning
            df.plot(kind='scatter',x="Average_Marks",y="Total_Marks",legend=True,ax=ax3,color='g')
            ax3.set_xlabel('Average Marks')
            ax3.set_ylabel('Total Marks')
            ax3.set_title('Total Marks V/S Average Marks') # Setting title of graph
            plt.style.use('seaborn-notebook') # Styling Of Graph
            g3.mainloop()
            
        #Buttons
        exit_button = Button(self.f1,text="Exit",width=15,bd=5)
        exit_button.grid(row = 13, column = 0) # Positioning
        exit_button.bind("<Button-1>", close) # Binding
        
        check_button = Button(self.f1,text="Check Record",bd=5)
        check_button.grid(row = 2, column = 2) # Positioning
        check_button.bind("<Button-1>", check) # Binding
        
        add_button = Button(self.f1,text="Add Record",bd=5)
        add_button.grid(row = 12, column = 2) # Positioning
        add_button.bind("<Button-1>", save) # Binding
        
        mean_button = Button(self.f1,text="Average Marks",bd=5,fg = 'blue')
        mean_button.grid(row=14,column=0) # Positioning
        mean_button.bind("<Button-1>", average) # Binding
        
        mode_button = Button(self.f1,text="Mode Of Marks",bd=5,fg = 'red')
        mode_button.grid(row=14,column=1) # Positioning
        mode_button.bind("<Button-1>", mode) # Binding
        
        median_button = Button(self.f1,text="Median Marks",bd=5,fg = 'blue')
        median_button.grid(row=14,column=2) # Positioning
        median_button.bind("<Button-1>", median) # Binding
        
        pylow_button = Button(self.f1,text="Lowest In Py",bd=5,fg = 'red')
        pylow_button.grid(row=16,column=0) # Positioning
        pylow_button.bind("<Button-1>", pylow) # Binding
        
        pyhigh_button = Button(self.f1,text="Highest In Py",bd=5,fg = 'blue')
        pyhigh_button.grid(row=18,column=0) # Positioning
        pyhigh_button.bind("<Button-1>", pyhigh) # Binding
        
        dslow_button = Button(self.f1,text="Lowest In DS",bd=5,fg = 'blue')
        dslow_button.grid(row=16,column=1) # Positioning
        dslow_button.bind("<Button-1>", dslow) # Binding
        
        dshigh_button = Button(self.f1,text="Highest In DS",bd=5,fg = 'red')
        dshigh_button.grid(row=18,column=1) # Positioning
        dshigh_button.bind("<Button-1>", dshigh) # Binding
        
        adbmslow_button = Button(self.f1,text="Lowest In ADBMS",bd=5,fg = 'red')
        adbmslow_button.grid(row=16,column=2) # Positioning
        adbmslow_button.bind("<Button-1>", adbmslow) # Binding
        
        adbmshigh_button = Button(self.f1,text="Highest In ADBMS",bd=5,fg = 'blue')
        adbmshigh_button.grid(row=18,column=2) # Positioning
        adbmshigh_button.bind("<Button-1>", adbmshigh) # Binding
        
        graph_button = Button(self.f1 , text = "Plot Graph 1",fg = 'red',bg = 'white',bd=5, relief = RAISED)
        graph_button.grid(row=20,column=0) # Positioning
        graph_button.bind("<Button-1>", graph1)  # Binding
        
        graph_button2 = Button(self.f1 , text = "Plot Graph 2",fg = 'blue',bg = 'white',bd=5, relief = RAISED)
        graph_button2.grid(row=20,column=1) # Positioning
        graph_button2.bind("<Button-1>", graph2) # Binding

        graph_button3 = Button(self.f1 , text = "Plot Graph 3",fg = 'red',bg = 'white',bd=5, relief = RAISED)
        graph_button3.grid(row=20,column=2) # Positioning
        graph_button3.bind("<Button-1>", graph3) # Binding
        
        

                     
inf = Tk() 
obj = Interface(inf) # Object Of GUI 
inf.mainloop()     # Mainloop Of GUI         
             
             
             
             
             
             
             