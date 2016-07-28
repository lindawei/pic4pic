#coding=utf-8
from PIL import Image
import os
       
def average_colour(image):

    colour_tuple = [None, None, None]
    for channel in range(3):

        # Get data for one channel at a time
        pixels = image.getdata(band=channel)

        values = []
        for pixel in pixels:
            values.append(pixel)

        colour_tuple[channel] = sum(values) / len(values)

    return tuple(colour_tuple)

def getColorPath(colorT, color):
    retPath = None
    delta = 255 * 3
    cr, cg, cb = color[:3]
    for p in colorT:
        if colorT[p] == None:
            continue
        r, g, b = colorT[p]
        dt = abs(cr - r) + abs(cg - g) + abs(cb - b)
        if dt < delta:
            delta = dt
            retPath = p
    return retPath

def main():
    pathFile = "pathes.txt"
    cellRoot = "img"
    CELL_W = 24
    CELL_H = CELL_W
    colorT = {}
    if os.path.exists(pathFile):
        colorT = eval(open(pathFile).read())
    else:
        for rt, dirs, files in os.walk(cellRoot):
            i = 0
            for f in files:
                fname = cellRoot + "/" + f
                img = Image.open(fname)
                color = average_colour(img)
                colorT[fname] = color
                i += 1
                print("\rcreate color table: %d%%\t" % (i * 100 / len(files)) ),  
        print("")
        open(pathFile, "w").write(str(colorT))
  
    
    imgBig = Image.open("big.jpg")
    
    w, h = imgBig.size
    imgHuge = Image.new( "RGB", (w * CELL_W, h * CELL_W))
    for i in xrange(0, w):
        for j in xrange(0, h):
            color = imgBig.getpixel((i, j))
            path = getColorPath(colorT, color)
            cellImage = Image.open(path).resize((CELL_W, CELL_H))
            imgHuge.paste(cellImage, (i * CELL_W, j * CELL_H))
            print("\rpaste img: %d%%\t\t" % ((i * h + j + 1) * 100 / w / h)),
    imgHuge.save("bigbig.jpg", "JPEG")
    
if __name__=="__main__":
    main()

