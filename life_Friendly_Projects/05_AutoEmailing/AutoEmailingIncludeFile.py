import os
# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart

# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

# 텍스트 형식
from email.mime.text import MIMEText
# 이미지 형식
from email.mime.image import MIMEImage
# 오디오 형식
from email.mime.audio import MIMEAudio

# 위의 모든 객체를 생성할 수 있는 기본 객체
# MIMEBase(_maintype, _subType)
# MIMEBase(<메인타입>, <서브 타입>)
from email.mime.base import MIMEBase

msg_dict = {
    'text' : { 'mainType' : 'text', 'subType' : 'plain', 'fileName' : 'res/email_sending/test.txt'},
    'image' : { 'mainType' :  'image', 'subType' : 'jpg', 'fileName' : 'res/email_sending/test.jpg'},
    'audio' : { 'mainType' : 'audio', 'subType' :  'mp3', 'fileName' : 'res/email_sending/test.mp3'},
    'video' : { 'mainType' : 'video', 'subType' : 'mp4', 'fileName' : 'res/email_sending/test.mp4'},
    'application' : { 'mainType' : 'application', 'subType' : 'octect-stream', 'fileName' : 'res/email_sending/text.pdf'}
}

def make_multimsg(msg_dict):
    multi = MIMEMultipart(_subType ='mixed')

    for key, value in msg_dict.items():
        # 각 타입에 적절한 MIMExxx() 함수를 호출하여 msg 객체를 생성한다.
        if key == 'text':
            with open(value['fileName'], encoding='utf-8') as fp:
                msg = MIMEText(fp.read(), _subType=value['subType'])
        elif key == 'image':
            with open(value['fileName'], 'rb') as fp:
                msg = MIMEImage(fp.read(), _subType=value['subType'])
        elif key == 'audio':
            with open(value['fileName'], "rb") as fp:
                msg = MIMEAudio(fp.read(), _subType=value['subType'])
        else:  
            with open(value['fileName'], 'rb') as fp :
                msg = MIMEBase(value['mainType'], _subType = value['subType'])
                msg .set_payload(fp.read())
                encoders.encode_base64(msg)

        msg.add_header('Content-Disposition', 'attachment', fileName=os.path.basename(value['fileName']))

        multi.attach(msg)

        return multi

