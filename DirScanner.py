from os import listdir
from os.path import isfile, join

class DirScanner:

    def scan(self, path):
        path_to_scan = str(path)
        msg = "Scanning " + path_to_scan + "..."
        print(msg)
        onlyfiles = [f for f in listdir(path_to_scan) if isfile(join(path_to_scan, f))]
        for file in onlyfiles:
            print(file)

    def scanFromInput(self):
        path_to_scan = str(input("enter path to scan: "))
        self.scan(path_to_scan)