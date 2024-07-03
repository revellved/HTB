<h1 align="center">Three</h1>

> NOTE: Do not forget to make sure that you downloaded the config file for connecting via vpn and connected to it. 

<h2 align="center">STEPS</h2>

<details> 
    <summary>
        <i>TASK 1: How many TCP ports are open?</i>
        <blockquote><i>nmap with flag -p-</i></blockquote>
    </summary><br>
    <b>2</b>
</details><br>

<details> 
    <summary>
        <i>TASK 2: What is the domain of the email address provided in the "Contact" section of the website?</i>
    </summary><br>
    <b>thetoppers.htb</b>
</details><br>

<details> 
    <summary>
        <i>TASK 3: In the absence of a DNS server, which Linux file can we use to resolve hostnames to IP addresses in order to be able to access the websites that point to those hostnames?</i>
    </summary><br>
    <b>/etc/hosts</b>
</details><br>

<details> 
    <summary>
        <i>TASK 4: Which sub-domain is discovered during further enumeration?</i>
        <blockquote><i>via gobuster with subdomain wordlist (https://github.com/n0kovo/n0kovo_subdomains)</i></blockquote>
    </summary><br>
    <b>s3.thetoppers.htb</b>
</details><br>

<details> 
    <summary>
        <i>TASK 5: Which service is running on the discovered sub-domain?</i>
    </summary><br>
    <b>Amazon s3</b>
</details><br>

<details> 
    <summary>
        <i>TASK 6: Which command line utility can be used to interact with the service running on the discovered sub-domain?</i>
    </summary><br>
    <b>awscli</b>
</details><br>

<details> 
    <summary>
        <i>TASK 7: Which command is used to set up the AWS CLI installation?</i>
    </summary><br>
    <b>aws configure</b>
</details><br>

<details> 
    <summary>
        <i>TASK 8: What is the command used by the above utility to list all of the S3 buckets?</i>
    </summary><br>
    <b>aws s3 ls</b>
</details><br>

<details> 
    <summary>
        <i>TASK 9: This server is configured to run files written in what web scripting language?</i>
        <blockquote><i>aws s3 ls --endpoint-url=http://s3.thetoppers.htb s3://thetoppers.htb</i></blockquote>
    </summary><br>
    <b>php</b>
</details><br>

<details> 
    <summary>
        <i>SUBMIT FLAG: Submit root flag</i>
    </summary><br>
    <b>write php script with reverse shell from webpage and upload it on server via aws-cli cp and find out flag on top dir from current (with index.html)</b>
</details><br>


<h2 align="center">NOTIFICATION</h2>
<p align="center"><b>Now the FBI is watching you ;)</b></p>
