function solution(wallpaper) {
    let yArr = []
    let xArr = []
    for (let y = 0; y < wallpaper.length; y++){
        for (let x = 0; x < wallpaper[0].length; x++){
            if (wallpaper[y][x] === "#"){
                yArr.push(y)
                xArr.push(x)
            }
        }
    }
    return [Math.min(...yArr), Math.min(...xArr), Math.max(...yArr)+1, Math.max(...xArr)+1];
}