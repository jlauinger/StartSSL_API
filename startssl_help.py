#!/usr/bin/python

import sys
from pydoc import pager

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "auth":
            help_auth()
        elif sys.argv[1] == "getcerts":
            help_getcerts()
        elif sys.argv[1] == "validate":
            help_validate()
        elif sys.argv[1] == "certify":
            help_certify()
        else:
            help_usage()
    else:
        help_usage()

def help_usage():
    text = "StartSSL command line interface\n\n"
    text += "Here follows the ultimate documentation of startssl cli\n\n"
    text += "Documentation for specific commands is available by calling\n"
    text += "startssl help <command>\n\n"
    text += "For example:\n"
    text += "startssl help auth\n"
    text += "startssl help getcerts\n"
    text += "startssl help validate\n"
    text += "startssl help certify\n"
    pager(text)    

def help_auth():
    print "StartSSL command line interface"
    print
    print "Usage: startssl auth"
    print
    print "Authenticates against StartSSL as if you would sign in using a browser."
    print "You must have your client login certificate somewhere and provide its path"
    print "in config.py."
    print "Use this command before using any other startssl command."

def help_getcerts():
    print "StartSSL command line interface"
    print
    print "Usage: startssl getcerts [-v]"
    print "       startssl getcerts <number>"
    print
    print "getcerts without parameters prints a list of your certificates. If you would"
    print "like to update the list cached locally, provide the -v flag."
    print "You can download a certificate by providing its number after the command, as in"
    print "startssl getcerts 1"

def help_validate():
    print "StartSSL command line interface"
    print
    print "Usage: startssl validate [<domain> [<token>]]"
    print
    print "validate without parameters prints a list of your validated domains. To validate"
    print "a new domain, provide it as first parameter, e.g. startssl validate example.com"
    print "You will then be prompted what to do."
    print "To resume a previous validation session, provide the authentification token sent"
    print "to you by mail in addition to the domain name."

def help_certify():
    print "StartSSL command line interface"
    print
    print "Usage: startssl certify <domainlist>"
    print "       startssl certify <key> <domainlist> <certificate>"
    print
    print "Use startssl certify to generate certificates of validates domains. You must"
    print "provide a file with domains and subdomains to include in the new certificate in"
    print "a domain list file. This file has to be named <slug>_domains.txt, where <slug>"
    print "can be anything you want."
    print "certify with only a domain list will generate a private key named <slug>_privatekey_<date>.pem"
    print "and store the signed certificate in <slug>_cert_<date>.pem"
    print "You can specify the file names of key and certificate by providing them as"
    print "first and third argument."

main()
