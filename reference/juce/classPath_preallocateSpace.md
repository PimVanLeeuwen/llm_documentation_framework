#### preallocateSpace()


 void Path::preallocateSpace ( int numExtraCoordsToMakeSpaceFor ) 
 

Preallocates enough space for adding the given number of coordinates to the path.If you're about to add a large number of lines or curves to the path, it can make the task much more efficient to call this first and avoid costly reallocations as the structure grows. The actual value to pass is a bit tricky to calculate because the space required depends on what you're adding e.g. each lineTo() or startNewSubPath() will require 3 coords (x, y and a type marker). Each quadraticTo() will need 5, and a cubicTo() will require 7. Closing a subpath will require 1.