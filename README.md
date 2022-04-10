# Smart-Garden-System
Smart Garden System using Node-Red

## About The Project
An Node-Red project that smart garden system, including 
light detection and auto light switch, 
auto watering, 
live stream video, 
soil moisture detection,
temperature detection,
humidity detection.


### Project dependencies

* [Python](https://www.python.org/)
* [PICamera](https://picamera.readthedocs.io/)
* [Flask](https://flask.palletsprojects.com/)
* [Node-Red](https://nodered.org/)
* [Paho-mqtt](https://pypi.org/project/paho-mqtt/)
* [Node.JS](https://nodejs.org/en/)
* [Npm](https://www.npmjs.com/)
	
## Hardware requirement

* 5mp camera
* DHT11 sensor
* LDR snesor
* ADS7830
* water pump
* relay
	

## Getting Started
Run the following steps to get a local copy up.

### Prerequisites

Install the following packages for Raspberry PI
  ```sh
  sudo apt install python3-pip
  sudo pip install picamera
  pip install paho-mqtt
  pip install Flask
  pip install opencv-python
  ```

Install the following packages for Node-Red
```sh
node-red-contrib-dht-sensor
node-red-contrib-fs
node-red-contrib-multipart-stream-decoder
node-red-dashboard
node-red-node-pi-gpio
```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/AlvisLai/Smart-Garden-System
   ```
2. Start Node-Red
   ```sh
   node-red-start
   ```
3. Import NodeRedSetup.json into Node-Red

4. Access http://localhost:1880/ui for the control dashboard
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Alvis Lai - alvislaish@gamil.com, 
Kenny Chan - arkin803@gmail.com

Project Link: [https://github.com/AlvisLai/Smart-Garden-System](https://github.com/AlvisLai/Smart-Garden-System)

   
   
   
   
   
   
   
   