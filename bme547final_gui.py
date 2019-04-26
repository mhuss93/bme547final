# BME547 Final Project
# Katrina Barth, Minhaj Hussain, and Iakov Rachinsky
# GUI Modules

from tkinter import *  # Brings in higher level tools
from tkinter import ttk  # Themed packages
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path


def main_window():
    root = Tk()
    root.title("Image Processor")
    root.grid_rowconfigure(9, weight=3)
    # Title message
    welcome_msg = ttk.Label(root, text="Welcome to the image processor!",
                            font=(20))
    welcome_msg.grid(column=0, row=0, columnspan=4, pady=15)
    # Frame for Image or Message Display
    img_frm = ttk.Frame(root, borderwidth=1, relief=GROOVE,
                        width=375, height=375)
    img_frm.grid(column=1, row=2, columnspan=3, rowspan=8, pady=5, ipady=5)
    img_frm.grid_propagate(0)
    img_obj = Image.open("Zoey.jpg")
    size = (375, 375)
    img_obj.thumbnail(size)
    img = ImageTk.PhotoImage(img_obj)
    img_space = ttk.Label(img_frm, image=img)
    img_space.grid(column=0, row=0, columnspan=3, rowspan=3)
    # img_frm.grid_rowconfigure(0, weight=1)  # Centering message in frame
    # img_frm.grid_rowconfigure(2, weight=1)
    # img_frm.grid_columnconfigure(0, weight=1)
    # img_frm.grid_columnconfigure(2, weight=1)
    # img_msg = ttk.Label(img_frm, text="No image file(s) selected")
    # img_msg.grid(column=0, row=1, columnspan=3)

    # Labels, boxes, and buttons for image file selection
    def open_file():
        open_file_adrs = filedialog.askopenfilename()
        open_file_box.insert(0, open_file_adrs)
        pass
    open_file_lbl = ttk.Label(root,
                              text="Select image file(s) for processing:")
    open_file_lbl.grid(column=0, row=1, pady=5, padx=10)
    open_file_adrs = StringVar()
    open_file_box = ttk.Entry(root, textvariable=open_file_adrs)
    open_file_box.config(width=50)
    open_file_box.grid(column=1, row=1, padx=5, columnspan=2)
    browse_btn = ttk.Button(root, text='Browse', command=open_file)
    browse_btn.grid(column=3, row=1)
    # Frame and radio buttons to choose image processing method
    proc_frm = ttk.Frame(root, borderwidth=1, relief=GROOVE)
    proc_frm.grid(column=0, row=3, pady=5, ipady=5)
    proc_lbl = ttk.Label(proc_frm, text="Select image processing method")
    proc_lbl.grid(column=0, row=0, pady=5)
    proc_choice = StringVar()
    proc_choice.set('Hist')
    proc_1 = ttk.Radiobutton(proc_frm, text="Histogram Equalization",
                             variable=proc_choice,
                             value='Hist')
    proc_1.grid(column=0, row=1, sticky=W, padx=20)
    proc_2 = ttk.Radiobutton(proc_frm, text="Contrast Stretching",
                             variable=proc_choice,
                             value='Stretch')
    proc_2.grid(column=0, row=2, sticky=W, padx=20)
    proc_3 = ttk.Radiobutton(proc_frm, text="Log Compression",
                             variable=proc_choice,
                             value='Compress')
    proc_3.grid(column=0, row=3, sticky=W, padx=20)
    proc_4 = ttk.Radiobutton(proc_frm, text="Reverse Video",
                             variable=proc_choice,
                             value='Reverse')
    proc_4.grid(column=0, row=4, sticky=W, padx=20)

    # Button to end image to server for processing and open up next window
    def img_proc():
        proc = proc_choice.get()
        print(proc)
        window2()
    proc_btn = ttk.Button(root, text="Process my image(s)",
                          command=img_proc)
    proc_btn.grid(column=0, row=9, sticky=N, pady=10)
    root.mainloop()
    return


def window2():
    window2 = Toplevel()
    window2.title("Processed Image Viewer")
    # Frame and Label for Original Image
    img1_lbl = ttk.Label(window2, text="Original Image",
                         font='Arial 10 bold')
    img1_lbl.grid(column=0, row=0, columnspan=4, pady=5)
    img1_frm = ttk.Frame(window2, borderwidth=1, relief=GROOVE,
                         width=375, height=375)
    img1_frm.grid(column=0, row=1, columnspan=4, rowspan=2, pady=5,
                  padx=5, ipady=5)
    img1_frm.grid_propagate(0)
    img1_obj = Image.open("Zoey.jpg")
    size = (375, 375)
    img1_obj.thumbnail(size)
    img1 = ImageTk.PhotoImage(img1_obj)
    img1_space = ttk.Label(img1_frm, image=img1)
    img1_space.grid(column=0, row=0)
    # Frame and Label for Processed Image
    img2_lbl = ttk.Label(window2, text="Processed Image",
                         font='Arial 10 bold')
    img2_lbl.grid(column=4, row=0, pady=5)
    img2_frm = ttk.Frame(window2, borderwidth=1, relief=GROOVE,
                         width=375, height=375)
    img2_frm.grid(column=4, row=1, rowspan=2, pady=5, padx=5, ipady=5)
    img2_frm.grid_propagate(0)
    img2_obj = Image.open("Zoey.jpg")
    img2_obj.thumbnail(size)
    img2 = ImageTk.PhotoImage(img2_obj)
    img2_space = ttk.Label(img2_frm, image=img2)
    img2_space.grid(column=0, row=0)
    # Frame for metadata
    data_frm = ttk.Frame(window2, borderwidth=1, relief=GROOVE,
                         width=200, height=95)
    data_frm.grid(column=5, row=1, columnspan=2, pady=5, padx=5, sticky=N)
    data_frm.grid_propagate(0)
    timestamp_lbl = ttk.Label(data_frm, text="Time of Upload:")
    timestamp_lbl.grid(column=0, row=0, pady=5, sticky=W)
    proctime_lbl = ttk.Label(data_frm, text="Time for Processing:")
    proctime_lbl.grid(column=0, row=1, pady=5, sticky=W)
    size_lbl = ttk.Label(data_frm, text="Image Size:")
    size_lbl.grid(column=0, row=2, pady=5, sticky=W)

    # Button to generate histogram of colors
    def gen_histo():
        window3()
    window2.grid_rowconfigure(2, weight=1)
    histo_btn = ttk.Button(window2,
                           text='Show Color Histograms',
                           command=gen_histo)
    histo_btn.grid(column=5, row=2, pady=10, columnspan=2, sticky=N)
    # Choose the save file type, with JPEG as default
    file_type = StringVar()
    file_type_lbl = ttk.Label(window2,
                              text="Select save file type:")
    file_type_lbl.grid(column=0, row=3, sticky=E, pady=5, padx=5)
    jpg_box = ttk.Radiobutton(window2, text='JPEG',
                              variable=file_type, value='.jpg')
    jpg_box.grid(column=1, row=3, padx=15, sticky=W)
    png_box = ttk.Radiobutton(window2, text='PNG',
                              variable=file_type, value='.png')
    png_box.grid(column=2, row=3, padx=15, sticky=W)
    tiff_box = ttk.Radiobutton(window2, text='TIFF',
                               variable=file_type, value='.tiff')
    tiff_box.grid(column=3, row=3, padx=15, sticky=W)
    file_type.set('.jpg')

    # Saving the processed image
    def save_file():
        save_file_adrs = filedialog.askopenfilename()
        save_file_box.insert(0, save_file_adrs)
        window2.lift()
        pass
    save_file_lbl = ttk.Label(window2, text="Save processed image as:")
    save_file_lbl.grid(column=0, row=4, sticky=E, pady=5, padx=5)
    save_file_adrs = StringVar()
    save_file_box = ttk.Entry(window2, textvariable=save_file_adrs)
    save_file_box.grid(column=1, row=4, columnspan=4, padx=5)
    save_file_box.config(width=105)
    browse_btn = ttk.Button(window2, text='Browse', command=save_file)
    browse_btn.grid(column=5, row=4, sticky=W)
    save_btn = ttk.Button(window2, text="Save Processed Image")
    save_btn.grid(column=6, row=4, pady=5, padx=5)
    # Close window button
    close_btn = ttk.Button(window2, text="Close Processed Image Viewer",
                           command=window2.destroy)
    close_btn.grid(column=0, row=5, columnspan=7, pady=10)
    window2.mainloop()
    return


def window3():
    window3 = Toplevel()
    window3.title("Histogram Viewer")
    # Frame and Label for Original Image Histogram
    histo1_label = ttk.Label(window3, text="Original Image",
                             font='Arial 10 bold')
    histo1_label.grid(column=0, row=0, pady=5)
    histo1_frm = ttk.Frame(window3, borderwidth=1, relief=GROOVE,
                           width=380, height=380)
    histo1_frm.grid(column=0, row=1, pady=5, padx=5)
    histo1_frm.grid_propagate(0)
    # Frame and Label for processed Image
    histo2_label = ttk.Label(window3, text="Processed Image",
                             font='Arial 10 bold')
    histo2_label.grid(column=1, row=0, pady=5)
    histo2_frm = ttk.Frame(window3, borderwidth=1, relief=GROOVE,
                           width=380, height=380)
    histo2_frm.grid(column=1, row=1,  pady=5, padx=5)
    histo2_frm.grid_propagate(0)
    # Close window button
    close_btn = ttk.Button(window3, text="Close Histogram Viewer",
                           command=window3.destroy)
    close_btn.grid(column=0, row=2, columnspan=2, pady=10)
    window3.mainloop()
    return


if __name__ == '__main__':
    main_window()
