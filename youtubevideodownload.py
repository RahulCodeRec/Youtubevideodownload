import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def download_video(video_url, download_path):
    """
    Downloads a YouTube video using yt-dlp to the specified location.

    Parameters:
        video_url (str): The URL of the YouTube video to download.
        download_path (str): The folder where the video should be saved.
    """
    try:
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # yt-dlp command
        command = [
            'yt-dlp',
            '-o', os.path.join(download_path, '%(title)s.%(ext)s'),
            video_url
        ]

        # Execute the command
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Download completed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def browse_folder():
    """Opens a dialog to select a folder."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_path_entry.delete(0, tk.END)
        download_path_entry.insert(0, folder_selected)


def start_download():
    """Starts the video download process."""
    video_url = url_entry.get().strip()
    download_path = download_path_entry.get().strip()

    if not video_url:
        messagebox.showwarning("Input Error", "Please enter a YouTube video URL.")
        return
    if not download_path:
        messagebox.showwarning("Input Error", "Please select a download folder.")
        return

    download_video(video_url, download_path)


# Create the main application window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("600x400")

# Background color (instead of image)
root.configure(bg="lightblue")

# YouTube URL input
url_label = tk.Label(root, text="YouTube Video URL:", font=("Arial", 12), bg="lightblue")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

# Destination folder selector
download_path_label = tk.Label(root, text="Select Download Folder:", font=("Arial", 12), bg="lightblue")
download_path_label.pack(pady=10)
download_path_frame = tk.Frame(root, bg="lightblue")
download_path_frame.pack(pady=5)
download_path_entry = tk.Entry(download_path_frame, width=40, font=("Arial", 12))
download_path_entry.pack(side=tk.LEFT, padx=5)
browse_button = tk.Button(download_path_frame, text="Browse", command=browse_folder, font=("Arial", 10))
browse_button.pack(side=tk.LEFT)

# Download button
download_button = tk.Button(root, text="Download Video", command=start_download, font=("Arial", 14), bg="green",
                            fg="white")
download_button.pack(pady=20)

# Run the application
root.mainloop()
