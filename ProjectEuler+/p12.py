li = {128: 157080, 1: 1, 2: 3, 4: 6, 6: 28, 648: 103672800, 9: 36, 144: 437580, 18: 300, 20: 528, 24: 630, 768: 236215980, 112: 73920, 162: 749700, 36: 2016, 1024: 842161320, 40: 3240, 1280: 3090906000L, 48: 5460, 192: 1493856, 320: 2162160, 90: 25200, 480: 17907120, 16: 120, 240: 2031120, 168: 1385280, 1344: 4819214400L, 576: 76576500}
keys = sorted(li.keys())
n = []
for i in xrange(input()):
    n.append(input())
for i in n:
    for j in keys:
        if j>i:
            print li[j]
            break