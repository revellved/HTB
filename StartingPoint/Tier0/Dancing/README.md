<h1 align="center">Dancing</h1>

> NOTE: Do not forget to make sure that you downloaded the config file for connecting via vpn and connected to it. 

<h2 align="center">STEPS</h2>

<details> 
    <summary>
        <i>TASK 1: What does the 3-letter acronym SMB stand for?</i>
    </summary><br>
    <b>Server Message Block</b>
</details><br>

<details> 
    <summary>
        <i>TASK 2: What port does SMB use to operate at?</i>
    </summary><br>
    <b>445</b>
</details><br>

<details> 
    <summary>
        <i>TASK 3: What is the service name for port 445 that came up in our Nmap scan?</i>
        <blockquote><i>nmap -p 445 $MACHINE_IP_ADRESS</i></blockquote>
    </summary><br>
    <b>microsoft-ds</b>
</details><br>

<details> 
    <summary>
        <i>TASK 4: What is the 'flag' or 'switch' that we can use with the smbclient utility to 'list' the available shares on Dancing?</i>
    </summary><br>
    <b>-L</b>
</details><br>

<details> 
    <summary>
        <i>TASK 5: How many shares are there on Dancing?</i>
        <blockquote><i>smbclient -L $MACHINE_IP_ADRESS</i></blockquote>
    </summary><br>
    <b>4</b>
</details><br>

<details> 
    <summary>
        <i>TASK 6: What is the name of the share we are able to access in the end with a blank password?</i>
        <blockquote><i>smbclient -L $MACHINE_IP_ADRESS</i></blockquote>
    </summary><br>
    <b>WorkShares </b>
</details><br>

<details> 
    <summary>
        <i>TASK 7: What is the command we can use within the SMB shell to download the files we find?</i>
    </summary><br>
    <b>get</b>
</details><br>

<details> 
    <summary>
        <i>SUBMIT FLAG: Submit root flag</i>
    </summary><br>
    <b>You should connected via smbclient: smbclient //$MACHINE_IP_ADRESS/WorkShares -U " "%" "</b>
</details><br>

<h2 align="center">NOTIFICATION</h2>
<p align="center"><b>Now the FBI is watching you ;)</b></p>
