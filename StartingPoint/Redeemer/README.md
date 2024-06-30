<h1 align="center">REDEEMER</h1>

> NOTE: Do not forget to make sure that you downloaded the config file for connecting via vpn and connected to it. 


<h2 align="center">STEPS</h2>

<details> 
    <summary>
        <i>TASK 1: Which TCP port is open on the machine?</i>
        <blockquote><i>need using nmap with flag -T5, -p-, --open</i></blockquote>
    </summary><br>
    <b>6379</b>
</details><br>

<details> 
    <summary>
        <i>TASK 2: Which service is running on the port that is open on the machine?</i>
        <blockquote><i>need using nmpa with flag -sV</i></blockquote>
    </summary><br>
    <b>redis</b>
</details><br>

<details> 
    <summary>
        <i>TASK 3: What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database</i>
    </summary><br>
    <b>In-memory Database</b>
</details><br>

<details> 
    <summary>
        <i>TASK 4: Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into the terminal without any arguments.</i>
    </summary><br>
    <b>redis-cli</b>
</details><br>

<details> 
    <summary>
        <i>TASK 5: Which flag is used with the Redis command-line utility to specify the hostname?</i>
    </summary><br>
    <b>-h</b>
</details><br>

<details> 
    <summary>
        <i>TASK 6: Once connected to a Redis server, which command is used to obtain the information and statistics about the Redis server?</i>
    </summary><br>
    <b>info</b>
</details><br>

<details> 
    <summary>
        <i>TASK 7: What is the version of the Redis server being used on the target machine?</i>
    </summary><br>
    <b>5.0.7</b>
</details><br>

<details> 
    <summary>
        <i>TASK 8: Which command is used to select the desired database in Redis?</i>
    </summary><br>
    <b>select</b>
</details><br>

<details> 
    <summary>
        <i>TASK 9: How many keys are present inside the database with index 0?</i>
        <blockquote><i>need using redis-cli -h $MACHINE_IP_ADRESS info</i></blockquote>
    </summary><br>
    <b>4</b>
</details><br>

<details> 
    <summary>
        <i>TASK 10: Which command is used to obtain all the keys in a database?</i>
    </summary><br>
    <b>KEYS *</b>
</details><br>

<details> 
    <summary>
        <i>SUBMIT FLAG: Submit root flag</i>
    </summary><br>
    <b>need connected to redis database via redis-cli and get key with flag</b>
</details><br>


<h2 align="center">NOTIFICATION</h2>

<p align="center">
    <b>Now the FBI is watching you ;)</b>
</p>
