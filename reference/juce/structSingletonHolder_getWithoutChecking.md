#### getWithoutChecking()


template<typename Type , typename MutexType , bool onlyCreateOncePerRun> 

 Type \* SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::getWithoutChecking ( ) 
 

Returns the current instance, or creates a new instance if there isn't one, but doesn't do any locking, or checking for recursion or error conditions.References SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::instance.Referenced by SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::get().