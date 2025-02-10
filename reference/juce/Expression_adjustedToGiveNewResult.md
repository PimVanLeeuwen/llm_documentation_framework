#### adjustedToGiveNewResult()


 Expression Expression::adjustedToGiveNewResult ( double targetValue, 
 
 const Scope & scope ) const 

Attempts to return an expression which is a copy of this one, but with a constant adjusted to make the expression resolve to a target value.E.g. if the expression is "x + 10" and x is 5, then asking for a target value of 8 will return the expression "x + 3". Obviously some expressions can't be reversed in this way, in which case they might just be adjusted by adding a constant to the original expression.Exceptions

 Expression::EvaluationError