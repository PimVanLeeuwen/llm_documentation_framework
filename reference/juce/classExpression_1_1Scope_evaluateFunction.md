#### evaluateFunction()


 virtual double Expression::Scope::evaluateFunction ( const String & functionName, const double \* parameters, int numParameters ) const virtual 
 

Executes a named function.If the function name is unknown, this can throw an Expression::EvaluationError exception.Exceptions

 Expression::EvaluationError