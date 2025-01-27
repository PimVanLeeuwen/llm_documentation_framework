#### get()


template<typename Type , typename MutexType , bool onlyCreateOncePerRun> 

 Type \* SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::get ( ) 
 

Returns the current instance, or creates a new instance if there isn't one.References SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::getWithoutChecking(), SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::instance, and jassertfalse.