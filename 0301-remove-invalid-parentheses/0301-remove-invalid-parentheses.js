var removeInvalidParentheses = function (s) {
    function valid(s) {
        let stack = [];
        for (let c of s) {
            if (c === '(') stack.push(c);
            else if (c === ')') {
                if (stack.length && stack.at(-1) === '(') {
                    stack.pop();
                } else return false;
            }
        }
        return stack.length === 0;
    }
    let q = [s], vis = new Set([s]), res = [];
    let found = false;
    while (q.length) {
        let top = q.shift();
        if (valid(top)) {
            res.push(top);
            found = true;
        }
        if (found) continue;
        for (let i = 0; i < top.length; i++) {
            if (!'()'.includes(top[i])) continue;
            let str = top.slice(0, i) + top.slice(i + 1);
            if (!vis.has(str)) {
                q.push(str);
                vis.add(str);
            }
        }
    }
    if (res.length === 0) return [''];
    return res;
};