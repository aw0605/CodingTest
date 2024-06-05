function solution(survey, choices) {
    let result = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0,
    };
    
    const types = ["RT","CF","JM","AN"];

    for(let i = 0; i < survey.length; i++){
        result[choices[i]<4 ? survey[i][0] : survey[i][1]] += Math.abs(choices[i] - 4);
    }

    return types.map(([a, b]) => result[b] > result[a]? b : a).join("");
}