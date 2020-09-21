import math
def hammingdistance(hex1,hex2):
    bot = "{0:08b}".format(int(hex1, 16))
    bit = "{0:08b}".format(int(hex2, 16))
    while len(bot) > len(bit):
        bit = "0" + bit
    while len(bot) < len(bit):
        bot = "0" + bit
    hdist = 0
    for e in range(0, len(bot)):
        if (bot[e] != bit[e]):
            hdist += 1
    return hdist