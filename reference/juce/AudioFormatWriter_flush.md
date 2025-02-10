#### flush()


 virtual bool AudioFormatWriter::flush ( ) virtual 
 

Some formats may support a flush operation that makes sure the file is in a valid state before carrying on.If supported, this means that by calling flush periodically when writing data to a large file, then it should still be left in a readable state if your program crashes. It goes without saying that this method must be called from the same thread that's calling write()! If the format supports flushing and the operation succeeds, this returns true.