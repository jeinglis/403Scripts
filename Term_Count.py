corrective = 0
fixed = 0
fixing = 0
fix = 0
debug = 0
debugging = 0
debugged = 0
bug = 0 
debug = 0 
fix = 0 
broken = 0 
work = 0 
edit = 0
problem = 0 
error = 0 
typo = 0 
exception = 0 
tryy = 0 
catch = 0
adaptive = 0
platform = 0
hardware = 0
test = 0
testing = 0
change = 0
changing = 0
tested = 0
changed = 0
platform = 0
build = 0
test = 0
doc = 0
documentation = 0
international = 0
config = 0
data = 0
readme = 0
info = 0
comment = 0
description = 0
src = 0
note = 0
perfective = 0
reformat = 0
reformatted = 0
moved = 0
moving = 0
move = 0
rename = 0
renaming = 0
renamed = 0
refactor = 0
refactored = 0
refactoring = 0
delete = 0
deleted = 0
deleting = 0
remove = 0
removed = 0
removing = 0
clean = 0
whitespace = 0
indent = 0
spacing = 0
refactor = 0
move = 0
replace = 0
remove = 0
order = 0
redundant = 0
tidy = 0
rework = 0
patch = 0
move = 0
nonfunctional = 0
clean = 0
cleaning = 0
cleaned = 0
license = 0
lisense = 0
copyright = 0
author = 0
authorship = 0
rename = 0
renaming = 0
renamed = 0
token = 0
merge = 0
merging = 0
merged = 0
implementation = 0
initialize = 0
initializing = 0
initialized = 0
importing = 0
imported = 0
add = 0
adding = 0
added = 0
feature = 0
external = 0
language = 0
requirements = 0

terms = [corrective,fixed,fixing,fix,debug,debugging,debugged,bug, debug, fix, broken, work, edit,problem, error, typo, exception, 
    tryy, catch,adaptive,platform,hardware,test,testing,change,changing,tested,changed,platform,build,test,doc,documentation,international,
    config,data,readme,info,comment,description,src,note,perfective,reformat,reformatted,moved,moving,move,rename,renaming,renamed,
    refactor,refactored,refactoring,delete,deleted,deleting,remove,removed,removing,clean,whitespace,indent,spacing,refactor,move,replace,
    remove,order,redundant,tidy,rework,patch,move,nonfunctional,clean,cleaning,cleaned,license,lisense,copyright,author,authorship,rename,
    renaming,renamed,token,merge,merging,merged,implementation,initialize,initializing,initialized,importing,imported,add,adding,added,feature,
    external,language, requirements]


categories = ["corrective","fixed","fixing","fix","debug","debugging","debugged","bug", "debug", "fix", "broken", "work", "edit","problem", "error", "typo", "exception",
    "try", "catch",'adaptive','platform','hardware','test','testing','change','changing','tested','changed','platform','build','test','doc','documentation','international',
    'config','data','readme','info','comment','description','src','note', 'perfective','reformat','reformatted','moved','moving','move','rename','renaming','renamed',
    'refactor','refactored','refactoring','delete','deleted','deleting','remove','removed','removing','clean','whitespace','indent','spacing','refactor','move','replace',
    'remove','order','redundant','tidy','rework','patch','move',"nonfunctional","clean","cleaning","cleaned","license","lisense","copyright", "author","authorship","rename", 
    "renaming","renamed", "token", "merge","merging", "merged","implementation","initialize","initializing","initialized","importing","imported","add","adding","added","feature",
    "external","language","requirements"]



total = 0
temp = 0
count = 0
outFile = open("TermCount.txt", 'w')

with open("Commit_categorizations.txt") as f:
    for line in f:
        for category in categories:
            if category in line:
                temp = categories.index(category)
                terms[temp] +=1
                total += 1
                break


outFile.write('\n')
for term in terms:
    outFile.write("%s: " % categories[count])
    count += 1
    if(total != 0):
        temp = int(term)
        outFile.write('{:<10}'.format(str(round((temp/total)*100,1))))
        outFile.write('\n')
    else:
        outFile.write('\n')


