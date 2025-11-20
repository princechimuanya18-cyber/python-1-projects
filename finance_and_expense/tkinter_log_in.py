import tkinter as tk

root = tk.Tk()

root.geometry("500x500")

root.title("Login windows")

label = tk.Label(root, text=("Log in page"), font=("Times New Roman", 18), fg="blue")
label.pack()



button_1 = tk.Button(root, text=("Login"), font=("Times New Roman", 15), bg="blue")
button_1.pack(side=tk.RIGHT)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.pack(padx=10, pady=80)

btn_1 =tk.Button(buttonframe, font=("Times New Roman", 15), text="boy")
btn_1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn_2 =tk.Button(buttonframe, font=("Times New Roman", 15), text="girl")
btn_2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn_3 =tk.Button(buttonframe, font=("Times New Roman", 15), text="man")
btn_3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn_4 =tk.Button(buttonframe, font=("Times New Roman", 15), text="mango")
btn_4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn_5 =tk.Button(buttonframe, font=("Times New Roman", 15), text="Banana")
btn_5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn_6 =tk.Button(buttonframe, font=("Times New Roman", 15), text="apple")
btn_6.grid(row=1, column=2, sticky=tk.W + tk.E)

btn_7 =tk.Button(buttonframe, font=("Times New Roman", 15), text="dollars")
btn_7.grid(row=2, column=0, sticky=tk.W + tk.E)

btn_8 =tk.Button(buttonframe, font=("Times New Roman", 15), text="naira")
btn_8.grid(row=2, column=1, sticky=tk.W + tk.E)

btn_9 =tk.Button(buttonframe, font=("Times New Roman", 15), text="pounds")
btn_9.grid(row=2, column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill="x")

button_2 =tk.Button(root, text="input", font=("Times New Roman", 15))
button_2.place(x=200, y=400, height=50, width=50)


def create_shapes_on_canvas():
    # 1. Create the main window
    root = tk.Tk()
    root.title("Tkinter Canvas Example")

    # 2. Create a Canvas widget
    # Define the dimensions and background color
    canvas_width = 300
    canvas_height = 200
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=10, pady=10)

    # 3. Draw a rectangle (top-left, bottom-right corners specified)
    # Coordinates: (50, 50) to (250, 150)
    canvas.create_rectangle(50, 50, 250, 150, fill="green", outline="black")

    # 4. Draw an oval (defined by the bounding box of a rectangle)
    # Coordinates: (100, 80) to (200, 120)
    canvas.create_oval(100, 80, 200, 120, fill="blue", outline="white")

    # 5. Add text to the canvas (centered at the given coordinates)
    canvas.create_text(canvas_width/2, 20, text="Canvas Shapes", font=("Helvetica", 16))

    # 6. Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_shapes_on_canvas()

root.mainloop()