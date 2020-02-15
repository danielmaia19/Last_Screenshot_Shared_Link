import glob, os, requests, base64, json, pyperclip, sys
from secrets import APIKEY

url = 'https://api.imgbb.com/1/upload?key=' + APIKEY

list_of_files = glob.glob('/Users/$HOME/Pictures/Screenshots/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

with open(latest_file, 'rb') as imageFile:
    str = base64.b64encode(imageFile.read())

r = requests.post(url, data={'image':str})

resp_dict = json.loads(r.text)
URL_VIEWER = resp_dict['data']['url_viewer']
pyperclip.copy(URL_VIEWER)
