#### deleteInstance()


template<typename Type , typename MutexType , bool onlyCreateOncePerRun> 

 void SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::deleteInstance ( ) 
 

Deletes and resets the current instance, if there is one.References SingletonHolder< Type, MutexType, onlyCreateOncePerRun >::instance.