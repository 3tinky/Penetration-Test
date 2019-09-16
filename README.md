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
        
    *   Python编码(部分) [源码地址](https://github.com/3tinky/Penetration-Test/blob/master/scripts/py_psh_encode.py)
        <pre><code>
        cmd = [self._where('PowerShell.exe'),"-NoLogo", "-NonInteractive", "-Command", "-"]
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        self.popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, startupinfo=startupinfo)
        self.coding = coding
        
#   《中华人民共和国网络安全法》
##   第二十七条
任何个人和组织不得从事非法侵入他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动；不得提供专门用于从事侵入网络、干扰网络正常功能及防护措施、窃取网络数据等危害网络安全活动的程序、工具；明知他人从事危害网络安全的活动的，不得为其提供技术支持、广告推广、支付结算等帮助。
##   第六十三条
违反本法第二十七条规定，从事危害网络安全的活动，或者提供专门用于从事危害网络安全活动的程序、工具，或者为他人从事危害网络安全的活动提供技术支持、广告推广、支付结算等帮助，尚不构成犯罪的，由公安机关没收违法所得，处五日以下拘留，可以并处五万元以上五十万元以下罚款；情节较重的，处五日以上十五日以下拘留，可以并处十万元以上一百万元以下罚款。单位有前款行为的，由公安机关没收违法所得，处十万元以上一百万元以下罚款，并对直接负责的主管人员和其他直接责任人员依照前款规定处罚。违反本法第二十七条规定，受到治安管理处罚的人员，五年内不得从事网络安全管理和网络运营关键岗位的工作；受到刑事处罚的人员，终身不得从事网络安全管理和网络运营关键岗位的工作。
