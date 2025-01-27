#### getNonexistentSibling()


 File File::getNonexistentSibling ( bool putNumbersInBrackets = true ) const 
 

Chooses a filename for a sibling file to this one that doesn't already exist.If this file doesn't exist, this will just return itself, otherwise it will return an appropriate sibling that doesn't exist, e.g. if a file "/moose/fish/foo.txt" exists, this might return "/moose/fish/foo(2).txt".Parameters

 putNumbersInBrackets whether to add brackets around the numbers that get appended to the new filename.