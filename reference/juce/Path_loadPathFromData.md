#### loadPathFromData()


 void Path::loadPathFromData ( const void \* data, 
 
 size\_t numberOfBytes ) 

Loads a stored path from a block of data.This is similar to loadPathFromStream(), but just reads from a block of data. Useful if you're including stored shapes in your code as a block of static data.See alsoloadPathFromStream, writePathToStream