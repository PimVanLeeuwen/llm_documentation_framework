#### getPooledString() [4/4]


 String StringPool::getPooledString ( String::CharPointerType start, 
 
 String::CharPointerType end ) 

Returns a pointer to a copy of the string that is passed in.The pool will always return the same String object when asked for a string that matches it.