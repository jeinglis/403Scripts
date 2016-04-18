import subprocess
#for each commit in text file
#grab dates of projects

urls = [ 
    "https://github.com/hsarvesthq/chosen",
    "https://github.com/slimphp/Slim",
    "https://github.com/twitter/gizzard",
    "https://github.com/JakeWharton/ActionBarSherlock",
    "https://github.com/thoughtbot/paperclip",
    "https://github.com/mitsuhiko/flask",
    "https://github.com/ariya/phantomjs",
    "https://github.com/tornadoweb/tornado",
    "https://github.com/scalatra/scalatra",
    "https://github.com/sbt/sbt",
    "https://github.com/twitter/finagle",
    "https://github.com/antirez/redis",
    "https://github.com/hbons/SparkleShare",
    "https://github.com/ServiceStack/ServiceStack",
    "https://github.com/sebastianbergmann/phpunit",
    # brandon & tanner
    "https://github.com/facebook/facebook-android-sdk",
    "https://github.com/pockethub/PocketHub",
    "https://github.com/AutoMapper/AutoMapper",
    "https://github.com/bitcoin/bitcoin",
    "https://github.com/TTimo/doom3.gpl",
    "https://github.com/jquery/jquery",
    "https://github.com/xbmc/xbmc",
    "https://github.com/reddit/reddit",
    "https://github.com/rails/rails",
    "https://github.com/scala/scala",
    #jon & karson
    "https://github.com/ThinkUpLLC/ThinkUp",
    "https://github.com/bitcoin/bitcoin",
    "https://github.com/scala/scala",
    "https://github.com/mongodb/mongo",
    "https://github.com/akka/akka",
    "https://github.com/rstudio/shiny",
    "https://github.com/xbmc/xbmc",
    "https://github.com/reddit/reddit",
    "https://github.com/Homebrew/legacy-homebrew",
    "https://github.com/nodejs/node"
		]

repoNames = [ 

    "chosen",
    "Slim",
    "gizzard",
    "ActionBarSherlock",
    "paperclip",
    "flask",
    "phantomjs",
    "tornado",
    "scalatra",
    "sbt",
    "finagle",
    "redis",
    "SparkleShare",
    "ServiceStack",
    "phpunit",

    "facebook-android-sdk",
    "PocketHub",
    "AutoMapper",
    #"bitcoin",
    "doom3.gpl",
    "jquery",
    "xbmc",
    "reddit",
    "rails",
    #"scala",

    "ThinkUp",
    "bitcoin",
    "scala",
    "mongo",
    "akka",
    "shiny",
    "xbmc",
    "reddit",
    "legacy-homebrew",
    "node"

	]

index = 0
for repoName in repoNames:
	outputtotextfile = 1
	gotcommit1 = 0
	gotcommit2 = 0 
	with open(repoName + "_largestcommits.txt") as f:
		count = 0 
		for line in f:

			if(line.startswith("1 percent of commits")):
				numcommits = int(float(line[21:]))
			if(line.startswith("commit number: ")):
				commitNumber = int(float(line[15:]))
			elif(line.startswith("commitid1")):
				commitid1 = line[11:17]
				gotcommit1 = 1
			elif(line.startswith("commitid2")):
				commitid2 = line[11:17]
				gotcommit2 = 1
			elif(gotcommit1 and gotcommit2):
				gotcommit1 = 0
				gotcommit2 = 0
				if(commitNumber==1):
					subprocess.call(["git", "clone", urls[index]])

				process = subprocess.Popen(["git", "-C", repoNames[index], "diff", commitid2, commitid1 ], stdout=subprocess.PIPE)
				out, err = process.communicate()
				
				fname = open(repoName+"_gitdiff"+str(commitNumber)+".txt",'w')
				for diffline in out.splitlines():
					fname.write(diffline)
					fname.write('\n')
				fname.close()
				
				if(commitNumber == numcommits):
					subprocess.call(["rm", "-rf", repoName])
				
	index = index + 1

				

