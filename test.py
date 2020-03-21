from tkinter import *

root = Tk()

main_menu = Menu(root)
root.configure(menu=main_menu)

tab1 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=tab1)
tab1.add_command(label='New')
tab1.add_command(label='Exit')

tab2 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Edit', menu=tab2)
tab2.add_command(label='File1')
tab2.add_command(label='File2')



root.mainloop()
