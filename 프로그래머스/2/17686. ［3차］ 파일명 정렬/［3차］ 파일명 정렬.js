function solution(files) {
    const re = /^([a-zA-Z-\. ]+)([0-9]+)(.*)$/
    let dict = []
    files.forEach((v, i) => {
        let [file, head, num] = v.match(re)
        dict.push({file, head: head.toLowerCase(), num: parseInt(num), i})
    })

    return dict.sort((a, b) => {
        if (a.head > b.head) return  1
        if (a.head < b.head) return -1
        if (a.num > b.num) return  1
        if (a.num < b.num) return -1
        return a.i - b.i
    }).map(v => v.file)
}