#### next()


 bool PathFlatteningIterator::next ( ) 
 

Fetches the next line segment from the path.This will update the member variables x1, y1, x2, y2, subPathIndex and closesSubPath so that they describe the new line segment.Returnsfalse when there are no more lines to fetch.