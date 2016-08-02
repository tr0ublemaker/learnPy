#-*- coding:utf-8 -*-
'''一个简单的执行脚本
func：将图片转化为字符串组成的画
input：图片
output：字符画
'''

from PIL import Image
import argparse

#命令行参数处理

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-O','--output')
parser.add_argument('--width', type = int, default = 40)
parser.add_argument('--height', type = int, default = 33)

#获取参数

args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@ARSTUVWXYZ%|8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjftBCDEFGHIJKLMNOPQ/\|()1{BCDEFGHIJKLMNOPQ}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char=  ['@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', '&nbsp;','@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', '&nbsp;','@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', '&nbsp;','@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', '&nbsp;','@', 'w', '#', '$', 'k', 'd', 't', 'j', 'i', '.', '&nbsp;']
#将灰度映射到字符
def get_char(r,b,g,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)

    unit = (256.0+1)/length

    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
    import codecs
    with codecs.open('result2.txt', mode='a', encoding='utf-8') as f_out:
        txt = ""
        for i in xrange(HEIGHT):
            for j in xrange(WIDTH):

                txt += get_char(*im.getpixel((j,i)))
            txt += '\n'
        f_out.write(txt)





    f_out.close()