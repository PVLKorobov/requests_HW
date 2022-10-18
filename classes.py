import pip._vendor.requests as requests

class YandexUploader:
    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        return {"Content-Type": "application/json", "Authorization": f"OAuth {self.token}"}
    
    def get_upload_link(self, disk_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()
    
    def upload_file_to_disk(self, disk_path, filename):
        href = self.get_upload_link(disk_path)["href"]
        response = requests.put(href, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл загружен на Яндекс Диск")