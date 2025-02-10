#### getListeners()


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 

 const ArrayType & ListenerList< ListenerClass, ArrayType >::getListeners ( ) const nodiscardnoexcept 
 

Returns the raw array of listeners.Any attempt to mutate the array may result in undefined behaviour.If the array uses a mutex/CriticalSection, reading from the array without first obtaining the lock may potentially result in undefined behaviour.See alsoadd, remove, clear, contains