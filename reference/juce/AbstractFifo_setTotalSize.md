#### setTotalSize()


 void AbstractFifo::setTotalSize ( int newSize ) noexcept 
 

Changes the buffer's total size.Note that this isn't threadsafe, so don't call it if there's any danger that it might overlap with a call to any other method in this class!