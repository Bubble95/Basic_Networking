import tkinter as tk
from tkinter import*
import networking
import pdb

m = tk.Tk() #where m is the name of the main window object
m.title('Client')

def file_request():
    #pdb.set_trace()
    textConsole.delete('1.0',END)
    c = networking.Client(entryAdrss.get(),int(entryPort.get()))      
    try:
        file = c.get_file()      
        textConsole.insert(INSERT, file['content'])
    except Exception as err:
        print(err)
        return
  
def close_server():
    textConsole.delete('1.0',END)
    c = networking.Client(entryAdrss.get(),int(entryPort.get()))
    try:
        c.close_server()
        textConsole.insert(INSERT, 'server  closed')
    except Exception as err:
        print(err)
        return
    
var = tk.StringVar()
entryAdrss = tk.Entry(m)
entryAdrss.grid(row = 0, column = 1,padx = 4, pady = 4)

entryPort = tk.Entry(m)
entryPort.grid(row = 1, column = 1,padx = 4, pady = 4)

labelAdrss = tk.Label(m, text = 'Adress')
labelAdrss.grid(row = 0, column = 0,padx = 4, pady = 4)

labelPort = tk.Label(m, text = 'Port')
labelPort.grid(row = 1, column = 0,padx = 4, pady = 4)

buttonCloseServer = tk.Button(m, text='close server',width=25,command=close_server)
buttonCloseServer.grid(row = 1, column = 3,padx = 4, pady = 4)


buttonSend = tk.Button(m, text='connect',width=25,command= file_request)
buttonSend.grid(row = 0, column = 3,padx = 4, pady = 4)

buttonDestroy = tk.Button(m, text='close',width=25,command=m.destroy)
buttonDestroy.grid(row = 4, column = 3,padx = 4, pady = 4)


textConsole = tk.Text(m,width = 45, height = 5)
textConsole.grid(row = 2, column = 0,padx = 0, pady = 4, columnspan = 2)



m.mainloop()
