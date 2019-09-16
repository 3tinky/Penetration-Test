# Penetration-Test-Tips
*   Tips001-解决powershell执行时的编码问题
   
    <p>Powershell编码：</p>
    <pre><code>
    $CMD = "powershell -c calc.exe"
    $Bytes = [System.Text.Encoding]::Unicode.GetBytes($CMD)
    $EncodedText =[Convert]::ToBase64String($Bytes)
    $EncodedTex
    </code>
    </pre>
