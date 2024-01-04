import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def download():
    link = add.get()

    try:
        response = requests.get(link)
        response.raise_for_status()

        # Open the downloaded image using PIL
        img = Image.open(BytesIO(response.content))

        # Save the image
        img.save("image.jpg")

        # Display the image
        tk_img = ImageTk.PhotoImage(img)
        ilabel.config(image=tk_img)
        ilabel.image = tk_img

        # Reset the warning label after successful download
        invalid_url_label.config(text="")
    except requests.exceptions.RequestException as e:
        # Display a warning message if the URL is not valid or download fails
        invalid_url_label.config(text="Invalid URL or download error. Please check the URL and try again.", foreground="red")

def ui():
    # Creating the main window
    root = tk.Tk()
    root.title("Image Downloader")
    root.geometry("600x450")  # Set a fixed size for the window

    # Top frame for the title
    tframe = tk.Frame(root, background="#4CAF50", height=100)
    tframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Title label
    title = tk.Label(tframe, text="Image Downloader", foreground="white", height=2, font="Arial 20 bold", background="#4CAF50", padx=10, pady=10)
    title.pack()

    # Middle frame for the entry and download button
    dframe = tk.Frame(root, height=200, background="#E1EFFF")
    dframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Description label
    desc = tk.Label(dframe, text="Enter image address", font="arial 14", padx=10, pady=10, background="#E1EFFF")
    desc.grid(row=0, column=0)

    # Entry for image address
    global add  # Make add a global variable to be accessible in other functions
    add = tk.Entry(dframe, font="arial 14", width=30)
    add.grid(row=0, column=1, padx=10, pady=10)

    # Download button
    btn_download = tk.Button(dframe, text="Download", command=download, bg="#4CAF50", fg="white", padx=10, pady=10)
    btn_download.grid(row=1, column=0, columnspan=2, pady=10)

    # Warning label for invalid URL
    global invalid_url_label
    invalid_url_label = tk.Label(dframe, text="", font="arial 12", foreground="red", background="#E1EFFF")
    invalid_url_label.grid(row=2, column=0, columnspan=2, pady=5)

    # Exit button
    btn_exit = tk.Button(root, text="Exit", command=root.destroy, bg="#FF6347", fg="white", padx=10, pady=10)
    btn_exit.pack(side=tk.BOTTOM, padx=10, pady=10)

    # Call down() initially to create the frame for the image
    down_image = ImageTk.PhotoImage(Image.new("RGB", (400, 400), "white"))  # Placeholder image
    global ilabel  # Make ilabel a global variable
    ilabel = tk.Label(root, image=down_image)
    ilabel.image = down_image
    ilabel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Start the Tkinter main loop
    root.mainloop()

# Call the ui() function to start the application
ui()
