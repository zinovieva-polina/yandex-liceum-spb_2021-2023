import sys

from pygame import *
fps=60
w=600
h=600
clock=time.Clock()
sc=display.set_mode((w,h))#окошко
draw.rect(sc,(255,255,255),(20,22,100,150),)
draw.rect(sc,(255,255,255),(101,151,201,251),20)
draw.line(sc,(255,0,0),[2,90],[60,90],5)
draw.aaline(sc,(255,0,0),[91,60],[141,60],5)
draw.lines(sc,(255,0,0),False,[[2,150],[60,120],[5,200]],5)
display.update()
while True:
    for i in event.get():
        if i.type==QUIT:
            quit()
            sys.exit()
        clock.tick(fps)