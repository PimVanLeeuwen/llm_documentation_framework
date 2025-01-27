#### writeToStream()


 bool ZipFile::Builder::writeToStream ( OutputStream & target, 
 
 double \* progress ) const 

Generates the zip file, writing it to the specified stream.If the progress parameter is nonnull, it will be updated with an approximate progress status between 0 and 1.0