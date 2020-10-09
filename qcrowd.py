#!/usr/bin/env python -B
import crowd_api
import getpass
import sys

url = "https://crowd.apache.org/crowd/rest/usermanagement/latest"
app_name = "crowd"
app_user = input("Crowd User: ")
app_password = getpass.getpass("Crowd Password: ")
crowd = crowd_api.CrowdAPI(api_url = url, app_name = app_name, app_password = app_password)
req = crowd.get_user(username = sys.argv[1])
print(req)
