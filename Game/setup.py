import os

#Remove from grading folder
def removeGrading():
    files = os.listdir("grading")
    for f in files:
        os.remove(os.path.join("grading", f))