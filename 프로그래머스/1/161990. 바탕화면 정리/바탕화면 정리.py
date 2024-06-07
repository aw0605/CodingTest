def solution(wallpaper):
    yArr = []
    xArr = []
    
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == "#":
                yArr.append(y)
                xArr.append(x)
                
    return [min(yArr),min(xArr),max(yArr)+1,max(xArr)+1]