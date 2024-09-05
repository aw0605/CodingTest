def solution(m, n, startX, startY, balls):
    ans = []
    slist = [[startX,startY+2*(n-startY)],[startX,-startY],[-startX,startY],[startX+2*(m-startX),startY]]
    for a,b in balls :
        dist = []
        for i in range(4) :
            if (startY==b and startX>a and i==2) or (startY==b and startX<a and i==3) or (startX==a and startY>b and i==1) or (startX==a and startY<b and i==0) : continue
            x,y = slist[i]
            dist.append((x-a)**2+(y-b)**2)
        ans.append(min(dist))
    return ans