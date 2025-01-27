#### loadPathFromStream()


 void Path::loadPathFromStream ( InputStream & source ) 
 

Loads a stored path from a data stream.The data in the stream must have been written using writePathToStream().Note that this will append the stored path to whatever is currently in this path, so you might need to call clear() beforehand.See alsoloadPathFromData, writePathToStream