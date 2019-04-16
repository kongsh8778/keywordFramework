# -*-coding:utf-8 -*-
from Utils.OtherUtils.SendMail import SendMail
from Utils.FileUtils.ConfigParser import ConfigParser
from Config.ProjVar import mail_file_conf_path

def send_test_result(mail_subject,  mail_content,  *test_report_file_name):
    """邮件发送测试结果"""
    # 从配置文件中获取所有邮件接收者
    cf = ConfigParser(mail_file_conf_path)
    receivers_list = [receiver for receiver in cf.get_all_option_items("Receivers").values()]
    # print(receivers_list)
    # 从配置文件中获取发送者
    sender = cf.get_all_option_items("Sender")
    # 实例化发送邮件类的对象
    sendmail = SendMail(receivers_list, sender=sender['user'], password=sender['password'])
    # 发送邮件
    sendmail.send_email(mail_subject, mail_content, *test_report_file_name)


if __name__ == "__main__":
    send_test_result('测试报告', '测试通过', r'F:\pet-shop-tutorial\box-img-lg.png')
