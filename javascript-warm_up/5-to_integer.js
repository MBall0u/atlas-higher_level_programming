#!/usr/bin/node
const arg = process.argv[2];

const num = parseInt(arg);
if (NaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
