#### createFromSVGFile()


 static std::unique\_ptr< Drawable > Drawable::createFromSVGFile ( const File & svgFile ) static 
 

Attempts to parse an SVG (Scalable Vector Graphics) document from a file, and to turn this into a Drawable tree.If something goes wrong while parsing, it may return nullptr.SVG is a pretty large and complex spec, and this doesn't aim to be a full implementation, but it can return the basic vector objects.Any references to references to external image files will be relative to the parent directory of the file passed.