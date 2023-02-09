import json

# This string is not a valid JSON object
invalid_json_string = """{
  "Amount": "float",
  "Class": "int",
  "Time": "int",
  "V1": "float",
  "V10": "float",
  "V11": "float",
  "V12": "float",
  "V13": "float",
  "V14": "float",
  "V15": "float",
  "V16": "float",
  "V17": "float",
  "V18": "float",
  "V19": "float",
  "V2": "float",
  "V20": "float",
  "V21": "float",
  "V22": "float",
  "V23": "float",
  "V24": "float",
  "V25": "float",
  "V26": "float",
  "V27": "float",
  "V28": "float",
  "V3": "float",
  "V4": "float",
  "V5": "float",
  "V6": "float",
  "V7": "float",
  "V8": "float",
  "V9": "float"
}
"""

try:
    json_object = json.loads(invalid_json_string)
except json.decoder.JSONDecodeError as e:
    print("Error:", e)