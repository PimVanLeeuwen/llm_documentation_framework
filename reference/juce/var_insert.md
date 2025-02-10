#### insert()


 void var::insert ( int index, 
 
 const var & value ) 

Inserts an element to the var, converting it to an array if it isn't already one.If the var isn't an array, it will be converted to one, and if its value was nonvoid, this value will be kept as the first element of the new array. The parameter value will then be inserted into it. For more control over the array's contents, you can call getArray() and manipulate it directly as an Array<var>.