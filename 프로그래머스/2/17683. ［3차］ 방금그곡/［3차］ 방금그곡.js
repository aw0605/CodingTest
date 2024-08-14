function change(s) {
    return s.replace(/C#/g, 'c')
            .replace(/D#/g, 'd')
            .replace(/F#/g, 'f')
            .replace(/G#/g, 'g')
            .replace(/A#/g, 'a')
            .replace(/B#/g, 'b');
}

function solution(m, musicinfos) {
    let answer = [0, '(None)'];
    m = change(m);
    
    for (const info of musicinfos) {
        const [t1, t2, title, notes] = info.split(',');
        
        const startHour = parseInt(t1.slice(0, 2), 10);
        const startMinute = parseInt(t1.slice(3), 10);
        const endHour = parseInt(t2.slice(0, 2), 10);
        const endMinute = parseInt(t2.slice(3), 10);
        const time = (endHour - startHour) * 60 + (endMinute - startMinute);
        
        const partNotes = change(notes);
        const fullNotes = partNotes.repeat(Math.floor(time / partNotes.length)) + partNotes.slice(0, time % partNotes.length);
        
        if (fullNotes.includes(m) && time > answer[0]) answer = [time, title];
    }
    
    return answer[1];
}