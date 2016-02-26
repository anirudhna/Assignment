
import urllib2
import json


def user_details():
    """
       Returns basic info of codemod user.
    """
    url = 'https://api.github.com/orgs/facebook/repos'
    json_obj = urllib2.urlopen(url)
    userdata = json.load(json_obj)
    if 'error' in userdata:
        print 'errors are scanned in data'
    for data in userdata:
        if 'name' in data:
            if data['name'] == 'codemod':
                print 'language used'
                print data['language']
                print 'number of watchers'
                print data['watchers']
                print 'git url'
                print data['git_url']
                print 'open issues'
                print data['open_issues']
                print 'permissions for user'
                print 'push'
                print data['permissions']['push']
                print 'pull'
                print data['permissions']['pull']

if __name__ == "__main__":
	user_details()
