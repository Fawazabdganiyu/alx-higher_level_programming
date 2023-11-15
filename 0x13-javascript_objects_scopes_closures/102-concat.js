#!/usr/bin/node

const fs = require('fs');

const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];

const data1 = fs.readFileSync(src1, 'utf-8');
const data2 = fs.readFileSync(src2, 'utf-8');

const concat = data1 + data2;

fs.writeFileSync(dest, concat);
