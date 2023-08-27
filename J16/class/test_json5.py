# java ....>
# دیتا های مورد علاقه API
# میتونه داخل لیست نباشه و توی {} باشه

# Serialization   / Encode
# DeSerialization  / Decode

import json

data = {
    "president" : {
        "1990" : ""
        ""
    }
}

with open('J16\class\class\test_json','w') as json_file:
    json.dump(data,json_file)
    # dumbs دیک رو تبدیل به استرینگ میکنه 