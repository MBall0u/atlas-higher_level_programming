#!/usr/bin/node
const count = process.argv.slice(2);
for (let i = 0; i < count; i++) {
  for (let j = 0; j < count; j++) {
    console.log('X');
  }
}
