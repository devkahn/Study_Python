import smtplib


smtp_info = dict({"smtp_server" : "smpt.naver.com",
                  "smtp_user_id" : "gaebok0331@naver.com",
                  "smtp_user_pw" : "!qp02wo93ei8",
                  "smtp_port" : 587})

                
def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info['smtp_server'], smtp_info["smtp_port"]) as server:
        server.starttls()
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])

        response = server.sendmail(msg['from'], msg['to'], msg.as_string())

        if not response:
            print('이메일을 성공ㅈ4긍로 보냈습니다.')
        else:
            print(response)