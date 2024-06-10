function solution(park, routes) {
        const dirs = {E: [0, 1], W: [0, -1], S: [1, 0], N: [-1, 0]};
        let [y, x] = [0, 0];
    
        for (let i = 0; i < park.length; i++) {
          if (park[i].includes("S")) {
            [y, x] = [i, park[i].indexOf("S")];
            break;
          }
        }

        routes.forEach((route) => {
          const [d, n] = route.split(" ");
          let [ny, nx] = [y, x];
          let i = 0;
          while (i < n) {
            [ny, nx] = [ny + dirs[d][0], nx + dirs[d][1]];
            if (!park[ny] || !park[ny][nx] || park[ny][nx] === "X") break;
            i++;
          }
          if (i == n) [y, x] = [ny, nx];
        });
    
        return [y, x];
      }
