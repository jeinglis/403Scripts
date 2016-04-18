
categories = []
categories.append([
    "corrective",
    "fixed",
    "fixing",
    "fix",
    "debug",
    "debugging",
    "debugged",
    "bug", 
    "debug", 
    "fix", 
    "broken", 
    "work", 
    "edit",
    "problem", 
    "error", 
    "typo", 
    "exception", 
    "try", 
    "catch"])
categories.append([
    'adaptive',
    'platform',
    'hardware',
    'test',
    'testing',
    'change',
    'changing',
    'tested',
    'changed',
    'platform',
    'build',
    'test',
    'doc',
    'documentation',
    'international',
    'config',
    'data',
    'readme',
    'info',
    'comment',
    'description',
    'src',
    'note'])
categories.append([
    'perfective',
    'reformat',
    'reformatted',
    'moved',
    'moving',
    'move',
    'rename',
    'renaming',
    'renamed',
    'refactor',
    'refactored',
    'refactoring',
    'delete',
    'deleted',
    'deleting',
    'remove',
    'removed',
    'removing',
    'clean',
    'whitespace',
    'indent',
    'spacing',
    'refactor',
    'move',
    'replace',
    'remove',
    'order',
    'redundant',
    'tidy',
    'rework',
    'patch',
    'move'])
categories.append([
    "nonfunctional",
    "clean",
    "cleaning",
    "cleaned",
    "license",
    "lisense",
    "copyright",
    "author",
    "authorship",
    "rename",
    "renaming",
    "renamed",
    "token",
    "merge",
    "merging",
    "merged"])
categories.append([
    "implementation",
    "initialize",
    "initializing",
    "initialized",
    "importing",
    "imported",
    "add",
    "adding",
    "added",
    "feature",
    "external",
    "language",
    "requirements"])

projects = [
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
    #"doom3.gpl",
    "jquery",
    "xbmc",
    "reddit",
    "rails",
    "ThinkUp",
    "bitcoin",
    "scala",
    "mongo",
    "akka",
    "shiny",
    "xbmc",
    "reddit",
    #"legacy-homebrew",
    #"node"
    ]

outFile = open("Commit_categorizations.txt", 'w')

for project in projects:
    corrective = []
    adaptive = []
    perfective = []
    implementation = []
    nonfunctional = []
    uncategorized = []
    
    with open(project + "_commitlog.txt") as f:
            for line in f:
                categorized = 0
                line.lower()
                if line.startswith('    '):
                    if line.startswith('    merge'):
                        continue
                    else:
                        for cat in categories:
                            if(categorized == 1):
                                break
                            for term in cat:
                                #gets here
                                if term in line: 
                                    #gets here
                                    if(cat[0] == 'corrective'):
                                        corrective.append(str(term))
                                        categorized = 1
                                        break
                                    elif(cat[0] == 'adaptive'):
                                        adaptive.append(str(term))
                                        categorized = 1
                                        break
                                    elif(cat[0] == 'perfective'):
                                        perfective.append(str(term))
                                        categorized = 1
                                        break
                                    elif(cat[0] == 'implementation'):
                                        implementation.append(str(term))
                                        categorized = 1
                                        break
                                    elif(cat[0] == 'nonfunctional'):
                                        nonfunctional.append(str(term))
                                        categorized = 1
                                        break
                                    else:
                                        uncategorized.append(line)

    outFile.write('\n')
    # outFile.write('****************'+ project + '******************\n')
    # outFile.write('Corrective Commits: ' + str(len(corrective)) +'\n' )
    # outFile.write('words found:\n')
    for item in corrective:
        outFile.write("%s" % item)
        outFile.write('\n')

    # outFile.write('adaptive Commits: ' + str(len(adaptive)) +'\n' )
    # outFile.write('words found:\n')
    for item in adaptive:
        outFile.write("%s" % item)
        outFile.write('\n')

    # outFile.write('perfective Commits: ' + str(len(perfective)) +'\n' )
    # outFile.write('words found:\n')
    for item in perfective:
        outFile.write("%s" % item)
        outFile.write('\n')

    # outFile.write('implementation Commits: ' + str(len(implementation)) +'\n' )
    # outFile.write('words found:\n')
    for item in implementation:
        outFile.write("%s" % item)
        outFile.write('\n')

    # outFile.write('nonfunctional Commits: ' + str(len(nonfunctional)) +'\n' )
    # outFile.write('words found:\n')
    for item in nonfunctional:
        outFile.write("%s" % item)
        outFile.write('\n')

    # outFile.write('uncategorized Commits: ' + str(len(uncategorized)) +'\n' )
    # outFile.write('uncategorized commit: \n')
    for item in uncategorized:
        outFile.write("%s" % item)
        outFile.write('\n')
    # outFile.write('//////////////////////////////////////////////////')




            
                 
