import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3
from minecraftstuff import MinecraftDrawing
from minecraftstuff import MinecraftShape, ShapeBlock
from random import randint
from time import sleep
LENGTH=20
snow=80

mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)
def prepare():
    for x in range(LENGTH):
        for z in range(LENGTH):
             mc.setBlock(x, 0, z, block.DIRT)
def gg():
    mc.setBlocks(19, 1, 0, 19, 6, 18, block.TNT)
def gh():
    mc.setBlocks(0, 1, 0, 19, 6, 0, block.TNT)
def gj():
    mc.setBlocks(0, 1, 0, 0, 6, 19, block.TNT)
def gk():
    mc.setBlocks(0, 1, 19, 18, 6, 19, block.TNT)
def hh():
    rx= randint(0,LENGTH-1)
    rz= randint(0,LENGTH-1)
    mc.setBlocks(rx, 0, rz, rx+4, 4, rz, block.SNOW_BLOCK)
def dd():
    rx= randint(0,LENGTH-1)
    rz= randint(0,LENGTH-1)
    mc.setBlocks(rx, 0, rz, rx, 4, rz+4, block.SNOW_BLOCK)
def zz():
    rx= randint(0,LENGTH-1)
    rz= randint(0,LENGTH-1)
    ry= randint(1,6)
    mc.setBlock(rx, ry, rz, block.GOLD_BLOCK)
def win():
        ev= mc.events.pollBlockHits()
        if ev:
            hit = ev[0]
            print(hit.pos)
            bl = mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
            print(bl)
            if bl == 41 :
                mc.postToChat("you win")
    
    
    
def main():
    prepare()
    gg()
    gh()
    gj()
    gk()
    for i in range(20):
        hh()
    for i in range(20):
        dd()
    zz()
    while True:
        win()
        
    
    
main()


