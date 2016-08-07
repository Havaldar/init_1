#!/usr/bin/python

from subprocess import call
import requests as req

call(['cd'])
call(['/usr/bin/ruby', '-e', "'$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)'"])
call(['brew', 'install', 'git'])
call(['brew', 'install', 'node'])
call(['brew', 'install', 'npm'])
call(['brew', 'install', 'wget'])
call(['npm', 'install', '-g', 'express'])
call(['sudo', 'easy_install', 'pip'])
call(['sudo', 'pip', 'install', 'virtualenv'])
username = raw_input('Github username: ')
r = req.get('https://api.github.com/users/' + username + '/repos')
urls = [repo[u'clone_url'].encode() for repo in r.json()]
for url in urls:
	call(['git','clone',url])