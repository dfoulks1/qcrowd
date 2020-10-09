#!/usr/bin/env python
import requests
import sys
import getpass

class CrowdServer:
    
    def __init__(self, stub, username, password):

        self.data = {
                'stub': stub,
                'username': username,
                'password': password
                }

        self.crowd = requests.Session()
        self.crowd.headers.update = {
            'Content-Type': 'application/json', 
            'Accept': 'application/json',
            }
        auth_data = { 'value': self.data['password'] }
        ext = "authentication?username=%s" % self.data['username']
        uri = "%s/%s" % (self.data['stub'], ext)
        req = requests.Request('POST', uri, data=auth_data, auth=('crowd', self.data['password']))
        auth_req = req.prepare()
        r = self.crowd.send(auth_req)
       
        print(r.status_code)


    def get_user(self, search_term):
        ext = "/console/secure/user/browse.action?search=%s" % search_term
        uri = "%s/%s" % (self.data['stub'], ext)
        resp = self.crowd.get(uri)
        print(resp.status_code)        
        print(resp.response)







url = 'https://crowd.apache.org/crowd/rest/usermanagement/latest'
uname = input("Crowd Username: ")
pword = getpass.getpass("Crowd Password: ")

crowd = CrowdServer(url, uname, pword)
