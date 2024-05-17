# ⚠️ Prometheus Twilio Call ⚠️

  A simple script to integrate Prometheus/Alertmanager with twilio call tool.   

-----
## Environment Variables

~~~
ACCOUNT_SID
AUTH_TOKEN
FROM_NUMBER
TO_NUMBERS
~~~

 To find the value for this variables you can read the following documentation from Twilio:
 https://help.twilio.com/articles/14726256820123-What-is-a-Twilio-Account-SID-and-where-can-I-find-it-

-----

## Running on Docker

~~~
$ docker run -p 5000:5000 -e ACCOUNT_SID="<YOUR-ACCOUNT-SID>" -e AUTH_TOKEN="<YOUR-AUTH-TOKEN>" -e FROM_NUMBER="<YOUR-FROM-NUMBER>" -e TO_NUMBERS="['+999999999999', '+999999999999']" tibursio/prometheus-twilio-call:<TAG>
~~~

-----

## Test the application

~~~
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "alerts": [
          {
            "annotations": {
              "description": "HELPPPPPPPPPP!!!!!!"
            }
          }
        ]
      }' \
  http://<IP>:<PORT>/alert
~~~

-----

## Integration on AlertManager

~~~
- name: twiliocall
  webhook_configs:
     - url: '<IP/SERVICE>:5000/alert'
~~~

