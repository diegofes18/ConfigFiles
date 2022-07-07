import json,sys,argparse

parser = argparse.ArgumentParser(description = "Python Script to change the "+
         "qtile theme from the json file")
parser.add_argument ("-t","--theme", help="dark-grey, dracula, material-darker"+
        ", material-ocean, monokai-pro, nord-wave, nord, onedark, rosepine")
args = parser.parse_args()

def main(argv):
    path = "/home/diegofes/.config/qtile/"
    theme = args.theme

    with open(path+"config.json","r") as jsonFile:
        data = json.load(jsonFile)

    data["theme"] = theme  

    with open(path+"config.json","w") as jsonFile:
        json.dump(data, jsonFile)

    print("theme changed to: " + theme)

if __name__ == "__main__":
    main(sys.argv)
