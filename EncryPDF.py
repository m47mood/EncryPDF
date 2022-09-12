from tkinter import *
from tkinter import messagebox
import tkinter,time
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileWriter, PdfFileReader

# Developed by Mahmood AlShukri https://github.com/m47mood/EncryPDF/

def Enrypt(file):
    if file == '':
        messagebox.showinfo('Error 1','There was no file chosen.')
    else:
        pdfwriter=PdfFileWriter()
        try:
            pdf=PdfFileReader(file)
            for page_num in range(pdf.numPages):
                pdfwriter.addPage(pdf.getPage(page_num))
            passw=tkinter.simpledialog.askstring("Password", "Enter password:", show='*')
            pdfwriter.encrypt(passw)
            with open('Encrypted_'+ time.strftime("%d-%m-%Y-%H%M%S")+'.pdf','wb') as f:
                pdfwriter.write(f)
            messagebox.showinfo('Done!','The file is Encrypted')
        except :
            messagebox.showinfo('Error 2','Cannot read the file. \nMake sure the file exists in the path chosen.')
        else:
            pass
        


def Browse():
    global filepath
    filepath=askopenfilename()
    filelocEntry.insert(0,str(filepath))

   
main=Tk()
main.title("EncryPDF")
main.iconbitmap("EncryPDF.ico")
main.geometry('400x100')
main.resizable(False,False)
fileloclable=Label(main,text="PDF file location: ",anchor=W)
filelocEntry=Entry(main,width=50)
Browsebtn=Button(main,text="Browse",width=10,command=Browse)
Encryptbtn=Button(main,text="Encrypt PDF",command=lambda: Enrypt(filelocEntry.get()))
filelocEntry.grid(row=1,column=0,padx=5,pady=5)
fileloclable.grid(row=0,column=0,padx=5,sticky=W+E)
Browsebtn.grid(row=1,column=1)
Encryptbtn.grid(row=2,column=0)
main.mainloop()
