#### write()


 std::array< Range< int >, 2 > SingleThreadedAbstractFifo::write ( int num ) 
 

Returns two blocks in the buffer where new items may be written.Note that if the buffer is running low on free space, the sum of the lengths of the returned ranges may be less than num!References getRemainingSpace(), and jmin().