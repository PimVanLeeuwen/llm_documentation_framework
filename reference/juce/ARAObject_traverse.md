#### traverse()


template<typename Fn > 

 void ARAObject::traverse ( Fn && fn ) 
 

Implements a depth first traversal of the ARA model graph starting from the current object, and visiting its children recursively.The provided function should accept a single ARAObject& parameter.References getChild(), getNumChildren(), and traverse().Referenced by traverse().