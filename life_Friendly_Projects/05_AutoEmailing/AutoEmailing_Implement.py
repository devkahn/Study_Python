from fileinput import filename
import os
import smtplib
# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart

# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

# 텍스트형식
from email.mime.text import MIMEText
# 이미지 형식
from email.mime.image import MIMEImage
# 오디오 형식
from email.mime.audio import MIMEAudio

# 위의 모든 객체들을 생성할 수 있는 기본 객체
# MIMEBase(_mainType, _subType)
# MIMEBase(<메인타입>, <서브타입>)
from email.mime.base import MIMEBase
from urllib import response

def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls()
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])
        # 로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string())
        # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.

        # 이메일을 성공적으로 보내면 결과는{}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print(response)


def make_multimsg(msg_dict):
    multi = MIMEMultipart(_subType = 'mixed')

    for key, value in msg_dict.items():
        if key == 'text' :
            with open(value['fileName'], encoding='utf-8') as fp:
                msg = MIMEText(fp.read(), _subType = value['subType'])
        elif key == 'image' : 
            with open(value['fileName'], 'rb' ) as fp:
                msg = MIMEImage(fp.read(), _subType = value['subType'])
        elif key == 'audio' : 
            with open(value['fileName'], 'rb' ) as fp:
                msg = MIMEAudio(fp.read(), _subType = value['subType'])
        else:
            with open(value['fileName'], 'rb') as fp :
                msg = MIMEBase(value['mainType'], _subType = value['subType'])
                msg.set_payload(fp.read())
                encoders.encode_base64(msg)

        # 파일 이름을 첨부파일 제목으로 추가
        msg.add_header('Content=Disposition', 'attachment', filename=os.path.basename(value['fileName']))
        # 첨부파일 추가
        multi.attach(msg)
    
    return multi
    

