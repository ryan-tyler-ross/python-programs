"""Common Tkinter widgets with callbacks that print their values."""

from tkinter import (
    END, Button, Checkbutton, Entry, IntVar, Label, Listbox,
    Radiobutton, Scale, Spinbox, Text, Tk,
)


def main():
    window = Tk()
    window.title("Widget Examples")
    window.minsize(width=500, height=500)

    Label(window, text="Tkinter widget reference").pack()

    entry = Entry(window, width=30)
    entry.insert(END, "Example text")
    entry.pack()
    Button(window, text="Read entry", command=lambda: print(entry.get())).pack()

    text = Text(window, height=5, width=30)
    text.insert(END, "Example of multi-line text entry.")
    text.pack()
    Button(window, text="Read text", command=lambda: print(text.get("1.0", END))).pack()

    spinbox = Spinbox(window, from_=0, to=10, width=5,
                      command=lambda: print(spinbox.get()))
    spinbox.pack()
    Scale(window, from_=0, to=100, command=lambda value: print(value)).pack()

    checked_state = IntVar(window)
    Checkbutton(window, text="Enabled", variable=checked_state,
                command=lambda: print(checked_state.get())).pack()

    radio_state = IntVar(window)
    for value in (1, 2):
        Radiobutton(window, text=f"Option {value}", value=value,
                    variable=radio_state, command=lambda: print(radio_state.get())).pack()

    listbox = Listbox(window, height=4)
    for item in ("Apple", "Pear", "Orange", "Banana"):
        listbox.insert(END, item)
    listbox.pack()

    def show_selection(_event):
        selection = listbox.curselection()
        if selection:
            print(listbox.get(selection[0]))

    listbox.bind("<<ListboxSelect>>", show_selection)
    window.mainloop()


if __name__ == "__main__":
    main()
