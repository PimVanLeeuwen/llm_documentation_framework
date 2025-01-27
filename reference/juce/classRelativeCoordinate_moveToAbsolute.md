#### moveToAbsolute()


 void RelativeCoordinate::moveToAbsolute ( double absoluteTargetPosition, 
 
 const Expression::Scope \* evaluationScope ) 

Changes the value of this coord to make it resolve to the specified position.Calling this will leave the anchor points unchanged, but will set this coordinate's absolute or relative position to whatever value is necessary to make its resultant position match the position that is provided.