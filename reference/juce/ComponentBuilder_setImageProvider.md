#### setImageProvider()


 void ComponentBuilder::setImageProvider ( ImageProvider \* newImageProvider ) noexcept 
 

Gives the builder an ImageProvider object that the type handlers can use when loading images from stored references.The object that is passed in is not owned by the builder, so the caller must delete it when it is no longer needed, but not while the builder may still be using it. To clear the image provider, just call setImageProvider (nullptr).