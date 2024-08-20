function solution(expression) {
    const splitted = expression.split(/([\*\+-])/g);

    const solve = (precedence, left = 0, right = splitted.length) => {
        if (left + 1 === right) return eval(splitted[left]);

        for (const operator of precedence) {
            for (let i = right - 2;i > left;i -= 2) {
                if (splitted[i] === operator) {
                    return eval(`${solve(precedence, left, i)}${operator}${solve(precedence, i + 1, right)}`);
                }
            }
        }

        return Number.POSITIVE_INIFINITY;
    };

    return Math.max(
        ...[
            ['*', '+', '-'],
            ['*', '-', '+'],
            ['+', '*', '-'],
            ['+', '-', '*'],
            ['-', '*', '+'],
            ['-', '+', '*']
        ]
        .map((precedence) => solve(precedence))
        .map(Math.abs)
    );
}