#!/usr/bin/python
import subprocess, re, os, sys

scriptPath = os.path.dirname(os.path.realpath(sys.argv[0]))
execfile(scriptPath+"/config.py")

auth_command = "curl --cert \"%s\" -d app=11 -si https://auth.startssl.com" % (scriptPath+"/"+CERTFILE)
output = subprocess.check_output(auth_command, shell=True)
#print output
m = re.search(r"STARTSSLID=[a-zA-Z0-9]+", output)
if not m:
	print "Error"
	os.exit(1)

token = m.group()
print "Auth Token: ", token
with open(scriptPath+'/startssl_cookie.txt', 'w') as outfile:
	outfile.write(token)



