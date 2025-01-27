#### references()


 bool RelativeCoordinate::references ( const String & coordName, 
 
 const Expression::Scope \* evaluationScope ) const 

Returns true if this coordinate uses the specified coord name at any level in its evaluation.This will recursively check any coordinates upon which this one depends.