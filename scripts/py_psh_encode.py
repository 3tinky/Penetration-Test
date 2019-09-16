
# coding:utf-8

import os
from glob import glob
import subprocess


class PowerShell:

    def __init__(self, coding, ):

        cmd = [self._where('PowerShell.exe'),
               "-NoLogo", "-NonInteractive",
               "-Command", "-"]
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self.popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
        self.coding = coding

    def __enter__(self):
        return self

    def __exit__(self, a, b, c):
        self.popen.kill()

    def run(self, cmd):
        b_cmd = cmd.encode(encoding=self.coding)
        b_outs, errs = self.popen.communicate(b_cmd)
        outs = b_outs.decode(encoding=self.coding)
        return outs, errs

    @staticmethod
    def _where(filename, dirs=None, env="PATH"):
        if dirs is None:
            dirs = []
        if not isinstance(dirs, list):
            dirs = [dirs]
        if glob(filename):
            return filename
        paths = [os.curdir] + os.environ[env].split(os.path.pathsep) + dirs
        try:
            return next(os.path.normpath(match)
                        for path in paths
                        for match in glob(os.path.join(path, filename))
                        if match)
        except (StopIteration, RuntimeError):
            raise IOError("File not found: %s" % filename)


if __name__ == '__main__':

    cmd = "\"" + raw_input('Input Your Strings:') + "\""

    with PowerShell('GBK') as ps:
        outs, errs = ps.run("$base64encoded=[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes(" + str(cmd) + "));$base64encoded")

    posh_cmd = "powershell.exe -exec bypass -enc "
    print(posh_cmd + outs)
