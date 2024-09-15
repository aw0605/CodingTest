function solution(genres, plays) {
    const dic = {};
    const dupDic = {};
    genres.forEach((g,i)=> dic[g] = dic[g] ?  dic[g] + plays[i] : plays[i]);

    return genres          
          .map((g,i)=> ({genre: g, count: plays[i], index: i}))
          .sort((a,b)=>{               
               if (a.genre !== b.genre) return dic[b.genre] - dic[a.genre];
               if (a.count !== b.count) return b.count - a.count;
               return a.index - b.index;
           })
           .filter(v => {
               if (dupDic[v.genre] >= 2) return false;
               dupDic[v.genre] = dupDic[v.genre] ? dupDic[v.genre] + 1 : 1;
               return true;
            })
           .map(v => v.index);    
}