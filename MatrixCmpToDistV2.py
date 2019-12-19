for y in range(height):
    for x in range(width):
        if (not label[y, x] == output[y, x]):  # start lfr same class
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
                print("\n-------------------------------------------")
                print("left=",left)
                print("right=",right)
                print("top=",top)
                print("bottom=",bottom)
                print("ry=",ry)
                print("rx=",rx)
                print("-------------------------------------------\n")
                #-------------print----------------


                #                 if()
                for xt in range(left, (right+1)):
                    if (label[top, xt] == output[y, x]):
                        dist_tmp = (((top - y) ** 2) + ((xt - x) ** 2)) ** 0.5
                        if (dist_tmp <= distancem[y, x]):
                            distancem[y, x] = dist_tmp
                            found=True
#                             break
                    if (label[bottom, xt] == output[y, x]):
                        dist_tmp = (((bottom - y) ** 2) + ((xt - x) ** 2)) ** 0.5
                        if (dist_tmp <= distancem[y, x]):
                            distancem[y, x] = dist_tmp
                            found=True
#                             break
                for yt in range(top, (bottom+1)):  # a walk through height and take a look at left and right columns
                    if (label[yt, left] == output[y, x]):
                        dist_tmp=(((yt - y) ** 2) + ((left - x) ** 2)) ** 0.5
                        if(dist_tmp<=distancem[y, x]):
                            distancem[y,x]=dist_tmp
#                             distancem[y, x] = (((yt - y) ** 2) + ((left - x) ** 2)) ** 0.5
                            found=True
#                         break
                    if (label[yt, right] == output[y, x]):
                        dist_tmp=(((yt - y) ** 2) + ((right - x) ** 2)) ** 0.5
                        if(dist_tmp<=distancem[y,x]):
                            distancem[y, x]=dist_tmp
#                         distancem[y, x] = (((yt - y) ** 2) + ((right - x) ** 2)) ** 0.5
                            found=True
#                         break

        else:
            distancem[y,x]=0
