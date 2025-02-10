#### invoke()


 var JSCursor::invoke ( Span< const var > args, 
 
 Result \* result = nullptr ) const 

Invokes this node as though it were a method.If the optional Result pointer is provided it will contain Result::ok() in case of success, or an error message in case an exception was thrown during evaluation.You must only call this function for valid cursors.