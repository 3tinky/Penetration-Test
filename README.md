# Penetration-Test-Tips
*   Tips001-解决powershell执行时的编码问题

    *   Powershell编码
        <pre><code>
        $CMD = "powershell -c calc.exe"
        $Bytes = [System.Text.Encoding]::Unicode.GetBytes($CMD)
        $EncodedText =[Convert]::ToBase64String($Bytes)
        $EncodedTex
        </code>
        </pre>
        
    *   Python编码(部分) [源码地址](http://weibo.com/ihubo)
        <pre><code>
        cmd = [self._where('PowerShell.exe'),"-NoLogo", "-NonInteractive", "-Command", "-"]
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self.popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
        self.coding = coding
