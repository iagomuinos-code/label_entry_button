import tkinter as tk

#creating window 
window = tk.Tk()

window.geometry("800x400")
window.title("Basic Widgets")
window.config(bg= "lightblue")

#label
name_label = tk.Label(window, text= "Please enter your name.",
                        bg= "lightyellow", fg="darkblue",
                        width= 50, height= 2,font=("Helvetica",18))
name_label.pack( pady= 5)

#entry widget
name_entry = tk.Entry(window, bg= "red", fg="lightgreen")
name_entry.pack(pady= 10)

close_button= tk.Button(window, text="Press this if you wish to close",
                        width=54, height =4, command= window.destroy)
close_button.pack(pady=5)




# last instruction to keep window running
window.mainloop()