
import json
import requests
from requests.auth import HTTPBasicAuth

def send(structure):
    response = requests.post('https://workshop1210.waxlrs.com/TCAPI/statements',
        data=json.dumps(structure),
        auth=HTTPBasicAuth('q8Mwyl4Lp9PgdFCodetq', 'uGEvrvspI6veJod2eaii'),
        headers={
            'X_EXPERIENCE_API_VERSION': '0.95',
            'content-type': 'application/json'
        }
    )
    print response.status_code, response.text



send([
   {
      "verb":{
         "id":"http://example.com/verbs/sailed",
         "display":{
            "en":"sailed"
         }
      },
      "result":{
         "completion":True,
         "success":True
      },
      "context":{
         "contextActivities":{
            "other":{
               "id":"http://example.com/activities/oceanrelated"
            }
         },
         "instructor":{
            "mbox":"mailto:sam@example.com",
            "name":"Sam"
         }
      },
      "timestamp":"2011-05-25T20:34:05.787000+00:00",
      "object":{
         "id":"http://example.com/activities/sailingcourse"
      },
      "actor":{
         "objectType":"Group",
         "member":[
            {
               "mbox":"mailto:a@b.com",
               "name":"Bob"
            },
            {
               "mbox":"mailto:b@c.com",
               "name":"Jones"
            }
         ],
         "name":"Team ABC"
      }
   },
   {
      "verb":{
         "id":"http://example.gov/verbs/transported",
         "display":{
            "en":"transported"
         }
      },
      "context":{
         "contextActivities":{
            "grouping":{
               "id":"http://example.com/topics/lading"
            }
         }
      },
      "timestamp":"2011-06-25T20:34:05.787000+00:00",
      "object":{
         "id":"http://example.com/coconut"
      },
      "actor":{
         "objectType":"Agent",
         "openid":"https://africanoreuropean.com",
         "name":"Martin Hirun"
      }
   }
])