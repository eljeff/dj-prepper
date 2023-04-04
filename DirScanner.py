import glob

class DirScanner:

    def scan(self, path, matchPattern):
        path_to_scan = str(path)
        msg = "Scanning " + path_to_scan + "..."
        print(msg)
        files = glob.glob(path + "/" + matchPattern)       
        return files

    def scanFromInput(self):
        path_to_scan = str(input("enter path to scan: "))
        match_pattern = str(input("enter pattern to match via glob: "))
        self.scan(path_to_scan, match_pattern)