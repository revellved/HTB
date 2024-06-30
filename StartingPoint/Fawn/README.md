<h1 align="center">FAWN</h1>

> NOTE: Do not forget to make sure that you downloaded the config file for connecting via vpn and connected to it. 
<h2 align="center">STEPS</h2>

<details> 
    <summary>
        <i>TASK 1: What does the 3-letter acronym FTP stand for? </i>
    </summary><br>
    <b>File Transfer Protocol</b>
</details>
<br>
 
<details> 
    <summary>
        <i>TASK 2: Which port does the FTP service listen on usually?</i>
    </summary><br>
    <b>21</b>
</details>
<br>
 
<details> 
    <summary>
        <i>TASK 3: What acronym is used for the version of FTP secured by running over the SSH protocol?</i>
    </summary><br>
    <b>SFTP</b>
</details>
<br>
 
<details> 
    <summary>
        <i>TASK 4: What is the command we can use to send an ICMP echo request to test our connection to the target?</i>
    </summary><br>
    <b>ping</b>
</details>
<br>

<details> 
    <summary>
        <i>TASK 5: From your scans, what version is FTP running on the target?</i>
        <blockquote cite="HINT">
            <i>HINT: To get the ftp version you shoud use nmap with the -sV switch, which allows us to find out the software versions: nmap -sV $HTB_MACHINE_IP_ADRESS</i>
        </blockquote>
    </summary><br>
    <b>vsftpd 3.0.3</b>
</details>
<br>

<details> 
    <summary>
        <i>TASK 6: From your scans, what OS type is running on the target?</i>
        <blockquote cite="HINT">
            <i>HINT: To get the OS type you should use nmap with the -sV switch, which allows us to find out the software versions: nmap -sV $HTB_MACHINE_IP_ADRESS</i>
        </blockquote>
    </summary><br>
    <b>Unix</b>
</details>
<br>

<details> 
    <summary>
        <i>TASK 7: What is the command we need to run in order to display the 'ftp' client help menu?</i>
    </summary><br>
    <b>ftp -h</b>
</details>
<br>

<details> 
    <summary>
        <i>TASK 8: What is username that is used over FTP when you want to log in without having an account?</i>
        <blockquote cite="NOTE">
            <i>NOTE: On this machine, if you are asked for a password, for anonymous you can enter whatever you want or leave it blank, you will still be successfully logged in.</i>
        </blockquote>
    </summary><br>
    <b>anonymous</b>
</details>
<br>

<details> 
    <summary>
        <i>TASK 9: What is the response code we get for the FTP message 'Login successful'?</i>
    </summary><br>
    <b>230</b>
</details>
<br>

<details> 
    <summary>
        <i>TASK 10: There are a couple of commands we can use to list the files and directories available on the FTP server. One is dir. What is the other that is a common way to list files on a Linux system.</i>
    </summary><br>
    <b>ls</b>
</details>
<br>

<details> 
    <summary>
        <i>TASK 11: What is the command used to download the file we found on the FTP server?</i>
    </summary><br>
    <b>get</b>
</details>
<br>

<details> 
    <summary>
        <i>SUBMIT FLUG: Submit root flag</i>
    </summary><br>
    <b>To receive the flag you need to connect via ftp to the IP address that you receive when you spawn the machine. Next you need to enter the default login and password (see TASK 8), and then download the flag using the get command (ftp does not support cat</b>
</details>
<br>

<h2 align="center">NOTIFICATION</h2>

<p align="center">
    <b>Now the FBI is watching you ;)</b>
</p>
