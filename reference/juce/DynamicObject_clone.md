#### clone()


 virtual std::unique\_ptr< DynamicObject > DynamicObject::clone ( ) const virtual 
 

Returns a clone of this object.The default implementation of this method just returns a new DynamicObject with a (deep) copy of all of its properties. Subclasses can override this to implement their own custom copy routines.