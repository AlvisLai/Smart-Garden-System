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

*5mp camera
*DHT11 sensor
*LDR snesor
*ADS7830
*water pump
*relay
	

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
3. Import the json into Node-Red
   ```
   [
    {
        "id": "d757dbb1.993928",
        "type": "tab",
        "label": "Smart weed System",
        "disabled": false,
        "info": ""
    },
    {
        "id": "2b1353fe4638747c",
        "type": "exec",
        "z": "d757dbb1.993928",
        "command": "sudo uhubctl -l 1-1 -a ",
        "addpay": "payload",
        "append": "",
        "useSpawn": "false",
        "timer": "",
        "winHide": false,
        "oldrc": false,
        "name": "",
        "x": 560,
        "y": 360,
        "wires": [
            [
                "a9104746a151ba48"
            ],
            [],
            []
        ]
    },
    {
        "id": "a9104746a151ba48",
        "type": "exec",
        "z": "d757dbb1.993928",
        "command": "sudo uhubctl | grep 'Port 1' | awk '{print $4}' | awk 'FNR == 1'",
        "addpay": "",
        "append": "",
        "useSpawn": "false",
        "timer": "",
        "winHide": false,
        "oldrc": false,
        "name": "",
        "x": 640,
        "y": 480,
        "wires": [
            [
                "93f3b07819016961"
            ],
            [],
            []
        ]
    },
    {
        "id": "bb8c760217c069b8",
        "type": "ui_text",
        "z": "d757dbb1.993928",
        "group": "738e60bcc9dffdc0",
        "order": 3,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "LED Bar Status",
        "format": "{{msg.ledStatus}}",
        "layout": "col-center",
        "className": "",
        "x": 680,
        "y": 620,
        "wires": []
    },
    {
        "id": "9010c467a36fc991",
        "type": "exec",
        "z": "d757dbb1.993928",
        "command": "python3 /home/pi/704/project/project.py",
        "addpay": "",
        "append": "",
        "useSpawn": "false",
        "timer": "",
        "winHide": false,
        "oldrc": false,
        "name": "",
        "x": 560,
        "y": 80,
        "wires": [
            [],
            [],
            []
        ]
    },
    {
        "id": "e5b7b3224af9c3ed",
        "type": "ui_button",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "eabf5f0e79fad3f0",
        "order": 1,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Start LED",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "",
        "payloadType": "str",
        "topic": "topic",
        "topicType": "msg",
        "x": 260,
        "y": 80,
        "wires": [
            [
                "9010c467a36fc991"
            ]
        ]
    },
    {
        "id": "1371f0e938596a07",
        "type": "mqtt in",
        "z": "d757dbb1.993928",
        "name": "",
        "topic": "ldr/value",
        "qos": "2",
        "datatype": "auto",
        "broker": "c3c88cac9a3b8b01",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 260,
        "y": 220,
        "wires": [
            [
                "3e355a445b6e0fd3",
                "da556637b2353829"
            ]
        ]
    },
    {
        "id": "3e355a445b6e0fd3",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "Turn on light by value (5)",
        "func": "//init light status\nvar lightStatus = context.get('lightStatus');\nvar LDRValue = parseInt(parseFloat(msg.payload || 0) * 10)\n\nif(LDRValue > 5 && lightStatus != 0){\n    context.set('lightStatus',0)\n    msg.payload = 0\n    msg.LDRValue = LDRValue\n    msg.lightStatus = lightStatus\n    return msg;\n}else if(LDRValue < 5 && lightStatus != 1){\n    context.set('lightStatus',1)\n    msg.payload = 1\n    msg.LDRValue = LDRValue\n    msg.lightStatus = lightStatus\n    return msg;\n}",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 510,
        "y": 220,
        "wires": [
            [
                "2b1353fe4638747c"
            ]
        ]
    },
    {
        "id": "ce26cec7c47db3e2",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "Init",
        "info": "",
        "x": 250,
        "y": 40,
        "wires": []
    },
    {
        "id": "d8a8512d876f4b11",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "Receive LDR value",
        "info": "",
        "x": 290,
        "y": 160,
        "wires": []
    },
    {
        "id": "5c9012ccc96fa4ed",
        "type": "ui_switch",
        "z": "d757dbb1.993928",
        "name": "",
        "label": "Turn On/Off LEF Bar manually",
        "tooltip": "",
        "group": "738e60bcc9dffdc0",
        "order": 4,
        "width": 0,
        "height": 0,
        "passthru": true,
        "decouple": "false",
        "topic": "topic",
        "topicType": "msg",
        "style": "",
        "onvalue": "1",
        "onvalueType": "num",
        "onicon": "",
        "oncolor": "",
        "offvalue": "0",
        "offvalueType": "str",
        "officon": "",
        "offcolor": "",
        "animate": false,
        "className": "",
        "x": 270,
        "y": 360,
        "wires": [
            [
                "2b1353fe4638747c"
            ]
        ]
    },
    {
        "id": "905657e8e52f4a7c",
        "type": "ui_gauge",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "738e60bcc9dffdc0",
        "order": 2,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "LDR Sensor Status",
        "label": "units",
        "format": "{{LDRValue}}",
        "min": 0,
        "max": 10,
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 750,
        "y": 180,
        "wires": []
    },
    {
        "id": "93f3b07819016961",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "",
        "func": "if(msg.payload == \"power\\n\"){\n    msg.ledStatus = \"ON\"\n}else{\n    msg.ledStatus = \"OFF\"\n}\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 460,
        "y": 620,
        "wires": [
            [
                "bb8c760217c069b8"
            ]
        ]
    },
    {
        "id": "0e117f75d1c65a88",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "Turn On / Off Usb power supply",
        "info": "",
        "x": 250,
        "y": 300,
        "wires": []
    },
    {
        "id": "52347ad7a71bbf61",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "Get Usb power supply status",
        "info": "",
        "x": 240,
        "y": 440,
        "wires": []
    },
    {
        "id": "383f32b5b32f2cb0",
        "type": "mqtt in",
        "z": "d757dbb1.993928",
        "name": "",
        "topic": "moisture/raw",
        "qos": "2",
        "datatype": "auto",
        "broker": "c3c88cac9a3b8b01",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 210,
        "y": 840,
        "wires": [
            [
                "045167db150f4d43",
                "cbcd53533a657fd3"
            ]
        ]
    },
    {
        "id": "b178a9d7a90d77fc",
        "type": "mqtt in",
        "z": "d757dbb1.993928",
        "name": "",
        "topic": "moisture/value",
        "qos": "2",
        "datatype": "auto",
        "broker": "c3c88cac9a3b8b01",
        "nl": false,
        "rap": true,
        "rh": 0,
        "inputs": 0,
        "x": 220,
        "y": 920,
        "wires": [
            [
                "48a2c70de941a25d",
                "9ebdf1de9d88e34f",
                "a86a49e9e15c21ba"
            ]
        ]
    },
    {
        "id": "045167db150f4d43",
        "type": "debug",
        "z": "d757dbb1.993928",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "statusVal": "",
        "statusType": "auto",
        "x": 430,
        "y": 840,
        "wires": []
    },
    {
        "id": "48a2c70de941a25d",
        "type": "debug",
        "z": "d757dbb1.993928",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "statusVal": "",
        "statusType": "auto",
        "x": 430,
        "y": 920,
        "wires": []
    },
    {
        "id": "1505b1e78656cd47",
        "type": "ui_button",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "eabf5f0e79fad3f0",
        "order": 2,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Start soil",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "",
        "payloadType": "str",
        "topic": "topic",
        "topicType": "msg",
        "x": 200,
        "y": 760,
        "wires": [
            [
                "d0041c6298c328e2"
            ]
        ]
    },
    {
        "id": "d0041c6298c328e2",
        "type": "exec",
        "z": "d757dbb1.993928",
        "command": "python3 /home/pi/704/project/soil_moisture.py",
        "addpay": "",
        "append": "",
        "useSpawn": "false",
        "timer": "",
        "winHide": false,
        "oldrc": false,
        "name": "",
        "x": 560,
        "y": 760,
        "wires": [
            [],
            [],
            []
        ]
    },
    {
        "id": "cbcd53533a657fd3",
        "type": "ui_gauge",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "f884bf190fc3de65",
        "order": 2,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "Soil RAW",
        "label": "units",
        "format": "{{msg.payload}}",
        "min": 0,
        "max": "500",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 440,
        "y": 880,
        "wires": []
    },
    {
        "id": "9ebdf1de9d88e34f",
        "type": "ui_gauge",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "f884bf190fc3de65",
        "order": 2,
        "width": 0,
        "height": 0,
        "gtype": "wave",
        "title": "Soil Moisture",
        "label": "%",
        "format": "{{msg.payload}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 450,
        "y": 960,
        "wires": []
    },
    {
        "id": "14ce0e6f73b8884f",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "GPIO 21 = water pump",
        "info": "",
        "x": 500,
        "y": 700,
        "wires": []
    },
    {
        "id": "1a812225485e85a3",
        "type": "rpi-gpio out",
        "z": "d757dbb1.993928",
        "name": "pump",
        "pin": "21",
        "set": true,
        "level": "1",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 790,
        "y": 1000,
        "wires": []
    },
    {
        "id": "a86a49e9e15c21ba",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "ON the pump",
        "func": "if(msg.payload <= 10){\n    msg.payload = 0\n    return msg;\n}",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 450,
        "y": 1000,
        "wires": [
            [
                "d8f8e066ac8ec7e6"
            ]
        ]
    },
    {
        "id": "d9caf5cd1608865e",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "Get moisture value from sensor",
        "info": "",
        "x": 250,
        "y": 700,
        "wires": []
    },
    {
        "id": "a268ed6115478d62",
        "type": "rpi-dht22",
        "z": "d757dbb1.993928",
        "name": "DHT11",
        "topic": "rpi-dht22",
        "dht": "11",
        "pintype": "0",
        "pin": "12",
        "x": 1210,
        "y": 160,
        "wires": [
            [
                "54d75a76b7ccfb27",
                "5816fc3fe1150301"
            ]
        ]
    },
    {
        "id": "995051b5d5038a52",
        "type": "inject",
        "z": "d757dbb1.993928",
        "name": "",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "30",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "x": 1050,
        "y": 160,
        "wires": [
            [
                "a268ed6115478d62"
            ]
        ]
    },
    {
        "id": "70320c16ab6d520a",
        "type": "debug",
        "z": "d757dbb1.993928",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 1610,
        "y": 200,
        "wires": []
    },
    {
        "id": "5816fc3fe1150301",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "Temperature Data",
        "func": "\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 1410,
        "y": 200,
        "wires": [
            [
                "b429553d07a5265f",
                "70320c16ab6d520a"
            ]
        ]
    },
    {
        "id": "54d75a76b7ccfb27",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "Humidity Data",
        "func": "msg.payload = msg.humidity\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 1400,
        "y": 120,
        "wires": [
            [
                "ecb3c473808da59a",
                "d0f359c5b0f91683"
            ]
        ]
    },
    {
        "id": "d0f359c5b0f91683",
        "type": "debug",
        "z": "d757dbb1.993928",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 1610,
        "y": 120,
        "wires": []
    },
    {
        "id": "ecb3c473808da59a",
        "type": "ui_gauge",
        "z": "d757dbb1.993928",
        "name": "Humidity",
        "group": "d57fc265cf16de6a",
        "order": 3,
        "width": 0,
        "height": 0,
        "gtype": "donut",
        "title": "Humidity",
        "label": "%",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 1600,
        "y": 160,
        "wires": []
    },
    {
        "id": "b429553d07a5265f",
        "type": "ui_gauge",
        "z": "d757dbb1.993928",
        "name": "Temperature",
        "group": "d57fc265cf16de6a",
        "order": 2,
        "width": 0,
        "height": 0,
        "gtype": "donut",
        "title": "Temperature",
        "label": "°C",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 1610,
        "y": 240,
        "wires": []
    },
    {
        "id": "b540dfa5ed15b079",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "GPIO 12 = DHT11",
        "info": "",
        "x": 1310,
        "y": 60,
        "wires": []
    },
    {
        "id": "574c6068cedd1db0",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "Get Temperature and Humidity",
        "info": "",
        "x": 1060,
        "y": 60,
        "wires": []
    },
    {
        "id": "d8f8e066ac8ec7e6",
        "type": "trigger",
        "z": "d757dbb1.993928",
        "name": "",
        "op1": "1",
        "op2": "0",
        "op1type": "str",
        "op2type": "str",
        "duration": "10",
        "extend": false,
        "overrideDelay": false,
        "units": "s",
        "reset": "",
        "bytopic": "all",
        "topic": "topic",
        "outputs": 1,
        "x": 630,
        "y": 1000,
        "wires": [
            [
                "1a812225485e85a3"
            ]
        ]
    },
    {
        "id": "db5630e7.83cdc",
        "type": "multipart-decoder",
        "z": "d757dbb1.993928",
        "name": "",
        "ret": "bin",
        "url": "http://0.0.0.0:5001/stream_video",
        "tls": "",
        "delay": 0,
        "maximum": "10000000",
        "blockSize": "1",
        "x": 1250,
        "y": 480,
        "wires": [
            [
                "6535feb.cbf33"
            ]
        ]
    },
    {
        "id": "fb64a032.e945b",
        "type": "ui_template",
        "z": "d757dbb1.993928",
        "group": "b483344015f5b401",
        "name": "Display image",
        "order": 1,
        "width": "6",
        "height": "6",
        "format": "<img width=\"16\" height=\"16\" alt=\"Click Star stream\" src=\"data:image/jpg;base64,{{msg.payload}}\" />\n",
        "storeOutMessages": true,
        "fwdInMessages": true,
        "resendOnRefresh": false,
        "templateScope": "local",
        "className": "",
        "x": 1617.256923675537,
        "y": 480.4166660308838,
        "wires": [
            []
        ]
    },
    {
        "id": "6535feb.cbf33",
        "type": "base64",
        "z": "d757dbb1.993928",
        "name": "Encode",
        "action": "",
        "property": "payload",
        "x": 1440,
        "y": 480,
        "wires": [
            [
                "fb64a032.e945b"
            ]
        ]
    },
    {
        "id": "22b1154347e15eaf",
        "type": "ui_button",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "eabf5f0e79fad3f0",
        "order": 4,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Start Stream",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "",
        "payloadType": "str",
        "topic": "topic",
        "topicType": "msg",
        "x": 1050,
        "y": 480,
        "wires": [
            [
                "db5630e7.83cdc"
            ]
        ]
    },
    {
        "id": "ad12f89622d4ccbb",
        "type": "comment",
        "z": "d757dbb1.993928",
        "name": "Video Streaming",
        "info": "",
        "x": 1060,
        "y": 320,
        "wires": []
    },
    {
        "id": "2c7f103932b3eb55",
        "type": "ui_button",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "eabf5f0e79fad3f0",
        "order": 5,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Start Record",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "",
        "payloadType": "str",
        "topic": "topic",
        "topicType": "msg",
        "x": 1050,
        "y": 580,
        "wires": [
            [
                "4ce3ec85d9a41987"
            ]
        ]
    },
    {
        "id": "27a776fdad572a8b",
        "type": "ui_button",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "eabf5f0e79fad3f0",
        "order": 3,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Start Camera Server",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "",
        "payloadType": "str",
        "topic": "topic",
        "topicType": "msg",
        "x": 1080,
        "y": 380,
        "wires": [
            [
                "38510be0a8562316"
            ]
        ]
    },
    {
        "id": "38510be0a8562316",
        "type": "exec",
        "z": "d757dbb1.993928",
        "command": "python3 /home/pi/704/project/camServer.py",
        "addpay": "",
        "append": "",
        "useSpawn": "false",
        "timer": "",
        "winHide": false,
        "oldrc": false,
        "name": "",
        "x": 1430,
        "y": 380,
        "wires": [
            [],
            [],
            []
        ]
    },
    {
        "id": "4ce3ec85d9a41987",
        "type": "http request",
        "z": "d757dbb1.993928",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": "ignore",
        "url": "http://192.168.0.10:5001/startRecord",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "senderr": false,
        "x": 1250,
        "y": 580,
        "wires": [
            [
                "9df45950b1cc462a"
            ]
        ]
    },
    {
        "id": "746ac5c6f1a6f6df",
        "type": "ui_button",
        "z": "d757dbb1.993928",
        "name": "",
        "group": "eabf5f0e79fad3f0",
        "order": 6,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Stop Record",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "className": "",
        "icon": "",
        "payload": "",
        "payloadType": "str",
        "topic": "topic",
        "topicType": "msg",
        "x": 1050,
        "y": 660,
        "wires": [
            [
                "0b67be37979a0f2a"
            ]
        ]
    },
    {
        "id": "0b67be37979a0f2a",
        "type": "http request",
        "z": "d757dbb1.993928",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": "ignore",
        "url": "http://192.168.0.10:5001/stopRecord",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "senderr": false,
        "x": 1250,
        "y": 660,
        "wires": [
            [
                "802932e5e3ebc08d"
            ]
        ]
    },
    {
        "id": "802932e5e3ebc08d",
        "type": "debug",
        "z": "d757dbb1.993928",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "statusVal": "",
        "statusType": "auto",
        "x": 1450,
        "y": 660,
        "wires": []
    },
    {
        "id": "9df45950b1cc462a",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "Get response filename",
        "func": "var videoFilename = JSON.parse(msg.payload).filename\ncontext.set('videoFilename',videoFilename)\nmsg.videoFilename = videoFilename\nreturn msg",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 1500,
        "y": 580,
        "wires": [
            [
                "b4934ed1da6486fd"
            ]
        ]
    },
    {
        "id": "b4934ed1da6486fd",
        "type": "change",
        "z": "d757dbb1.993928",
        "name": "save filename",
        "rules": [
            {
                "t": "set",
                "p": "videoFilename",
                "pt": "flow",
                "to": "videoFilename",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 1720,
        "y": 580,
        "wires": [
            []
        ]
    },
    {
        "id": "f6373f2499c5f56d",
        "type": "http in",
        "z": "d757dbb1.993928",
        "name": "",
        "url": "/download",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 1060,
        "y": 840,
        "wires": [
            [
                "390536a76436477b"
            ]
        ]
    },
    {
        "id": "beae6d2e10d9f45c",
        "type": "http response",
        "z": "d757dbb1.993928",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 1850,
        "y": 840,
        "wires": []
    },
    {
        "id": "390536a76436477b",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "Get the file name",
        "func": "var lightStatus = flow.get(\"videoFilename\");\nmsg.filename = \"/home/pi/\"+lightStatus;\nmsg.contentdisposition = \"attachment; filename=\\\"\" + (\"/home/pi/704/project/\"+lightStatus).replace(/^.*(\\\\|\\/|\\:)/, '') + \"\\\"\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 1310,
        "y": 840,
        "wires": [
            [
                "c9d2c62a56dd3a8e",
                "512bdade4925fe80"
            ]
        ],
        "outputLabels": [
            "Folder selected"
        ]
    },
    {
        "id": "c9d2c62a56dd3a8e",
        "type": "file in",
        "z": "d757dbb1.993928",
        "name": "",
        "filename": "",
        "format": "",
        "chunk": false,
        "sendError": false,
        "encoding": "none",
        "allProps": false,
        "x": 1500,
        "y": 840,
        "wires": [
            [
                "5c22e373e0f63fad",
                "e39ee01ad6ec5dfb"
            ]
        ]
    },
    {
        "id": "5c22e373e0f63fad",
        "type": "change",
        "z": "d757dbb1.993928",
        "name": "Set Headers",
        "rules": [
            {
                "t": "set",
                "p": "headers",
                "pt": "msg",
                "to": "{}",
                "tot": "json"
            },
            {
                "t": "set",
                "p": "headers.content-type",
                "pt": "msg",
                "to": "text/csv",
                "tot": "str"
            },
            {
                "t": "set",
                "p": "headers.Content-Disposition",
                "pt": "msg",
                "to": "contentdisposition",
                "tot": "msg"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 1670,
        "y": 840,
        "wires": [
            [
                "beae6d2e10d9f45c"
            ]
        ]
    },
    {
        "id": "e39ee01ad6ec5dfb",
        "type": "debug",
        "z": "d757dbb1.993928",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 1670,
        "y": 940,
        "wires": []
    },
    {
        "id": "512bdade4925fe80",
        "type": "debug",
        "z": "d757dbb1.993928",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "true",
        "targetType": "full",
        "statusVal": "",
        "statusType": "auto",
        "x": 1370,
        "y": 960,
        "wires": []
    },
    {
        "id": "5d55e1a81bc59dbd",
        "type": "ui_template",
        "z": "d757dbb1.993928",
        "group": "eabf5f0e79fad3f0",
        "name": "Download Video",
        "order": 7,
        "width": 0,
        "height": 0,
        "format": "<button \n    onClick=\"window.open('/download?filename=/home/pi/704/project/','_blank')\"\n    class=\"md-raised md-button md-ink-ripple\">\n    Download Video\n</button>\n\n",
        "storeOutMessages": true,
        "fwdInMessages": true,
        "resendOnRefresh": true,
        "templateScope": "local",
        "className": "nr-dashboard-button _md visible",
        "x": 1060,
        "y": 760,
        "wires": [
            []
        ]
    },
    {
        "id": "da556637b2353829",
        "type": "function",
        "z": "d757dbb1.993928",
        "name": "Get LDR Value",
        "func": "var LDRValue = parseInt(parseFloat(msg.payload || 0) * 10)\nmsg.LDRValue = LDRValue\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 480,
        "y": 180,
        "wires": [
            [
                "905657e8e52f4a7c"
            ]
        ]
    },
    {
        "id": "738e60bcc9dffdc0",
        "type": "ui_group",
        "name": "LED System",
        "tab": "ed1c40c3e1073756",
        "order": 2,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "eabf5f0e79fad3f0",
        "type": "ui_group",
        "name": "Control",
        "tab": "ed1c40c3e1073756",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "c3c88cac9a3b8b01",
        "type": "mqtt-broker",
        "name": "",
        "broker": "localhost",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "60",
        "cleansession": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "sessionExpiry": ""
    },
    {
        "id": "f884bf190fc3de65",
        "type": "ui_group",
        "name": "Soil",
        "tab": "ed1c40c3e1073756",
        "order": 4,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "d57fc265cf16de6a",
        "type": "ui_group",
        "name": "Room",
        "tab": "ed1c40c3e1073756",
        "order": 3,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "b483344015f5b401",
        "type": "ui_group",
        "name": "Stream",
        "tab": "ed1c40c3e1073756",
        "order": 5,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "ed1c40c3e1073756",
        "type": "ui_tab",
        "name": "Smart Garden System",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    }
]
   ```
4. Access http://localhost:1880/ui for the control dashboard
   
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Alvis Lai - alvislaish@gamil.com, 
Kenny Chan - arkin803@gmail.com

Project Link: [https://github.com/AlvisLai/Smart-Garden-System](https://github.com/AlvisLai/Smart-Garden-System)

   
   
   
   
   
   
   
   