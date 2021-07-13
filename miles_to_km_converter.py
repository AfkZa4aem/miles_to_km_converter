from tkinter import *


def mile_to_km():
    km = float(miles_entry.get())
    miles = "{:.1f}".format(km * 1.609)
    miles_count_label.config(text=f"{miles}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to", font=("Courier", 10, "normal"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=8)

miles_count_label = Label(text="0", font=("Courier", 10, "normal"))
miles_count_label.grid(column=1, row=1)
miles_count_label.config(pady=6)

km_label = Label(text="Km", font=("Courier", 10, "normal"))
km_label.grid(column=2, row=1)

miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Courier", 10, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=8)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)



























window.mainloop()