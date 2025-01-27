#### addScoped()


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 

 ErasedScopeGuard ListenerList< ListenerClass, ArrayType >::addScoped ( ListenerClass & listenerToAdd ) nodiscard 
 

Adds a listener that will be automatically removed again when the Guard is destroyed.Be very careful to ensure that the ErasedScopeGuard is destroyed or released before the ListenerList is destroyed, otherwise the ErasedScopeGuard may attempt to dereference a dangling pointer when it is destroyed, which will result in a crash.References ListenerList< ListenerClass, ArrayType >::add(), and ListenerList< ListenerClass, ArrayType >::remove().