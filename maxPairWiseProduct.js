const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

var lines = []

rl.on('line', (line) => {
  lines.push(line);
});

setTimeout( function() {
    var numIntegers = parseInt(lines[0]);
    var integersArray = lines[1].split(' ');
    var integers = []

    for (var i = 0; i < integersArray.length; i++) {
        integers.push(parseInt(integersArray[i]));
    }

    mainFn(numIntegers, integers);
    process.exit();
}, 100);


function mainFn(numIntegers, integers) {
    var largestCombo = 0;

    for (var i = 0; i < integers.length; i++) {
        for (var j = i + 1; j < integers.length; j++) {
            if (integers[i] * integers[j] > largestCombo) {
                largestCombo = integers[i] * integers[j];
            }
        }
    }

    console.log(largestCombo);
}