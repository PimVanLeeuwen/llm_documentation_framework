#### createCopy()


 virtual std::unique\_ptr< Drawable > Drawable::createCopy ( ) const pure virtual 
 

Creates a deep copy of this Drawable object.Use this to create a new copy of this and any subobjects in the tree.Implemented in DrawableComposite, DrawableImage, DrawablePath, DrawableRectangle, and DrawableText.