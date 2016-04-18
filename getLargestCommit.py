from operator import itemgetter

urls = [ 
  #  "https://github.com/hsarvesthq/chosen",
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
 #   "https://github.com/TTimo/doom3.gpl",
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
   # "chosen",
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
    #"doom3.gpl",
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

for repoName in repoNames: 
	commitidsfirst = [] 
	commitidssecond = [] 
	filecounts = [] 
            comment = []

	comments_and_counts = []

	def getKey(item):
		return item[2]

	with open(repoName + "_commitlog.txt") as f:
		
		#fname = open()

		counter = -1

		#for line in lines:
		for line in f:
			if line.startswith('commit'):
				if (counter == 0):
					commitidsfirst.append(line[7:len(line)-1])
					commitidssecond.append(line[7:len(line)-1])

					#print(commitidsfirst)
					#print(commitidssecond)
				elif(counter % 2 == 0):
					commitidsfirst.append(line[7:len(line)-1])
				else:
					commitidssecond.append(line[7:len(line)-1])
				
			elif line.startswith('File count'):
				filecounts.append(int(line[12:len(line)-1]))
				
			 elif line.startswith('    '):
			 	if line.lower().startswith('    merge'):
			 	   continue
				else
				    comment.append()


			counter = counter + 1
		

		index = 0
		for commitidstart in commitidsfirst:
			tup = (comment[index], filecounts[index])
			comments_and_counts.append(tup)
			index = index + 1

		comments_and_counts = sorted(comments_and_counts,key=getKey, reverse=True)

	
	fname = open( repoName + "_largestcommits.txt",'w')
	fname.write('Number of commits ')
	fname.write(str(len(comments_and_counts)))
	fname.write('\n1 percent of commits ')
	numberofcommits = len(comments_and_counts)*0.01
	fname.write(str(numberofcommits))
	fname.write('\n')
	commitcounter = 1
	for line in comments_and_counts:
		if(commitcounter >= numberofcommits):
			break
		fname.write('\n')
		fname.write("commit number: ")
		fname.write(str(commitcounter))
		fname.write('\ncomment: ')
		fname.write(line[0])
		fname.write('\nFiles Changed: ')
		fname.write(str(line[1]))
		fname.write(' ')
		fname.write('\n')
		commitcounter = commitcounter + 1



