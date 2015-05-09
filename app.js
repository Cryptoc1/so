#! /usr/bin/env node

var snag = require('./snag');
var title = process.argv.slice(2);

snag.get(title)
