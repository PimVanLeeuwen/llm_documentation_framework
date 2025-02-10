#### resize()


 void var::resize ( int numArrayElementsWanted ) 
 

Treating the var as an array, this resizes it to contain the specified number of elements.If the var isn't an array, it will be converted to one, and if its value was nonvoid, this value will be kept as the first element of the new array before resizing. For more control over the array's contents, you can call getArray() and manipulate it directly as an Array<var>.