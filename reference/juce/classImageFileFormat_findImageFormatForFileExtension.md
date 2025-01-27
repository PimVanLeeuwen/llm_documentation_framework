#### findImageFormatForFileExtension()


 static ImageFileFormat \* ImageFileFormat::findImageFormatForFileExtension ( const File & file ) static 
 

Looks for a format that can handle the given file extension.There are currently builtin formats for PNG, JPEG and GIF formats. The object that is returned should not be deleted by the caller.