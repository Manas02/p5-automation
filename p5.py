#!usr/bin/python

import os
import argparse

def stuff(option="p5"):
    os.mkdir("./Project")
    if option == "p5":
        with open("./Project/index.html","w") as f:
            html_p5= ("<!DOCTYPE html>\n  <head>\n\t<meta charset=\"utf-8\">\n\t<title>P5.js</title>\n\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.min.js\"></script>\n\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/addons/p5.dom.min.js\"></script>\n\t<script src=\"sketch.js\"></script>\n  </head>\n</html>")
            f.write(html_p5)
    elif option == "ml5":   
        with open("./Project/index.html","w") as f:
            html_ml5= ("<!DOCTYPE html>\n  <head>\n\t<meta charset=\"utf-8\">\n\t<title>ml5.js</title>\n\t<script src=\"https://unpkg.com/ml5@0.4.3/dist/ml5.min.js\"></script>\n\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.min.js\"></script>\n\t<script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/addons/p5.dom.min.js\"></script>\n\t<script src=\"sketch.js\"></script>\n  </head>\n</html>")
            f.write(html_ml5)
    with open("./Project/sketch.js","w") as i:
        i.write("function setup(){\n\tcreateCanvas(windowWidth,windowHeight)\n\tbackground(0)\n}\n\nfunction draw(){\n\n}")
    else:
        print('Use \npython p5.py <-t>/<--type> <p5>OR<ml5>\npython p5.py -h [for help]')

def run(args):
    stuff(args.input)

def main():
    parser = argparse.ArgumentParser(description="ℹ️ This will create a p5  p5 + ml5 project with index.html & sketch.js")
    parser.add_argument("-t","--type",help="🎯 creates p5/ml5 porject dir",dest='input',type=str,default="p5")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
