#### closeSubPath()


 void Path::closeSubPath ( ) 
 

Closes a the current subpath with a line back to its startpoint.When creating a closed shape such as a triangle, don't use 3 lineTo() calls instead use two lineTo() calls, followed by a closeSubPath() to join the final point back to the start.This ensures that closes shapes are recognised as such, and this is important for tasks like drawing strokes, which needs to know whether to draw endcaps or not.See alsostartNewSubPath, lineTo, quadraticTo, cubicTo, closeSubPath