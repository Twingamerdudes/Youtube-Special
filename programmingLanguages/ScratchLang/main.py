from asyncio.windows_events import NULL
import json
from textwrap import indent

spriteNames = []
templete='''
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "variables": { "`jEk@4|i[#Fk?(8x)AV.-my variable": ["my variable", 0] },
      "lists": {},
      "broadcasts": {},
      "blocks": {},
      "comments": {},
      "currentCostume": 0,
      "costumes": [
        {
          "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
          "name": "backdrop1",
          "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
          "dataFormat": "svg",
          "rotationCenterX": 240,
          "rotationCenterY": 180
        }
      ],
      "sounds": [],
      "volume": 100,
      "layerOrder": 0,
      "tempo": 60,
      "videoTransparency": 50,
      "videoState": "on",
      "textToSpeechLanguage": null
    }
  ],
  "monitors": [],
  "extensions": [],
  "meta": { "semver": "3.0.0", "vm": "0.2.0", "agent": "" }
}
'''
spriteTemplete='''
    {
        "isStage": false,
        "name": "Sprite1",
        "variables": {},
        "lists": {},
        "broadcasts": {},
        "blocks": {},
        "comments": {},
        "currentCostume": 0,
        "costumes": [
          {
            "assetId": "cd21514d0531fdffb22204e0ec5ed84a",
            "name": "costume1",
            "bitmapResolution": 1,
            "md5ext": "cd21514d0531fdffb22204e0ec5ed84a.svg",
            "dataFormat": "svg",
            "rotationCenterX": 44,
            "rotationCenterY": 44
          }
        ],
        "sounds": [],
        "volume": 100,
        "layerOrder": 1,
        "visible": true,
        "x": 0,
        "y": 0,
        "size": 100,
        "direction": 90,
        "draggable": false,
        "rotationStyle": "all around"
    }
'''
jsonData = json.loads(templete)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
print("File name: ")
name = input()
f = open(name, "r")
data = f.read()
f.close()
code = data.split("\n")
for i in range(len(code)):
    code[i] = code[i].strip()
    if code[i][0] == "#":
        continue
    if code[i][0:4] == "make":
        if code[i][5:11] == "sprite" :
            sprite = json.loads(spriteTemplete)
            sprite["blocks"]["c"] = {"opcode": "event_whenflagclicked", "next": "a", "inputs": {}, "fields": {}, "shadow": False, "topLevel": True, "x": 0, "y": 0}
            sprite["name"] = code[i][12:]
            jsonData["targets"].insert(30, sprite)
            spriteNames.append(sprite["name"])
    if code[i][0:4] == "loop":
        if code[i][5:9] == "true":
            #add a forever loop to the sprite
            sprite["blocks"]["c"]["next"] = "b"
            sprite["blocks"]["b"] = {"opcode": "control_forever", "next": "null", "parent": "a", "inputs": {"SUBSTACK": [2, "d"] }, "fields": {}, "shadow": False, "topLevel": False}
            temp = {"opcode": "control_forever", "next": "null", "parent": "a", "inputs": {"SUBSTACK": [2, "d"] }, "fields": {}, "shadow": False, "topLevel": False}
        else:
            #add a repeat num loop
            try:
                if temp != None:
                    temp["next"] = "b"
                    sprite["blocks"]["b"] = temp
                if(temp == None):
                    sprite["blocks"]["c"]["next"] = "d"
                if temp == None:
                    sprite["blocks"]["d"] = {"opcode": "control_repeat", "next": "null", "parent": "a", "inputs": {"TIMES": [1, [6, code[i][5:]]]}, "fields": {}, "shadow": False, "topLevel": False}
                else:
                    sprite["blocks"][letters[i]] = {"opcode": "control_repeat", "next": "null", "parent": letters[i-1], "inputs": {"TIMES": [1, [6, code[i][5:]]]}, "fields": {}, "shadow": False, "topLevel": False}
            except:
                sprite["blocks"]["c"]["next"] = "d"
                sprite["blocks"]["d"] = {"opcode": "control_repeat", "next": "null", "parent": "a", "inputs": {"TIMES": [1, [6, code[i][5:]]]}, "fields": {}, "shadow": False, "topLevel": False}
            temp = {"opcode": "control_repeat", "next": "null", "parent": "a", "inputs": {"TIMES": [1, [6, code[i][5:]]]}, "fields": {}, "shadow": False, "topLevel": False}
jsonData = json.dumps(jsonData, indent=2)
print(jsonData)