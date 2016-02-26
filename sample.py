import urllib2
import json
data = ""
datadetails =""

def usersTotal():
    """
        Returns TOTAL number of users.
    """
    url = 'https://api.github.com/orgs/facebook/repos'
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    if 'error' in data:
        print 'errors are scanned in data'
    counter = 0
    for name in data:
        counter= counter + 1
    #print 'TOTAL number of users'
    return counter

def publicRepos():
   """
        Returns public repositories.
    """
   secondurl = 'https://api.github.com/users/facebook'
   json_objs = urllib2.urlopen(secondurl)
   datadetails = json.load(json_objs)
   if 'error' in datadetails:
        print 'errors are scanned in data'
   for key, value in datadetails.iteritems():
        if 'public_repos' in key:
           # print 'public repositories'
            return value

def forksUser():
    """
        Returns no of forks for codemod user.
    """
    thirdurl = 'https://api.github.com/orgs/facebook/repos'
    json_objs = urllib2.urlopen(thirdurl)
    singleuser = json.load(json_objs)
    for info in singleuser:
        if 'name' in info:
            if info['name'] == 'codemod':
                #print 'no of forks for codemod user'
                return info['forks']
	

def commitCount():
    """
       Returns number of commits of codemod user.
    """
    foururl = 'https://api.github.com/repos/facebook/codemod/commits'
    json_objs = urllib2.urlopen(foururl)
    usercommits = json.load(json_objs)
    commitcount = 0
    for commit in usercommits:
        commitcount = commitcount + 1
	    #print 'number of commits of codemod user'
        return commitcount



def main():
 print """<html>
		<head>
		<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>"""

 print """<script type="text/javascript">
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ["TOTAL forks count", "count", { role: "style" } ],"""
 users = usersTotal()
 repos = publicRepos()
 forks = forksUser()
 commits = commitCount()
 print " [\"TOTAL number of users in organisation\", %d , \"#b87333\"]," %users
 print " [\"public repositories of facebook\", %d, \"silver\"]," %repos
 print " [\"no of forks for codemod user\", %d, \"gold\"],"%forks
 print " [\"commits of codemod user\", %d, \"color: #e5e4e2\"]," %commits
 print """  ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

      var options = {
        title: "GIT API data of facebook",
        width: 600,
        height: 400,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
      chart.draw(view, options);
  }
  </script>"""
print """<div id="barchart_values" style="width: 900px; height: 300px;"></div>
    </script>
  </head>
  <body>
    <div id="columnchart_material" style="width: 900px; height: 500px;"></div>
    <table border="1">"""

print "</table>"
print """</table>
  </body>
</html>"""

if __name__ == '__main__':
    main()
