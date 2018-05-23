1. Host a accessible MQTT broker
    * [Mosquitto MQTT Broker on Linux (www.steves-internet-guide)](http://www.steves-internet-guide.com/install-mosquitto-linux/)
    * Install the Mosquitto Broker.
        ```bash
        sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
        sudo apt-get update
        sudo apt-get install mosquitto
        sudo apt-get install mosquitto-clients
        ``` 
    * Start and Stop the service
        ```bash
        sudo /etc/init.d/mosquitto start
        sudo /etc/init.d/mosquitto stop
        ```
    * Start the mosquitto broker and see the control message on console.
        ```bash
        mosquitto -v
        ```
2.  Starting Mosquitto Using a **Configuration file**.
    * You can find the **mosquitto.conf** template file in the **/etc/mosquitto/** folder.
    * Start with the config, it's better to save a file on directory which need no root permision.
    ```bash
    mosquitto -c <filename>
    mosquitto -c /home/ubuntu/mqtt/mosquitto.conf #where I put the config
    ``` 
   * Config:
        * Setting the Logging File Location
        * Others
         
       
       
3. 
rostopic pub -r 10 my_topic std_msgs/String "hello there"     

  
        