#### invokeMethod()


 var DynamicObject::invokeMethod ( Identifier methodName, 
 
 const var::NativeFunctionArgs & args ) 

Invokes a named method on this object.The default implementation looks up the named property, and if it's a method call, then it invokes it.