#### setProperty() [2/2]


 void JSObject::setProperty ( int64 index, 
 
 const var & value ) const 

Adds a property with an integral identifier and the provided value to the underlying Object, or assigns the value to an existing property.If the underlying Object is also an Array, then the provided value will be assigned to the specified element of this Array, and ensure that it will have a size of at least index 1.