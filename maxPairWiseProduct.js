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
    var largest = 0;
    var secondLargest = 0;

    for (var i = 0; i < integers.length; i++) {
        if (integers[i] >= largest) {
            secondLargest = largest;
            largest = integers[i];
        } else if (integers[i] >= secondLargest) {
            secondLargest = integers[i] 
        }
    }

    console.log(largest * secondLargest);
}
