#### getNonexistentChildFile()


 File File::getNonexistentChildFile ( const String & prefix, 
 
 const String & suffix, 
 bool putNumbersInBrackets = true ) const 

Chooses a filename relative to this one that doesn't already exist.If this file is a directory, this will return a child file of this directory that doesn't exist, by adding numbers to a prefix and suffix until it finds one that isn't already there.If the prefix + the suffix doesn't exist, it won't bother adding a number.e.g. File ("/moose/fish").getNonexistentChildFile ("foo", ".txt", true) might return "/moose/fish/foo(2).txt" if there's already a file called "foo.txt".Parameters

 prefix the string to use for the filename before the number 
 
 suffix the string to add to the filename after the number 
 putNumbersInBrackets if true, this will create filenames in the format "prefix(number)suffix", if false, it will leave the brackets out.