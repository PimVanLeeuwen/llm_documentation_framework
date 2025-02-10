#### writeToStream()


 void ValueTree::writeToStream ( OutputStream & output ) const 
 

Stores this tree (and all its children) in a binary format.Once written, the data can be read back with readFromStream().It's much faster to load/save your tree in binary form than as XML, but obviously isn't humanreadable.