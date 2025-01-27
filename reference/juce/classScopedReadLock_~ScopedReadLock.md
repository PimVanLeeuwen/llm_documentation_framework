#### ~ScopedReadLock()


 ScopedReadLock::~ScopedReadLock ( ) noexcept 
 

Destructor.The ReadWriteLock's exitRead() method will be called when the destructor is called.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!