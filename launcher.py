import requests
import svn.remote
import os.path

versionUrl = "https://raw.githubusercontent.com/NihilisticRealist/VersionControlTest/master/version.txt"
repoUrl = "https://github.com/NihilisticRealist/VersionControlTest.git"

cloudVer = requests.get(versionUrl)

cloudVer = cloudVer.text

clientVer = open("version.txt", "r")
clientVer = clientVer.read()
print("Client version number: " + clientVer)
print("Cloud version number: " + cloudVer)

if cloudVer > clientVer:
    print ("Update required! Updating...")
    updateRepo = svn.remote.RemoteClient(repoUrl)
    updateRepo.checkout(os.path.dirname(os.path.realpath(__file__)))
    del(updateRepo)
    print("All done!")

elif cloudVer < clientVer:
    print("What in the name of the seven hells did you do to the version file?")

else:
    print("All is well.")
    
    
