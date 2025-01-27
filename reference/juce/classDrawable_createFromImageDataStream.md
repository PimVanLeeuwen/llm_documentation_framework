#### createFromImageDataStream()


 static std::unique\_ptr< Drawable > Drawable::createFromImageDataStream ( InputStream & dataSource ) static 
 

Tries to turn a stream containing some kind of image data into a drawable.The data could be an image that the ImageFileFormat class understands, or it could be SVG.