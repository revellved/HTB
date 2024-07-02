<h1 align="center">Responder</h1>

> NOTE: Do not forget to make sure that you downloaded the config file for connecting via vpn and connected to it. 

<h2 align="center">STEPS</h2>

<details> 
    <summary>
        <i>TASK 1: When visiting the web service using the IP address, what is the domain that we are being redirected to?</i>
    </summary><br>
    <b>unika.htb</b>
</details><br>

<details> 
    <summary>
        <i>TASK 2: Which scripting language is being used on the server to generate webpages?</i>
    </summary><br>
    <b>php</b>
</details><br>

<details> 
    <summary>
        <i>TASK 3: What is the name of the URL parameter which is used to load different language versions of the webpage?</i>
    </summary><br>
    <b>page</b>
</details><br>

<details> 
    <summary>
        <i>TASK 4: Which of the following values for the `page` parameter would be an example of exploiting a Local File Include (LFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"</i>
    </summary><br>
    <b>../../../../../../../../windows/system32/drivers/etc/hosts</b>
</details><br>

<details> 
    <summary>
        <i>TASK 5: Which of the following values for the `page` parameter would be an example of exploiting a Remote File Include (RFI) vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts", "minikatz.exe"</i>
    </summary><br>
    <b>//10.10.14.6/somefile</b>
</details><br>

<details> 
    <summary>
        <i>TASK 6: What does NTLM stand for?</i>
    </summary><br>
    <b>New Technology Lan Manager</b>
</details><br>

<details> 
    <summary>
        <i>TASK 7: Which flag do we use in the Responder utility to specify the network interface?</i>
    </summary><br>
    <b>-I</b>
</details><br>

<details> 
    <summary>
        <i>TASK 8: There are several tools that take a NetNTLMv2 challenge/response and try millions of passwords to see if any of them generate the same response. One such tool is often referred to as `john`, but the full name is what?.</i>
    </summary><br>
    <b>john the ripper</b>
</details><br>

<details> 
    <summary>
        <i>TASK 9: What is the password for the administrator user?</i>
        <blockquote><i>using responder and john (with wordlist rockyou)</i></blockquote>
    </summary><br>
    <b>badminton</b>
</details><br>

<details> 
    <summary>
        <i>TASK 10: We'll use a Windows service (i.e. running on the box) to remotely access the Responder machine using the password we recovered. What port TCP does it listen on?</i>
        <blockquote><i>using nmap -Pn -p- $MACHINE_IP_ADRESS</i></blockquote>
    </summary><br>
    <b>5985</b>
</details><br>

<details> 
    <summary>
        <i>SUBMIT FLAG: Submit root flag</i>
    </summary><br>
    <b>Connect to Windows Power Shell remote via evil-winrm and find flag (it's on the other a user)</b>
</details><br>


<h2 align="center">NOTIFICATION</h2>
<p align="center"><b>Now the FBI is watching you ;)</b></p>
