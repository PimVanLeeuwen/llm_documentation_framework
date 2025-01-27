#### getSymbolValue()


 virtual Expression Expression::Scope::getSymbolValue ( const String & symbol ) const virtual 
 

Returns the value of a symbol.If the symbol is unknown, this can throw an Expression::EvaluationError exception. The member value is set to the part of the symbol that followed the dot, if there is one, e.g. for "foo.bar", symbol = "foo" and member = "bar".Exceptions

 Expression::EvaluationError 
 


Reimplemented in RelativeCoordinatePositionerBase::ComponentScope.