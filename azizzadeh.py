import tkinter as tk 


def calculate(): 
    mizan_balance = float(entry1.get()) 
    mizan_risk = float(entry2.get()) 
    peak_stop = float(entry3.get()) 
    total = ((((mizan_risk * mizan_balance) / 100) / peak_stop) / 10) 
    
    result_label.config(text=f"{total} Lot") 

root = tk.Tk() 
root.title("آکادمی فارکس بوشهر")
label1 = tk.Label(root, text="$ میزان بلنس", font=("Arial", 13))
label1.pack() 
entry1 = tk.Entry(root) 
entry1.pack() 
label2 = tk.Label(root, text="درصد میزان ریسک", font=("Arial", 13))
label2.pack() 
entry2 = tk.Entry(root) 
entry2.pack()
label3 = tk.Label(root, text="مقدار استاپ", font=("Arial", 13))
label3.pack() 
entry3 = tk.Entry(root) 
entry3.pack() 
check_button = tk.Button(root, text="محاسبه", command=calculate) 
check_button.pack() 
result_label = tk.Label(root, text="", font=("Arial", 13)) 
result_label.pack() 
bottom_text = tk.Label(root, text="https://t.me/dailytrade70 پشتیبانی کانال فارکس", width=0, height=10) 
bottom_text.place(relx=100, rely=100, anchor ='n')
bottom_text.pack() 

root.geometry("450x450")
root.minsize(300, 300)
root.maxsize(600, 600)  


root.mainloop()

