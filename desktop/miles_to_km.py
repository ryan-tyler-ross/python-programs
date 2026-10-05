"""Convert miles to kilometers in a small Tkinter window."""

from tkinter import Button, Entry, Label, Tk

MILES_TO_KM = 1.609344


def main():
    window = Tk()
    window.title("Miles to KM Converter")
    window.minsize(width=300, height=100)
    window.config(padx=20, pady=20)

    miles_input = Entry(window, width=7)
    miles_input.grid(column=1, row=0)
    Label(window, text="Miles").grid(column=2, row=0)
    Label(window, text="is equal to").grid(column=0, row=1)

    result_label = Label(window, text="0")
    result_label.grid(column=1, row=1)
    Label(window, text="Km").grid(column=2, row=1)

    def convert():
        try:
            miles = float(miles_input.get())
        except ValueError:
            result_label.config(text="Enter a number")
            return
        result_label.config(text=f"{miles * MILES_TO_KM:.2f}")

    Button(window, text="Calculate", command=convert).grid(column=1, row=2)
    window.mainloop()


if __name__ == "__main__":
    main()
