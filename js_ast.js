if (process.argv.length < 3) {
  console.log("Usage: node js_ast.js path_to_obfuscated_file");
  return;
}

var filesystem = require('fs');
var path = require('path');
var filePath = path.join(__dirname, process.argv[2]);
filesystem.readFile(filePath, 'utf8', function(error,data){
    if (!error){
      console.log('Original Obfuscated Code: ' + data);
      var esprima = require('esprima');
      console.log(JSON.stringify(esprima.parse(data), null, 4));
    } else{
        console.log(error);
    }
});
