#!/usr/bin/env python
import requests
import sys
import getpass

class CrowdWork:


    def __init__(self, stub, username, password):

        self.data = {
                'stub': stub,
                'username': username,
                'password': password,
                }

        self.crowd = requests.Session()
        self.crowd.headers.update = {
            'Content-Type': 'application/json', 
            'Accept': 'application/json',
            }

        auth_data = {
            "username": self.data['username'],
            "password": self.data['password'],
            "validation-factors": {
                "validationFactors": [
                    {
                        "name": "remote_address",
                        "value": "127.0.0.1"
                    }
                    ]
                }
            }

 
        ext = "1/session"
        uri = "%s/%s" % (self.data['stub'], ext)

        req = requests.Request('POST', uri, data=auth_data)
        auth_req = req.prepare()
        resp = self.crowd.send(auth_req)

        print(resp.status_code)
        print(resp.content)


url = 'https://crowd.apache.org/crowd/rest/usermanagement'
uname = input("Username: ")
pword = getpass.getpass("Password: ")

crowd = CrowdWork(url, uname, pword)
