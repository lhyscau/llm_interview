import re
import requests
import os
 
new_md = []
 
 
def deal_yuque(new_md, old_path, file_path):
    i = 0
    print('处理中...')
    with open(old_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            line = re.sub(r'png#(.*)+', 'png)', line)
            img_url = str(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                     line)).replace("[", "").replace("'", "").replace(")", "").replace("]", "")
            # if ('](https://' in img_url) and ('.png' in img_url):
            if ('https://' in img_url) and ('.png' in img_url):
                i += 1
                # img_path = f'{file_path}\\img{i}.png'
                img_path = f'{file_path}/img{i}.png'
                download_img(img_url, img_path)
                line = line.replace(img_url, img_path)
            new_md.append(line)
    with open(new_file, 'w', encoding='utf-8', errors='ignore') as f:
        for new_md in new_md:
            f.write(str(new_md))
 
 
def download_img(img_url, img_path):
    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        open(img_path, 'wb').write(r.content)
    del r
 
 
def mkdir(file_path):
    file_path = file_path.strip()
    file_path = file_path.rstrip("\\")
    isExists = os.path.exists(file_path)
    if not isExists:
        os.makedirs(file_path)
        return file_path
 
 
if __name__ == '__main__':
    # old_path = input('原文件路径：')
    # file_path = input('图片存储路径：')
    old_path = "常规八股.md"
    file_path = "./figure"
    file_name = old_path.split("\\")[-1]
    new_path = '_' + file_name
    new_file = old_path.replace(file_name, "") + new_path
    mkdir(file_path)
    deal_yuque(new_md, old_path, file_path)
    print('处理完成')
    print('文件保存在：' + new_file)
    print('图片保存在：' + file_path)