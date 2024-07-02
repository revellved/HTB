<h1 align="center">Crocodile</h1>

> NOTE: Do not forget to make sure that you downloaded the config file for connecting via vpn and connected to it. 

<h2 align="center">STEPS</h2>

<details> 
    <summary>
        <i>TASK 1: What Nmap scanning switch employs the use of default scripts during a scan?</i>
    </summary><br>
    <b>-sC</b>
</details><br>

<details> 
    <summary>
        <i>TASK 2: What service version is found to be running on port 21?</i>
    </summary><br>
    <b>vsftpd 3.0.3</b>
</details><br>

<details> 
    <summary>
        <i>TASK 3: What FTP code is returned to us for the "Anonymous FTP login allowed" message?</i>
        <blockquote><i>conect to ftp as anonymous</i></blockquote>
    </summary><br>
    <b>230</b>
</details><br>

<details> 
    <summary>
        <i>TASK 4: After connecting to the FTP server using the ftp client, what username do we provide when prompted to log in anonymously?</i>
    </summary><br>
    <b>anonymous</b>
</details><br>

<details> 
    <summary>
        <i>TASK 5: After connecting to the FTP server anonymously, what command can we use to download the files we find on the FTP server?</i>
    </summary><br>
    <b>get</b>
</details><br>

<details> 
    <summary>
        <i>TASK 6: What is one of the higher-privilege sounding usernames in 'allowed.userlist' that we download from the FTP server?</i>
    </summary><br>
    <b>admin</b>
</details><br>

<details> 
    <summary>
        <i>TASK 7: What version of Apache HTTP Server is running on the target host?</i>
        <blockquote><i>using nmap with -sV flag</i></blockquote>
    </summary><br>
    <b>Apache httpd 2.4.41</b>
</details><br>

<details> 
    <summary>
        <i>TASK 8: What switch can we use with Gobuster to specify we are looking for specific filetypes?</i>
    </summary><br>
    <b>-x</b>
</details><br>

<details> 
    <summary>
        <i>TASK 9: Which PHP file can we identify with directory brute force that will provide the opportunity to authenticate to the web service?</i>
        <blockquote><i>usning gobuster</i></blockquote>
    </summary><br>
    <b>login.php</b>
</details><br>

<details> 
    <summary>
        <i>SUBMIT FLAG: Submit root flag</i>
    </summary><br>
    <b>The admin password is on the FTP serve</b>
</details><br>


<h2 align="center">NOTIFICATION</h2>
<p align="center"><b>Now the FBI is watching you ;)</b></p>
