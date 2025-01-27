#### createFromImageFile()


 static std::unique\_ptr< Drawable > Drawable::createFromImageFile ( const File & file ) static 
 

Tries to turn a file containing some kind of image data into a drawable.The data could be an image that the ImageFileFormat class understands, or it could be SVG.