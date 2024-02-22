#!/usr/bin/node

const { chownSync } = require('fs');

// a script that reads and prints the content of a file.

const fs = require('fs').promises;

async function readFile (filepath, encoding) {
  try {
    const data = await fs.readFile(filepath, encoding);
    console.log(data);
  } catch (error) {
    // const errorObject = {
    //     'Error': error.message,
    //     'errno': error.errno,
    //     'code': error.code,
    //     'syscall': error.syscall,
    //     'path': error.path
    // }
    console.log(error);
    // console.error(errorObject);
  }
}
readFile(process.argv[2], 'utf8');
