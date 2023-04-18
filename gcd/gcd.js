function gcd(a, b) {
    if ((a % b) === 0) {
        return b
    }
    return gcd(b, a%b);
}

console.log(gcd(100, 15))
console.log(gcd(46, 64))