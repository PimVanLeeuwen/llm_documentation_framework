#### createCopy()


 Image Image::createCopy ( ) const 
 

Creates a copy of this image.Note that it's usually more efficient to use duplicateIfShared(), because it may not be necessary to copy an image if nothing else is using it.See alsogetReferenceCount