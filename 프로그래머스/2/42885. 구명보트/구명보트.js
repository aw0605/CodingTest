function solution(people, limit) {
    people.sort((a,b) => a - b)
    let i;
    
    for (i = 0, j = people.length-1; i < j; j--) {
        if(people[i] + people[j] <= limit) i++;
    } 
    
    return people.length - i;
}