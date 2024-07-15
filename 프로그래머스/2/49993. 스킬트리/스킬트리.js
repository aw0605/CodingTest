function solution(skill, skill_trees) {
    const regex = new RegExp(`[^${skill}]`, 'g');

    return skill_trees
        .map((v) => v.replace(regex, ''))
        .filter((s) => {return skill.startsWith(s);}).length
}