import os
import logging
import smtplib
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def zip_dir(path, output=None):
    """压缩目录默认输出文件为path末尾路径+.zip"""
    output = output or os.path.basename(path) + '.zip'  # 压缩文件的名字
    zip = zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        relative_root = '' if root == path else root.replace(str(path), '') + os.sep  # 计算文件相对路径
        for filename in files:
            zip.write(os.path.join(root, filename), relative_root + filename)  # 文件路径 压缩文件路径（相对路径）
    zip.close()
    return os.path.abspath(output)


class EmailUtils:
    def __init__(self, host, user, password, port=25, enable_ssl=False):
        if enable_ssl is None:
            enable_ssl = True

        self.host = host
        self.user = user
        self.password = password
        self.port = port or DEFAULT_SMTP_PORT
        self.enable_ssl = enable_ssl

    def _build_msg(self, subject, receivers, body='', attachments=None):
        """组装EMAIL消息体"""
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.user
        msg['To'] = ','.join(receivers)
        if isinstance(body, str) and body.strip().startswith('<'):
            # 使用html格式
            msg.attach(MIMEText(body, 'html', 'utf-8'))
        else:
            msg.attach(MIMEText(body, 'plain', 'utf-8'))

        if isinstance(attachments, list):
            for path in attachments:
                need_remove = False  # 标记是否需要移除压缩文件
                if not os.path.exists(path):
                    raise FileNotFoundError('附件文件 %s 不存在' % path)
                if os.path.isdir(path):
                    file_path = zip_dir(path)
                    need_remove = True
                else:
                    file_path = path
                # 添加附件
                file_name = os.path.basename(file_path)
                att = MIMEBase('application', 'octet-stream')
                att.add_header('Content-Disposition', 'attachment',
                               filename=('utf-8', '', file_name))
                att.set_payload(open(file_path, 'rb').read())
                encoders.encode_base64(att)
                msg.attach(att)
                if need_remove is True:  # 添加后删除压缩文件
                    os.remove(file_path)
        return msg

    def send_email(self, subject, receivers, body='', attachments=None):
        """组装并发送邮件"""
        logging.debug("发送邮件到 to %s" % ','.join(receivers))
        msg = self._build_msg(subject, receivers, body, attachments)

        if self.enable_ssl is True:
            smtp = smtplib.SMTP_SSL(self.host, self.port)
        else:
            smtp = smtplib.SMTP(self.host, self.port)
        try:
            smtp.login(self.user, self.password)
            smtp.sendmail(self.user, receivers, msg.as_string())
        except Exception as ex:
            logging.exception(ex)
        print("发送邮件到 %s 完成" % ','.join(receivers))
