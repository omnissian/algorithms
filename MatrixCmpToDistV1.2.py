import shutil
import numpy as np

height=10 # y
width=10 # x
label=np.zeros((height,width),dtype=int)
for y in range(height):
    for x in range(width):
        if(8>y>2 and 8>x>2):
            label[y,x]=1
label[0,0]=1
label[9,0]=1
label[9,1]=1
output=np.copy(label)
output[5,5]=0
output[5,6]=0
output[0,9]=1
output[0,0]=0
output[9,6]=1
diagonal=np.round((((height)**2) + ((width)**2))** 0.5)
# distancem=np.zeros((height,width),dtype=int) # we cant fill it with zeros because OF THINK YOUR STEP FAGGOT
distancem=np.full((height,width), diagonal)

# bad situation still = n^4, average situation ~ n^3
for y in range(height):
    for x in range(width):
        if (not label[y, x] == output[y, x]):  # start lfr same class
            print("---------looking for-------------")
            print("label[",y,",",x,"]=", label[y, x])
            print("output[",y,",",x,"]=", output[y, x])
            found=False
            biggest = (height > width) and height or width
            for radius in range(1,biggest):
                if(found):
                    break
                ry = rx = radius
                left = ((x - rx) >= 0) and (x - rx) or 0
                right = ((x + rx) < width) and (x + rx) or (width-1)
                # top -  "top" only is top for human and "actually is zero" for omnissiah
                top = ((y - ry) >= 0) and y - ry or 0
                bottom = ((y + ry) < height) and y + ry or (height-1)

                #-------------print----------------
                # print("\n-------------------------------------------")
                # print("left=",left)
                # print("right=",right)
                # print("top=",top)
                # print("bottom=",bottom)
                # print("ry=",ry)
                # print("rx=",rx)
                # print("-------------------------------------------\n")
                #-------------print----------------

                print("-----radius=", radius)
                #                 if()
                for yt in range(top, (bottom+1)):  # a walk through height and take a look at left and right columns
                    if (label[yt, left] == output[y, x]):
                        dist_tmp = (((yt - y) ** 2) + ((left - x) ** 2)) ** 0.5
                        if (dist_tmp <= distancem[y, x]):
                            distancem[y, x] = dist_tmp
                            print("(yt-y)**2= (", yt,"-", y,")**2=",(yt-y),"**2=", (yt-y)**2)
                            print("(left-x)**2= (", left,"-", x,")**2=",(left-x),"**2=", (left-x)**2)
                            print("(arg1+arg2)**0.5= (", (yt-y)**2,"+", (left-x)**2,")**0.5=",((yt-y)**2+(left-x)**2)**0.5)
                            print("founded dist=",dist_tmp)
                            print("label[", yt, ",", left, "]=", label[y, x])
                            print("output[", y, ",", x, "]=", output[y, x])
                            found=True
                            break
                    if (label[yt, right] == output[y, x]):
                        dist_tmp = (((yt - y) ** 2) + ((right - x) ** 2)) ** 0.5
                        if (dist_tmp <= distancem[y, x]):
                            distancem[y, x] = dist_tmp
                            print("(yt-y)**2= (", yt, "-", y, ")**2=", (yt - y), "**2=", (yt - y) ** 2)
                            print("(right-x)**2= (", right, "-", x, ")**2=", (right - x), "**2=", (right - x) ** 2)
                            print("(arg1+arg2)**0.5= (", (yt - y) ** 2, "+", (right - x) ** 2, ")**0.5=", ((yt - y) ** 2 + (right - x) ** 2) ** 0.5)
                            print("founded dist=",dist_tmp)
                            print("label[", yt, ",", right, "]=", label[y, x])
                            print("output[", y, ",", x, "]=", output[y, x])
                            found=True
                            break
                for xt in range(left, (right+1)):
                    if (label[top, xt] == output[y, x]):
                        dist_tmp = (((top - y) ** 2) + ((xt - x) ** 2)) ** 0.5
                        if (dist_tmp <= distancem[y, x]):
                            distancem[y, x] = dist_tmp
                            print("(top-y)**2= (", top, "-", y, ")**2=", (top - y), "**2=", (top - y) ** 2)
                            print("(xt-x)**2= (", xt, "-", x, ")**2=", (xt - x), "**2=", (xt - x) ** 2)
                            print("(arg1+arg2)**0.5= (", (top - y) ** 2, "+", (xt - x) ** 2, ")**0.5=", ((top - y) ** 2 + (xt - x) ** 2) ** 0.5)
                            print("founded dist=",dist_tmp)
                            print("label[", top, ",", xt, "]=", label[y, x])
                            print("output[", y, ",", x, "]=", output[y, x])
                            found=True
                            break
                    if (label[bottom, xt] == output[y, x]):
                        dist_tmp = (((bottom - y) ** 2) + ((xt - x) ** 2)) ** 0.5
                        if (dist_tmp <= distancem[y, x]):
                            distancem[y, x] = dist_tmp
                            print("founded dist=",dist_tmp)
                            print("(bottom-y)**2= (", bottom, "-", y, ")**2=", (bottom - y), "**2=", (bottom - y) ** 2)
                            print("(xt-x)**2= (", xt, "-", x, ")**2=", (xt - x), "**2=", (xt - x) ** 2)
                            print("(arg1+arg2)**0.5= (", (bottom - y) ** 2, "+", (xt - x) ** 2, ")**0.5=", ((bottom - y) ** 2 + (xt - x) ** 2) ** 0.5)
                            print("label[", bottom, ",", xt, "]=", label[y, x])
                            print("output[", y, ",", x, "]=", output[y, x])
                            found=True
                            break
        else:
            distancem[y,x]=0
distancem=np.round(distancem,2)
print(distancem)















