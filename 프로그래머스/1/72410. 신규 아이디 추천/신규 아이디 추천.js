function solution(new_id) {
    reg1 = /[^0-9a-z-_.]/g
    reg2 = /\.{2,}/g
    reg3 = /^\.+|\.$/g
    
    new_id=new_id.toLowerCase().replace(reg1,"").replace(reg2, ".").replace(reg3, "")
    
    if (new_id === "") new_id = "a"
    if (new_id.length >= 16) new_id = new_id.slice(0,15).replace(/\.$/, "")
    if (new_id.length < 3) new_id += new_id[new_id.length-1].repeat(3-new_id.length)
    
    return new_id;
}