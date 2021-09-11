#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CHS/LBA capacity calculator 
# CHS/LBA converter

#  ATA-5 limit corresponds to CHS 16383 16 63 (16514064 = 16383×16×63 = 1032×254×63)
# CHS addressing starts at 0/0/1 with a maximal value 1023/255/63 for 24=10+8+6 bits, 
# or 1023/254/63 for 24 bits limited to 255 heads.
#  ATA-5 CHS 24 bits = 14(C)+4(H)+6(S) bits -> 10+8+6 bits
# CHS addressing with 28 bits (EIDE and ATA-2) permits 
# eight bits for sectors still starting at 1, i.e., sectors 1...255, 
# four bits for heads 0...15, and sixteen bits for cylinders 0...65535

# To help visualize the sequencing of sectors into a linear LBA model, note that:
# 
# The first LBA sector is sector # zero, the same sector in a CHS model is called sector # one.
# All the sectors of each head/track get counted before incrementing to the next head/track.
# All the heads/tracks of the same cylinder get counted before incrementing to the next cylinder.
# The outside half of a whole Hard Drive would be the first half of the drive.

# Refs: 
# 1. https://en.wikipedia.org/wiki/Cylinder-head-sector
# 2. https://www.deathwombat.com/diskgeometry.html
# 3. http://www.csgnetwork.com/mediasizecalc.html
# 4. https://en.wikipedia.org/wiki/Logical_block_addressing#CHS_conversion

# Note: #header=#tracks, it is unneccesary to be an even number
def iCHSCapacity(C,H,S,B=512):
    C = int(input('Enter the total number of cylinders:'))
    H = int(input('Enter the total number of heads(#heads per cylinder):'))
    S = int(input('Enter the number of sectors per track:'))
    B = int(input('Enter the number of bytes per sector:'))

    capacity = C*H*S*B
    print("Disk capacity: ", capacity)
    return capacity

def iLBACapacity(L,B=512):
    L = int(input('Enter the maximum logical block address:'))
    B = int(input('Enter the number of bytes per sector:'))

    capacity = (L+1)*B
    print("Disk capacity: ", capacity)
    return capacity

# Note: sector # starts from 1, but head# or track# and cylinder# starts from 0
def ichs2lba(c,h,s,C,H,S): 
    C = int(input('Enter the total number of cylinders:'))
    H = int(input('Enter the total number of heads(#heads per cylinder):'))
    S = int(input('Enter the number of sectors per track:'))
    c,h,s = [int(x) for x in input('Enter the c,h,s coordinates, separate by blanks:\n').split()]
    
    l = c*H*S + h*S + (s-1)
    print("lba: ", l)

    return l

# Note: sector # start from 1, but head# or track# and cylinder# starts from 0
def ilba2chs(l,H,S):
    H = int(input('Enter the total number of heads(#heads per cylinder):'))
    S = int(input('Enter the number of sectors per track:'))
    l = int(input('Enter the logical block address:'))
    c,r = l // (H*S), l%(H*S)
    h,r = r // S, r%S
    s = r+1
    print("(c,h,s): ","(",c,h,s,")")
    return (c,h,s)

# Note: #header=#tracks, it is unneccesary to be an even number
def CHSCapacity(C,H,S,B=512):
    # C = int(input('Enter the total number of cylinders:'))
    # H = int(input('Enter the total number of heads(#heads per cylinder):'))
    # S = int(input('Enter the number of sectors per track:'))
    # B = int(input('Enter the number of bytes per sector:'))

    capacity = C*H*S*B
    # print("Disk capacity: ", capacity)
    return capacity

def LBACapacity(L,B=512):
    # L = int(input('Enter the maximum logical block address:'))
    # B = int(input('Enter the number of bytes per sector:'))

    capacity = (L+1)*B
    # print("Disk capacity: ", capacity)
    return capacity

# Note: sector # starts from 1, but head# or track# and cylinder# starts from 0
def chs2lba(c,h,s,C,H,S): 
    # C = int(input('Enter the total number of cylinders:'))
    # H = int(input('Enter the total number of heads(#heads per cylinder):'))
    # S = int(input('Enter the number of sectors per track:'))
    # c,h,s = [int(x) for x in input('Enter the c,h,s coordinates, separate by blanks:\n').split()]
    
    l = c*H*S + h*S + (s-1)
    # print("lba: ", l)

    return l

# Note: sector # start from 1, but head# or track# and cylinder# starts from 0
def lba2chs(l,H,S):
    # H = int(input('Enter the total number of heads(#heads per cylinder):'))
    # S = int(input('Enter the number of sectors per track:'))
    # l = int(input('Enter the logical block address:'))
    c,r = l // (H*S), l%(H*S)
    h,r = r // S, r%S
    s = r+1
    # print("(c,h,s): ","(",c,h,s,")")
    return (c,h,s)

if __name__ == '__main__':
	# test code   

    # C,H,S
    print("\nDisk capacity in CHS:")
    C = int(input('Enter the total number of cylinders:'))
    H = int(input('Enter the total number of heads(#heads per cylinder):'))
    S = int(input('Enter the number of sectors per track:'))
    B = int(input('Enter the number of bytes per sector:'))        
    capacity = CHSCapacity(C,H,S,B)
    print("Disk capacity with (C,H,S,B)=({},{},{},{}): {} bytes".format(C,H,S,B,capacity))

    # LBA
    print("\nDisk capacity in LBA:")
    L = int(input('Enter the maximum logical block address:'))
    B = int(input('Enter the number of bytes per sector:'))    
    capacity = LBACapacity(L,B)
    print("Disk capacity wit (L,B)=({},{}): {} bytes".format(L,B,capacity))

    # chs to lba
    print("\nchs to lba:")
    C = int(input('Enter the total number of cylinders:'))
    H = int(input('Enter the total number of heads(#heads per cylinder):'))
    S = int(input('Enter the number of sectors per track:'))
    (c,h,s) = [int(x) for x in input('Enter the c,h,s coordinates, separate by blanks:\n').split()] 
    lba = chs2lba(c,h,s,C,H,S)
    print("chs to lba: ({},{},{}) -> {}".format(c,h,s,lba))

    # lba to chs
    print("\nlba to chs:")
    H = int(input('Enter the total number of heads(#heads per cylinder):'))
    S = int(input('Enter the number of sectors per track:'))
    l = int(input('Enter the logical block address:'))
    c,h,s = lba2chs(l,H,S)
    print("lba to chs {} -> ({},{},{})".format(l,c,h,s))