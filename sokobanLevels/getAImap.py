import os

from element import border
def getmapbyAI():
    string = ""
    linecount = 0
    with open('sokobanLevels/'+'randomlevel.txt',"r") as f:
        for lines in f.readlines():
            if(linecount == 0):
                string += " HHHHHHHH\n"
            elif(linecount == 7):
                string += "HHHHHHHH\n"
            else:    
                rep = 'H' + lines[1:7] + 'H\n'
                string += rep
            linecount += 1
    return string
