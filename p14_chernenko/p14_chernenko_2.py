import json
#image_info_test-dev2017.json
#/home/kolya/Desktop/Studying/pythonHomeworks/p14_chernenko/image_info_test-dev2017.json
with open('/home/kolya/Desktop/Studying/pythonHomeworks/p14_chernenko/image_info_test-dev2017.json') as f:
    data = json.load(f)
    f.close()

images = data['images']
print("amount of pics: {0}".format(len(images)))
categor = data["categories"]
print("overall objects with attribute 'categories': {0}".format(len(categor)))
un_categor = []
for i in categor:
    if (i['supercategory'] not in un_categor):
        un_categor.append(i['supercategory'])
print("amount of unique categories used in dataset: {0}".format(len(un_categor)))
print("\n")
biggest = 0
inage = ''
for i in images:
    if int(i['id']) > biggest:
        biggest = int(i['id'])
        inage = i['file_name']
    
    if i['file_name'] == '000000000001.jpg':
        print("url: ", i["coco_url"])
        print("height: ", i['height'])
        print("width: ", i['width'])
        print("id: ", i["id"])
print("\n")    
print("Image with the biggest id value: {0}".format(inage))






















