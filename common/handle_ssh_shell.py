# Author : Ryanyi
# Creation time : 2022/12/13
# Data maintainer : Ryanyi


import paramiko, getpass, sys, traceback
from src.common import config


class SSHUtils():
    def login(self, ip, port, username, passwd):
        self.ip = ip
        self.port = port
        self.username = username
        self.passwd = passwd

    def ssh(self, shell):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, self.port, self.username, self.passwd)
            stdin, stdout, stderr = ssh.exec_command(shell)
            ssh.close()
        except:
            type, value, tb = sys.exc_info()
            return traceback.format_exception(type, value, tb)


if __name__ == '__main__':
    myssh = SSHUtils()
    myssh.login(config.ssh_ip, config.ssh_port, config.ssh_username, config.ssh_password)
    myssh.ssh(config.cmd_1+";"+config.cmd_2)


