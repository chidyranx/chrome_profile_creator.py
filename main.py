import os
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox

def create_chrome_profiles():
    base_name = entry_base_name.get()
    num_profiles = int(entry_num_profiles.get())
    folder_name = entry_folder_name.get()
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop', folder_name)

    # Create the folder on the desktop if it doesn't exist
    os.makedirs(desktop_path, exist_ok=True)

    for i in range(1, num_profiles + 1):
        profile_directory = f"{base_name}_{i}"
        create_desktop_shortcut(base_name, i, desktop_path)

    messagebox.showinfo("Profiles Created", f"{num_profiles} profiles created successfully!")

def create_desktop_shortcut(base_name, profile_number, desktop_path):
    # Path to the Chrome executable
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Path to the shortcut file
    shortcut_file = os.path.join(desktop_path, f'{base_name}_{profile_number}.lnk')

    # Create a shortcut to Chrome with the specified profile
    with open('ChromeProfile.vbs', 'w') as vbs_file:
        vbs_file.write(f'Set objShell = WScript.CreateObject("WScript.Shell")\n')
        vbs_file.write(f'strPath = "{chrome_path}"\n')
        vbs_file.write(f'strArgs = "--profile-directory={base_name}_{profile_number}"\n')
        vbs_file.write(f'Set objLink = objShell.CreateShortcut("{shortcut_file}")\n')
        vbs_file.write(f'objLink.TargetPath = strPath\n')
        vbs_file.write(f'objLink.Arguments = strArgs\n')
        vbs_file.write('objLink.Save\n')

    # Run the VBS script to create the shortcut
    subprocess.run(['wscript', 'ChromeProfile.vbs'])

    # Delete the temporary VBS script
    os.remove('ChromeProfile.vbs')

# Create the main application window with dimensions 400x400
root = tk.Tk()
root.title("Chrome Profile Creator")
root.geometry("400x400")

# Set the background color to green
root.configure(bg="white")

# Create a card-like frame
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10, borderwidth=2, relief="groove")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Label and entry for base name of profiles
label_base_name = tk.Label(frame, text="Base Name for Profiles:", font=("Arial", 10), bg="lightgray")
label_base_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_base_name = tk.Entry(frame, font=("Arial", 10))
entry_base_name.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Horizontal line
line1 = tk.Frame(frame, height=1, width=300, bg="gray")
line1.grid(row=1, columnspan=2)

# Label and entry for the number of profiles
label_num_profiles = tk.Label(frame, text="Number of Profiles:", font=("Arial", 10), bg="lightgray")
label_num_profiles.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_num_profiles = tk.Entry(frame, font=("Arial", 10))
entry_num_profiles.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Horizontal line
line2 = tk.Frame(frame, height=1, width=300, bg="gray")
line2.grid(row=3, columnspan=2)

# Label and entry for the folder name on the desktop
label_folder_name = tk.Label(frame, text="Folder Name on Desktop:", font=("Arial", 10), bg="lightgray")
label_folder_name.grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_folder_name = tk.Entry(frame, font=("Arial", 10))
entry_folder_name.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Horizontal line
line3 = tk.Frame(frame, height=1, width=300, bg="gray")
line3.grid(row=5, columnspan=2)

# Button to create profiles
create_button = tk.Button(frame, text="Create Profiles", command=create_chrome_profiles, font=("Arial", 12, "bold"), bg="green", fg="white")
create_button.grid(row=6, columnspan=2, pady=20)

# Copyright and company information label
copyright_label = tk.Label(root, text="© 2023 AlifBot | Website: www.alifbot.com", font=("Arial", 8), fg="red", bg="white")
copyright_label.pack(side="bottom", anchor="w", padx=20, pady=5)

# Run the Tkinter main loop
root.mainloop()
