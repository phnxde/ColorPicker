import tkinter
import numpy


def make_white_to_transparent(image):
    array = numpy.array(image)
    mask = numpy.all(array == [255, 255, 255, 255], axis=-1)  # png without artefacts
    array[mask] = [255, 255, 255, 0]


# Window
root = tkinter.Tk()
root.geometry("720x480")
root.resizable(False, False)
root.overrideredirect(True)
root.configure(bg="#000000")

# Frame
control_bar = tkinter.Frame(root, height=30, bg="#15171c")
control_bar.pack(fill=tkinter.X)


# Sprites
s_quit = tkinter.PhotoImage(file="assets/quit.png")
print(s_quit.transparency_get(0, 0))


# Methods
def exit_root():
    root.quit()


# Elements
quit_button = tkinter.Button(control_bar, anchor="e", image=s_quit, command=exit_root, bd=0, highlightthickness=0, bg="#15171c", highlightcolor="#15171c")
quit_button.pack(side=tkinter.RIGHT, padx=5, pady=5)


# Main Loop
root.mainloop()
