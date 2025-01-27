#### getJob()


 ThreadPoolJob \* ThreadPool::getJob ( int index ) const noexcept 
 

Returns one of the jobs in the queue.Note that this can be a very volatile list as jobs might be continuously getting shifted around in the list, and this method may return nullptr if the index is currently outofrange.