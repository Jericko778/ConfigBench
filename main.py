import subprocess

from config import Config

aliasalgo = Config("-aa", True, ("NONE", "FLOWSENSITIVE", "PTSBASED", "LAZY"))
aliasflowins = Config("-af")
callbackanalyzer = Config("-ca", True, ("FAST",))
codeelimination = Config("-ce", True, ("NONE", "PROPAGATECONSTS", "REMOVECODE"))
cgalgo = Config("-cg", True, ("AUTO", "CHA", "VTA", "RTA", "SPARK", "GEOM"))
paths = Config("-cp")
callbacksourcemode = Config("-cs", True, ("NONE", "ALL", "SOURCELIST"))
direction = Config("-dir", True, ("FORWARDS", "BACKWARDS"))
dataflowsolver = Config("-ds", True, ("CONTEXTFLOWSENSITIVE","FLOWINSENSITIVE"))
analyzeframeworks = Config("-ff")
implicit = Config("-i", True, ("NONE", "ARRAYONLY", "ALL"))
layoutmode = Config("-l", True, ("NONE", "PWD","ALL"))
logsourcesandsinks = Config("-ls")
nocallbacks = Config("-nc")
noexceptions = Config("-ne")
noiccresultspurify = Config("-np")
nothischainreduction = Config("-nr")
nostatic = Config("-ns")
notypechecking = Config("-nt")
outputlinenumbers = Config("-ol")
originalnames = Config("-on")
onesourceatatime = Config("-os")
onecomponentatatime = Config("-ot")
pathalgo = Config("-pa", True, ("CONTEXTSENSITIVE","CONTEXTINSENSITIVE", "SOURCESONLY"))
pathreconstructionmode = Config("-pr", True, ("NONE", "FAST", "PRECISE"))
pathspecificresults = Config("-ps")
enablereflection = Config("-r")
singlejoinpointabstraction = Config("-sa")
staticmode = Config("-sf", True, ("CONTEXTFLOWSENSITIVE", "CONTEXTFLOWINSENSITIVE", "NONE"))
sequentialpathprocessing = Config("-sp")

configs = Config.configs

base = "java -jar /Users/Jericko/Flowdroid/soot-infoflow-cmd/target/soot-infoflow-cmd-jar-with-dependencies.jar \
        -a /Users/Jericko/Documents/Flowdroid/apks/Library2.apk \
        -p /Users/Jericko/Library/Android/sdk/platforms/ \
        -s /Users/Jericko/Flowdroid/soot-infoflow-android/SourcesAndSinks.txt"

cmd = base

f = open("trial.txt", "a+")
d = open("trialoutput.txt", "a+")
f.write("default ")
d.write("default ")

print("starting analysis")

output = subprocess.run(["time timeout 1h " + cmd], shell=True, capture_output=True, text=True)

arr = str(output).split(r"\n")
print(arr[-4].replace("real\\t", ""))
d.write(str(output)+ "\n")
f.write("default \n" + arr[-4].replace("real\\t", "") + "\n")
prior = []

for i in configs:
    name = "base"
    cmd = base

    name += " + " + i.getSymbol()
    cmd += r" \ " + i.getSymbol()

    if i.hasSubconfigs():
        for k in i.getSubconfigs():
            subname = name
            sub = cmd
            subname += " " + k
            sub += " " + k

            print("start " + subname)
            output = subprocess.run(["time timeout 1h " + sub], shell=True, capture_output=True, text=True)
            arr = str(output).split(r"\n")
            print(arr[-4].replace("real\\t", ""))
            d.write(str(output)+ "\n")
            f.write("default + " + subname + " \n" + arr[-4].replace("real\\t", "") + "\n")
        continue

    print(name)
    output = subprocess.run(["time timeout 1h " + cmd], shell=True, capture_output=True, text=True)
    arr = str(output).split(r"\n")
    print(arr[-4].replace("real\\t", ""))
    d.write(str(output)+ "\n")
    f.write("default + " + name + " \n" + arr[-4].replace("real\\t", "") + "\n")
