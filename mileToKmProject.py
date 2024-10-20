import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=284,height=100)
window.config(padx=50,pady=5,bg="#FEC7B4")

def convert():
    value = float(inpt.get())*1.609
    converted_value.config(text=round(value,3))



my_lable = tkinter.Label(text="is equal to",bg="#FEC7B4")
my_lable.grid(column=0,row=1)
# my_lable.config(padx=50, pady=50)

inpt = tkinter.Entry(width=5,bg="#FEC7B4")
inpt.grid(column=1,row=0)


mile = tkinter.Label(text="Miles",bg="#FEC7B4")
mile.grid(column=2,row=0)
mile.config(padx=5,pady=5)

converted_value = tkinter.Label(text="0",bg="#FEC7B4")
converted_value.grid(column=1,row=1)
converted_value.config(padx=5,pady=0)

button = tkinter.Button(text="Calculate", command=convert,bg="#FEC7B4")
button.grid(column=1,row=2)

km = tkinter.Label(text="Km",bg="#FEC7B4")
km.grid(column=2,row=1)

window.mainloop()