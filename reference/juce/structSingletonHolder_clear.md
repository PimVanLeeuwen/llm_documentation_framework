#### clear()


template<typename Type , typename MutexType , bool onlyCreateOncePerRun> 

 void SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::clear ( Type \* expectedObject ) noexcept 
 

Called by the class's destructor to clear the pointer if it is currently set to the given object.References SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::instance.

Member Data Documentation