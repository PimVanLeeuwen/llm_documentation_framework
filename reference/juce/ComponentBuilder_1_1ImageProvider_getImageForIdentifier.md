#### getImageForIdentifier()


 virtual Image ComponentBuilder::ImageProvider::getImageForIdentifier ( const var & imageIdentifier ) pure virtual 
 

Retrieves the image associated with this identifier, which could be any kind of string, number, filename, etc.The image that is returned will be owned by the caller, but it may come from the ImageCache.