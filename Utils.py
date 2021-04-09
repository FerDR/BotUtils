import textwrap
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import facebook
from pathlib import Path

def get_font(size):
    try:#Linux
        font = ImageFont.truetype("Lato-Medium.ttf",size)
    except:#Windows
        font = ImageFont.truetype("arial.ttf",size)
        #mac users BTFO
    return font

def get_fontsize(text,draw,maxlenx,maxleny):
    pw = []
    ph = []
    for i in range(10):
        font = get_font((i+1)*10)
        ps = draw.textsize(text,font)
        pw.append(ps[0])
        ph.append(ps[1])
        #print (pw, ph)
    return int(min(10*maxlenx//np.mean(np.diff(pw)),10*maxleny//np.mean(np.diff(ph))))

def get_wrapped_text(text,draw,maxlenx,maxleny):
    size = 0
    lines = 0
    for j in range(5):
        i = j + 1
       font = get_fontsize(textwrap.fill(text,len(text)//i+i-1),draw,maxlenx,maxleny)
       if font>size:
           size = font
           lines = i
     return textwrap.fill(text,len(text)//lines+lines-1),size
