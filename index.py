from email.mime import image
from optparse import Values
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0") #width and height (and x and y se kha se start ho raha hai)
        # fg means fore-ground-color(text color) bg means back-ground-color
        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM", bd=15,relief=RIDGE,bg='white',fg='darkgreen',font=("times new roman",50,"bold"),padx=2,pady=4)

        # to show label in window and side=TOP which assign lable in top and fill x which take lable whole in x direction
        lbltitle.pack(side=TOP,fill=X)
        img1=Image.open("C:\\Users\\Dell\\Desktop\\pharmacymanagement\\logo.jpg")
        # size ko define karne ke liye
        img1=img1.resize((80,80))
        self.photoimg1=ImageTk.PhotoImage(img1)

        # image ko display karne ke liye button use kar rahe hai
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=68,y=18)
        
# =================DATAFRAME============================================

        # relief ridge se hum log show karte hai partition ko
        DataFrame=Frame(self.root,bd=15,padx=20,relief=RIDGE)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        # here LabelFrame woth label is nothing but same as above difference is text wala area
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg='darkgreen',font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg='darkgreen',font=("arial",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)


# ==================ButtonDataFrame===============
        ButtonFrame=Frame(self.root,bd=15,padx=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)

#================Main Button==================
        btnAddDAta=Button(ButtonFrame,text="Medicine Add",bg='darkgreen',font=("arial",12,"bold"),fg="white")
        btnAddDAta.grid(row=0,column=0)

        btnAddDAta=Button(ButtonFrame,text="Update",bg='darkgreen',font=("arial",12,"bold"),fg="white")
        btnAddDAta.grid(row=0,column=1)

        btnAddDAta=Button(ButtonFrame,text="Delete",bg='red',font=("arial",12,"bold"),fg="white")
        btnAddDAta.grid(row=0,column=2)

        btnAddDAta=Button(ButtonFrame,text="Reset",bg='darkgreen',font=("arial",12,"bold"),fg="white")
        btnAddDAta.grid(row=0,column=3)

        btnAddDAta=Button(ButtonFrame,text="Exit",bg='darkgreen',font=("arial",12,"bold"),fg="white")
        btnAddDAta.grid(row=0,column=4)

# =============== Search By=========================

        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg='red',fg='white')
        lblSearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",13,"bold"))
        search_combo.grid(row=0,column=6)
        search_combo["values"]=("Ref","Medname","Lot")
         #current above tuple me se konsa lena hai wo baata ta hai 
        search_combo.current(0)



if __name__== "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()