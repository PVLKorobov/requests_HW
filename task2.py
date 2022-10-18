from classes import YandexUploader


filename = "maxresdefault.jpg"
token = ""
with open("token.txt") as token_file:
    token = token_file.readline()
uploader = YandexUploader(token)
uploader.upload_file_to_disk("maxresdefault.jpg", "maxresdefault.jpg")