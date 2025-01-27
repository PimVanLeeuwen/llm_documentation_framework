#### withFileExtension()


 File File::withFileExtension ( StringRef newExtension ) const 
 

Returns a version of this file with a different file extension.e.g. File ("/moose/fish/foo.txt").withFileExtension ("html") returns "/moose/fish/foo.html"Parameters

 newExtension the new extension, either with or without a dot at the start (this doesn't make any difference). To get remove a file's extension altogether, pass an empty string into this function. 
 



See alsogetFileName, getFileExtension, hasFileExtension, getFileNameWithoutExtension