import requests  
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD



embed = ""
embed_copy = ""
title = ""

def upload_file(reqtype, filePath):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype" : reqtype}

    with open(filePath, "rb") as f: 
        files = {"fileToUpload" : f}  
        res = requests.post(url, data=data, files=files)    

    return res.text
def file_drop(event):
    rawData = event.data
    file_path = root.tk.splitlist(event.data)
    if file_path:
        embed = upload_file("fileupload", file_path[0])
        title = title_var.get()
        embed_copy = f"[{title}]({embed})" 
        root.clipboard_clear()
        root.clipboard_append(embed_copy)
        root.update()
        file_title.delete(0, tk.END)
        print(embed_copy)     
         
    
root = TkinterDnD.Tk()
root.geometry("500x300")
root.configure(bg="#ecbae8")
title_var = tk.StringVar()
root.title("catbox py tool")
label = tk.Label(root, text = "title of the clip :3 !!!", font=("Arial", 20))
label.pack(pady=10)
file_title = tk.Entry(root, textvariable= title_var, width=50, font=("Arial", 10))
file_title.pack(pady=20)
label2 = tk.Label(root, text = "drag clip anywhere in window.", font=("Arial", 15))
label2.pack(pady=70)
label3 = tk.Label(root, text = "(embed link will automatically copy to clipboard)", font=("Arial", 15))
label3.pack(pady=90)
#copy_button = tk.Button(root, text="copy embed", command=copy_embed, bg="#E19FF1", fg="white", padx=10)
#copy_button.pack(pady=10)
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', file_drop)

root.mainloop()
