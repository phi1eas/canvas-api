import * as async from 'async';
const exec = require('child_process').exec;

async.series([
 exec('yarn docs:dev')
]); 