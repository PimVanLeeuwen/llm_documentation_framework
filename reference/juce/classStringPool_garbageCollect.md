#### garbageCollect()


 void StringPool::garbageCollect ( ) 
 

Scans the pool, and removes any strings that are unreferenced.You don't generally need to call this it'll be called automatically when the pool grows large enough to warrant it.