#### createFromImageData()


 static std::unique\_ptr< Drawable > Drawable::createFromImageData ( const void \* data, size\_t numBytes ) static 
 

Tries to turn some kind of image file into a drawable.The data could be an image that the ImageFileFormat class understands, or it could be SVG.