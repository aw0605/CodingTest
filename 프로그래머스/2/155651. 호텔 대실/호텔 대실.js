function solution(book_time) {
    const bookings = book_time.map(([start, end]) => {
        const [sh, sm] = start.split(':').map(Number);
        const [eh, em] = end.split(':').map(Number);
        return [sh * 60 + sm,eh * 60 + em + 10];
    });
    bookings.sort((a, b) => a[0] - b[0]);

    const rooms = [];
    for (const [start, end] of bookings) {
        let roomFound = false;
        for (let i = 0; i < rooms.length; i++) {
            if (rooms[i] <= start) {
                rooms[i] = end;
                roomFound = true;
                break;
            }
        }
        if (!roomFound) rooms.push(end);
    }

    return rooms.length;
}