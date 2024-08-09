import subprocess

from config import Config

con = open("configurations.txt", "r")

for i in con:
    word = i.rstrip('\n').split(" ")

    if len(word) == 1:
        Config(word[0])
    else:
        Config(word[0], True, word[1: len(word) - 1])

configs = Config.configs

for i in configs:
    print(i)
input(configs)

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
    cmd += " \ " + i.getSymbol()

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
