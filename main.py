import tkinter as tk
import time

def saveBtn():
    f=open('Sample.txt','a')
    f.write('\n'+note+'    ')
    f.write(current_time)
    print("Note Saved")
    f.close()

def openBtn():
    f=open('Sample.txt','r')
    print(f.read())
    
    
current_time = time.asctime()


print("Welcome to Noty.You can now create sticky notes, easily.")
time.sleep(2)
note_input = input("Type your notes here: ")
note = ("*%s") % note_input
time.sleep(1)

    
    
root = tk.Tk()
root.title("Noty")
root.geometry("300x300")

tk.Label(root, text=current_time).pack()
    
tk.Label(root, text=note).pack()
    
btn = tk.Button(root, text="Save",bd='5',command=saveBtn)
btn.pack(side=tk.TOP)

btnopen=tk.Button(root,text="Open",bd='5',command=openBtn)
btnopen.pack(side=tk.TOP)

root.mainloop()
    

