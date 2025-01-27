#### read()


 std::array< Range< int >, 2 > SingleThreadedAbstractFifo::read ( int num ) 
 

Returns two blocks in the buffer from which new items may be read.Note that if the buffer doesn't have the requested number of items available, the sum of the lengths of the returned ranges may be less than num!References jmin().