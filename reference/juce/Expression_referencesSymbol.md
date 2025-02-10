#### referencesSymbol()


 bool Expression::referencesSymbol ( const Symbol & symbol, 
 
 const Scope & scope ) const 

Returns true if this expression makes use of the specified symbol.If a suitable scope is supplied, the search will dereference and recursively check all symbols, so that it can be determined whether this expression relies on the given symbol at any level in its evaluation. If the scope parameter is null, this just checks whether the expression contains any direct references to the symbol.Exceptions

 Expression::EvaluationError