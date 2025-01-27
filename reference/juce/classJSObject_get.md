#### get()


 var JSObject::get ( ) const 
 

Returns a variant with a value of the property under the given name.If no such property exists an undefined variant is returned.If this property points to an object created by JavascriptEngine::registerNativeObject(), then the returned variant will contain a pointer to the original object and can be acquired by variant::getDynamicObject().