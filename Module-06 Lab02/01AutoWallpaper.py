"""
problems:
Download and change desktop Wallpapers automitacally 
 """
import json
import requests
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')
# print(type(content))
# print(content)

# convert string to json
dict_content = json.loads(content)
# print(type(dict_content))
# get image url
img_url = dict_content['url']
# print(img_url)

# download image
res = requests.get(img_url)
# save the image
with open('apod.png','wb') as image:
    image.write(res.content)

# print(res)
