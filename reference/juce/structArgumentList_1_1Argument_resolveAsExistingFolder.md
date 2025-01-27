#### resolveAsExistingFolder()


 File ArgumentList::Argument::resolveAsExistingFolder ( ) const 
 

Resolves a usersupplied folder name into an absolute File, using the current working directory as a base for resolving relative paths, and also doing a check to make sure the folder exists.If the folder doesn't exist, this will call fail() with a suitable error.See alsoresolveAsFile, resolveAsExistingFile