# Image Projection onto Sphere
# https://en.wikipedia.org/wiki/Equirectangular_projection
# Download the test image from the Wikipedia page!
# FB36 - 20160731

import math, random
from PIL import Image

def image_on_sphere(imageInput: Image, xy: float, xz: float, yz: float,
                    imgxOutput: int, imgyOutput: int) -> Image:    
    
    pi2 = math.pi * 2
    # 3D Sphere Rotation Angles (arbitrary)
    sxy = math.sin(xy); cxy = math.cos(xy)
    sxz = math.sin(xz); cxz = math.cos(xz)
    syz = math.sin(yz); cyz = math.cos(yz)
    (imgxInput, imgyInput) = imageInput.size
    pixelsInput = imageInput.load()
    imageOutput = Image.new("RGBA", (imgxOutput, imgyOutput), (0, 0, 0, 0))
    pixelsOutput = imageOutput.load()
    # define a sphere behind the screen
    xc = (imgxOutput - 1.0) / 2
    yc = (imgyOutput - 1.0) / 2
    zc = min((imgxOutput - 1.0), (imgyOutput - 1.0)) / 2
    r = min((imgxOutput - 1.0), (imgyOutput - 1.0)) / 2
    # define eye point
    xo = (imgxOutput - 1.0) / 2
    yo = (imgyOutput - 1.0) / 2
    zo = -min((imgxOutput - 1.0), (imgyOutput - 1.0))
    xoc = xo - xc
    yoc = yo - yc
    zoc = zo - zc
    doc2 = xoc * xoc + yoc * yoc + zoc * zoc
    for yi in range(imgyOutput):
        for xi in range(imgxOutput):
            xio = xi - xo
            yio = yi - yo
            zio = 0.0 - zo
            dio = math.sqrt(xio * xio + yio * yio + zio * zio)
            xl = xio / dio
            yl = yio / dio
            zl = zio / dio
            dot = xl * xoc + yl * yoc + zl * zoc
            val = dot * dot - doc2 + r * r
            if val >= 0: # if there is line-sphere intersection
                if val == 0: # 1 intersection point
                    d = -dot
                else: # 2 intersection points => choose the closest
                    d = min(-dot + math.sqrt(val), -dot - math.sqrt(val))
                    xd = xo + xl * d
                    yd = yo + yl * d
                    zd = zo + zl * d
                    x = (xd - xc) / r
                    y = (yd - yc) / r
                    z = (zd - zc) / r
                    x0=x*cxy-y*sxy;y=x*sxy+y*cxy;x=x0 # xy-plane rotation
                    x0=x*cxz-z*sxz;z=x*sxz+z*cxz;x=x0 # xz-plane rotation 
                    y0=y*cyz-z*syz;z=y*syz+z*cyz;y=y0 # yz-plane rotation
                    lng = (math.atan2(y, x) + pi2) % pi2
                    lat = math.acos(z)
                    ix = int((imgxInput - 1) * lng / pi2 + 0.5)
                    iy = int((imgyInput - 1) * lat / math.pi + 0.5)
                    try:
                        pixelsOutput[xi, yi] = pixelsInput[ix, iy]
                    except:
                        pass
    return imageOutput