

# Extensions - alternative shown by the AI bot
# Uses a dictionary
# Andrew Waddington

ext = input("File name: ").lower().strip()

media_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Extract the file extension
file_extension = ext[ext.rfind("."):]

# Print the corresponding media type or default
print(media_types.get(file_extension, "application/octet-stream"))
