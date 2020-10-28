#!usr/bin/python

import os
import argparse

def stuff(option="p5"):
    if option == "p5":
        os.mkdir("./Project")
        os.mkdir("./Project/library")
        f = open("./Project/index.html","w")
        html_p5= ("<!DOCTYPE html>\n  <head>\n    <meta charset=\"utf-8\">\n    <title>P5.js</title>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.min.js\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/addons/p5.dom.min.js\"></script>\n    <script src=\"sketch.js\"></script>\n  </head>\n</html>")
        f.write(html_p5)
        f.close()
        i = open("./Project/sketch.js","w")
        i.write("function setup(){\n  createCanvas(windowWidth,windowHeight)\n  background(0)\n}\n\nfunction draw(){\n\n}")
        i.close()
    elif option == "ml5":
        os.mkdir("./Project")
        os.mkdir("./Project/library")
        f = open("./Project/index.html","w")
        html_ml5= ("<!DOCTYPE html>\n  <head>\n    <meta charset=\"utf-8\">\n    <title>ml5.js</title>\n    <script src=\"https://unpkg.com/ml5@0.4.3/dist/ml5.min.js\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/p5.min.js\"></script>\n    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.7.2/addons/p5.dom.min.js\"></script>\n    <script src=\"sketch.js\"></script>\n  </head>\n</html>")
        f.write(html_ml5)
        f.close()
        i = open("./Project/sketch.js","w")
        i.write("function setup(){\n  createCanvas(windowWidth,windowHeight)\n  background(0)\n}\n\nfunction draw(){\n\n}")
        i.close()
    else:
        print('Use \npython p5.py <-t>/<--type> <p5>OR<ml5>\npython p5.py -h [for help]')

def run(args):
    arg_input = args.input
    stuff(arg_input)

def main():
    parser = argparse.ArgumentParser(description="ℹ️  This will create a p5  p5 + ml5 project with index.html & sketch.js")
    parser.add_argument("-t","--type",help="🎯 creates p5/ml5 porject dir",dest='input',type=str,default="p5")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
