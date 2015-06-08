import requests
url = 'http://localhost/xampp/FYP/upload_file1.php'
files = {'file': open('image.jpg', 'rb')}
r = requests.post(url, files=files)
