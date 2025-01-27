#### ~ScopedWriteLock()


 ScopedWriteLock::~ScopedWriteLock ( ) noexcept 
 

Destructor.The ReadWriteLock's exitWrite() method will be called when the destructor is called.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!