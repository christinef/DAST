DAST is a AST creator designed for obfuscation.

3RD-PARTY TOOL REQUIREMENTS
-----------------------------

DAST uses Python 3.4 and bash. Additionally: 

OBFUSCATION
closure-compiler (add as a folder in the project root directory)

TOKENIZATION
pygments (pip install pygments)

SYNTAX TREE
node.js
esprima (npm install esprima)



USAGE
-----

Downloading from git (based on the included GitHub repo listing), deleting all but the javascript files, and running the obfuscator on those files are independent bash scripts and can be run as desired (dast_dldgit.sh, dast_elimjs.sh, and dash_obfus.sh, respectively). Because GitHub has a 100 MB limit, to attempt the download place the obtained query_result.csv in the 'cloning' directory prior to running the shell script. 

For tokenization,
python js_parser.py path_to_obfuscated_file
 >> prints out the token list to the console

For ASTs,
node js_ast.js path_to_obfuscated_file
 >> prints the JSON (via Esprima) AST to the console

Samples of the Tokenization and Syntax Tree outputs are included (js_parser_sample.txt and js_ast_sample.txt, respectively).
