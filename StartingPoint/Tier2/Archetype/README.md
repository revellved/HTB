<h1 align="center">Archetype</h1>

> NOTE: Do not forget to make sure that you downloaded the config file for connecting via vpn and connected to it. 

<h2 align="center">STEPS</h2>

<details> 
    <summary>
        <i>TASK 1: Which TCP port is hosting a database server?</i>
        <blockquote><i>nmap with -F</i></blockquote>
    </summary><br>
    <b>1433</b>
</details><br>

<details> 
    <summary>
        <i>TASK 2: What is the name of the non-Administrative share available over SMB?</i>
        <blockquote><i>smbclient -N -L will list shares. Administrative shares end in $.</i></blockquote>
    </summary><br>
    <b>backups</b>
</details><br>

<details> 
    <summary>
        <i>TASK 3: What is the password identified in the file on the SMB share?</i>
        <blockquote><i>Connect with smbclient.</i></blockquote>
    </summary><br>
    <b>M3g4c0rp123</b>
</details><br>

<details> 
    <summary>
        <i>TASK 4: What script from Impacket collection can be used in order to establish an authenticated connection to a Microsoft SQL Server?</i>
        <blockquote><i>Impacket examples can always help. Search for one related to the mssql.</i></blockquote>
    </summary><br>
    <b>mssqlclient.py</b>
</details><br>

<details> 
    <summary>
        <i>TASK 5: What extended stored procedure of Microsoft SQL Server can be used in order to spawn a Windows command shell?</i>
        <blockquote><i>Pentesting cheatsheets for Microsoft SQL Server will definitely help. Also a "Transact sql shell for Microsoft SQL Server" search in Google will bring useful results.</i></blockquote>
    </summary><br>
    <b>xp_cmdshell</b>
</details><br>

<details> 
    <summary>
        <i>TASK 6: What script can be used in order to search possible paths to escalate privileges on Windows hosts?</i>
    </summary><br>
    <b>winpeas</b>
</details><br>

<details> 
    <summary>
        <i>TASK 7: What file contains the administrator's password?</i>
        <blockquote><i>see C:\Users\sql_svc\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine</i></blockquote>
    </summary><br>
    <b>ConsoleHost_history.txt</b>
</details><br>

<details> 
    <summary>
        <i>SUBMIT FLAG: Submit user flag</i>
    </summary><br>
    <b>connect to mssql via mssqlclient.py (Iampacket). Next using xp_cmdshell get nc64.exe and run it for reverse shellon your machine with runner nc</b>
</details><br>

<details> 
    <summary>
        <i>SUBMIT FLAG: Submit root flag</i>
    </summary><br>
    <b>auth as administrator via psexec.py (Iampacket) and find root.txt</b>
</details><br>


<h2 align="center">NOTIFICATION</h2>
<p align="center"><b>Now the FBI is watching you ;)</b></p>
