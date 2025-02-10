#### startNewSubPath() [2/2]


 void Path::startNewSubPath ( Point< float > start ) 
 

Begins a new subpath with a given starting position.This will move the path's current position to the coordinates passed in and make it ready to draw lines or curves starting from this position.After adding whatever lines and curves are needed, you can either close the current subpath using closeSubPath() or call startNewSubPath() to move to a new subpath, leaving the old one openended.See alsolineTo, quadraticTo, cubicTo, closeSubPath