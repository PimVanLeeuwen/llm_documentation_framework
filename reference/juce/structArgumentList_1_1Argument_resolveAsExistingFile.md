#### resolveAsExistingFile()


 File ArgumentList::Argument::resolveAsExistingFile ( ) const 
 

Resolves this argument as an absolute File, using the current working directory as a base for resolving relative paths, and also doing a check to make sure the file exists.If the file doesn't exist, this will call fail() with a suitable error.See alsoresolveAsFile, resolveAsExistingFolder