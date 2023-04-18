/* Given a number, we need to find sum of its digits using recursion.
 Examples: 
 Input : 12345
 Output : 15
 Input : 45632
 Output :20 */

function sumOfDigitI(n) {
    const nString = n.toString()
    let total = 0;
    for (let i = 0; i < nString.length; i++) {
        total += parseInt(nString[i]);
    }
    return total;
}
function sumOfDigit(n) {
    if (n === 0) {
        return 0;
    }
    return (n % 10) + sumOfDigit(parseInt(n / 10));
}

console.log(sumOfDigitI(123456789123456789123));