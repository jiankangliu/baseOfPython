def main():

def createListFromFile(fileName):
    infile=open(fileName,'r')
    desireList=[line.rstrip() for line in infile]
    infile.close()
    return desireList

def