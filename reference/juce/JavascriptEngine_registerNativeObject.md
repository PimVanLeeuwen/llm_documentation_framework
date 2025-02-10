#### registerNativeObject()


 void JavascriptEngine::registerNativeObject ( const Identifier & objectName, 
 
 DynamicObject \* object ) 

Adds a native object to the root namespace.The object passedin is referencecounted, and will be retained by the engine until the engine is deleted. The name must be a simple JS identifier, without any dots.