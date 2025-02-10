#### setMethod()


 void DynamicObject::setMethod ( Identifier methodName, 
 
 var::NativeFunction function ) 

Adds a method to the class.This is basically the same as calling setProperty (methodName, (var::NativeFunction) myFunction), but helps to avoid accidentally invoking the wrong type of var constructor. It also makes the code easier to read.