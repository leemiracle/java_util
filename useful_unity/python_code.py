import re
import datetime
from html import unescape
import xml.etree.ElementTree as ET
import requests
import hashlib
import shutil

def re_use():
    a = "<ALBUMS><ALBUM id=''>http://m.xxx.com/s/files/e6/cd/e6cd15794ea9150a78ee88b7a42461bf296551b2/l81oEebgsBCAbaXhkpg7wJp52OfXtB6Di5QK3iPQ/JPEG_20180319_152824_1883313733.jpg</ALBUM></ALBUMS>"
    batRegex = re.compile(r'<ALBUM.*?>(.*?)</ALBUM>')
    batRegex.findall()

def datetime_use():
    datetime.datetime.utcnow()

def xml_use():
    vcard = "<vCard xmlns='vcard-temp'><FN>هعممنت</FN><AVATARURL>http://cdn.1-1.io/s/files/e6/cd/e6cd15794ea9150a78ee88b7a42461bf296551b2/EScQ7DR73xi4AL9CMCcFfnoE1ac6QVbiyqO9TwWD/JPEG_20180319_151957_69017972.jpg</AVATARURL><BDAY>1990-01-01</BDAY><LANG>ar_MA</LANG><NICKNAME>هعممنت</NICKNAME><WELCOME>مرحبا، يشرفني بمقابلتكم! !مرحبا</WELCOME><VIDEOS>&lt;VIDEO THUMBNAIL=&apos;http://cdn.1-1.io/s/files/e6/cd/e6cd15794ea9150a78ee88b7a42461bf296551b2/yLT0Br9TKfRjRA6LY3F4eIRHyEUDWXbhUbcR0eKd/1521473205263_thumbnail.jpg&apos; VIDEOURL=&apos;http://cdn.1-1.io/s/files/e6/cd/e6cd15794ea9150a78ee88b7a42461bf296551b2/K79ZdZD2uV0ag0xdbScn2Y9pbY0aGFp73rpnTi5j/1521473200287.mp4&apos; CHECKSUM=&apos;B4F3DC053C8A3DF4D320BC6B80B11681&apos;/&gt;</VIDEOS><ALBUMS>&lt;ALBUM&gt;http://cdn.1-1.io/s/files/e6/cd/e6cd15794ea9150a78ee88b7a42461bf296551b2/l81oEebgsBCAbaXhkpg7wJp52OfXtB6Di5QK3iPQ/JPEG_20180319_152824_1883313733.jpg&lt;/ALBUM&gt;</ALBUMS><ADR><WORK/><CTRY>MA</CTRY></ADR><ADR><CTRY>MA</CTRY><HOME/></ADR><GENDER>female</GENDER></vCard>"
    vcard = unescape(vcard)
    tree = ET.fromstring(vcard)
    end = tree.tag.index('}')
    namespace = tree.tag[1:end]
    albums = tree.findall(".//{namespace}ALBUM".format(namespace='{' + namespace + '}'))
    for d in albums:
        print(d.text)

def hashlib_use():
    uri = 'http://cdn.1-1.io/s/files/e6/cd/e6cd15794ea9150a78ee88b7a42461bf296551b2/l81oEebgsBCAbaXhkpg7wJp52OfXtB6Di5QK3iPQ/JPEG_20180319_152824_1883313733.jpg'
    response = requests.get(uri, stream=True)
    with open('img.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    with open('img.png', 'rb') as file:
        data = file.read()
        m = hashlib.md5()
        m.update(data)
        md5_val = m.hexdigest()
        print(md5_val)
    return md5_val

