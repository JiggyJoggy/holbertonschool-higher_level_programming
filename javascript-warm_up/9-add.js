#!/usr/bin/node
function add(a, b) {
    a = parseInt(process.argv[2]);
    b = parseInt(process.argv[3]);

    if (Number(a) && Number(b)) {
        console.log(`${(a + b)}`)
    }
}
