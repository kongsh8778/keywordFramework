# -*-coding:utf-8 -*-

import smtplib
from email.mime.application import MIMEApplication
from Utils.FileUtils.Log import *
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendMail(object):
    """发送邮件类"""
    '''
    邮件配置信息
    '''
    def __init__(self,
                 receiver,
                 server='smtp.qq.com',
                 sender='455576105@qq.com',
                 password='jdnqrvvjveqzcafb'):

        self._server = server
        self._sender = sender
        self._password = password
        self._receiver = receiver

    def send_email(self, mail_subject, mail_content, *test_report_file_name):
        """打开报告文件读取文件内容"""
        #  邮件主题
        subject = mail_subject
        # 邮件设置
        msg = MIMEMultipart()
        msg['subject'] = Header(subject, 'utf-8')
        msg['from'] = self._sender
        if len(self._receiver) > 1:
            msg['To'] = ','.join(self._receiver)  # 群发邮件
        else:
            msg['To'] = self._receiver[0]

        # 添加邮件正文
        msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
        # print(test_report_file_name)
        for file in test_report_file_name:
            # 获得文件名
            file_name = os.path.split(file)[-1]
            # # 去掉后缀
            # file_name = os.path.splitext(file_name)[0]
            part = MIMEApplication(open(file, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=file_name)
            msg.attach(part)

        # 连接服务器，登录服务器，发送邮件
        try:
            smtp = smtplib.SMTP_SSL(self._server, 465)
            smtp.login(self._sender, self._password)
        except Exception:
            info('connect [%s] server failed or username and password incorrect!' % smtp)
        else:
            info('email server [%s] login success!' % smtp)
            try:
                smtp.sendmail(self._sender, self._receiver, msg.as_string())
            except Exception:
                traceback.print_exc()
                info('send email failed!')
            else:
                info('send email successed!')


if __name__ == '__main__':
    sendmail = SendMail('kongsh@hengbao.com')
    sendmail.send_email('测试报告', "测试通过", test_report_path + "\\test_report.html", r'F:\pet-shop-tutorial\box-img-lg.png')
    # sendmail.send_email('测试报告', "测试通过", r'F:\pet-shop-tutorial\box-img-lg.png')

