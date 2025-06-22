"""
implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

file = input("Enter filename with extension: ")
formatted_filename = file.strip(" ").lower()
jpeg_extensions = ["jpg", "jpeg"]
image_extensions = ["gif", "png"]
app_extensions = ["pdf", "zip"]
text_extension =  ["txt"]
file_extension = formatted_filename.split(".")[-1].lower()


if file_extension in image_extensions:
    print(("image/"+file_extension).strip().strip("\n"))
elif file_extension in jpeg_extensions:
    print("image/jpeg")
elif file_extension in app_extensions:
    print(("application/"+file_extension).strip())
elif file_extension in text_extension:
    print("text/plain")
else:
    print("application/octet-stream")