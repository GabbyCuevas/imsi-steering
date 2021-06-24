from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("IMSI Steering command line generator")
root.geometry('400x400')


IPV4val = ["195.59.46.61","195.59.46.72","10.250.17.176","10.250.18.144","10.250.118.60","10.250.118.166","193.36.80.1","193.36.80.129"]


Label(root, text="BEGIMSI").grid(row=0, column=0)
begimsi = IntVar()
Entry(root, textvariable=begimsi).grid(row=0, column=1)


Label(root, text="ENDIMSI").grid(row=1, column=0)
endimsi = IntVar()
Entry(root,textvariable=endimsi).grid(row=1,column=1)


Label(root, text="APNNI").grid(row=2,column=0)
appni = Combobox(root)
appni['value']= ("*","EVERYWHERE", "IMS", "SOS", "EEZONE")
appni.insert(0,"Select APNNI")
appni.grid(row=2, column=1)


Label(root, text="IPV4").grid(row=3,column=0)
IPV4 = Combobox(root)
IPV4['value']= ("UGW901XWP","UGW902XWP","UGW903XWP","UGW904XWP","CGW1","CGW3","SCC01XWPMMK01","SCC03BDPMMK01")
IPV4.insert(0,"Select IPV4")
IPV4.grid(row=3, column=1,)


Label(root, text="Command Line").grid(row=4, column=0)
commandLine = StringVar()
Label(root, textvariable=commandLine).grid(row=4, column=1)


quitButton = Button(root, text="Quit", command=root.destroy)
quitButton.grid(row=5, column=1)


root.mainloop()
