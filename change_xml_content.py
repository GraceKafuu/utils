# coding=utf-8
import os
import os.path
import xml.dom.minidom

path = "/media/nvidia/ubuntu/Aug_Annotations/"
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        print(xmlFile)

        # TODO
    # xml文件读取操作

    # 将获取的xml文件名送入到dom解析
    dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
    root = dom.documentElement
    # 获取标签对name/pose之间的值
    filename = root.getElementsByTagName('filename')


    name = filename[0].firstChild.data.split('.')[0]
    filename[0].firstChild.data = name + '.jpg'

    with open(os.path.join(path, xmlFile),'w') as fh:
        dom.writexml(fh)
        print("OK!")