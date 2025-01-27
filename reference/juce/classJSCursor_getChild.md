#### getChild() [2/2]


 JSCursor JSCursor::getChild ( int64 index ) const 
 

Returns a new cursor that has the same root Object as the parent and has the index parameter appended to the cursor's location.This overload will create a path that indexes into an Array.If the new path points to a location unreachable from the root, the resulting JSCursor object will be invalid. This however can change due to subsequent script executions.