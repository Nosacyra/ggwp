import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3
from minecraftstuff import MinecraftDrawing
from minecraftstuff import MinecraftShape, ShapeBlock
from random import randint
from time import sleep

mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

def main():
    mc.setBlocks(1, 1, 1, 30, 1, 20, block.WOOD)
    mc.setBlocks(1, 1, 0, 30, 20, 0, block.WOOD)   






main()


