#### toHexString() [2/2]


 static String String::toHexString ( const void \* data, int size, int groupSize = 1 ) static 
 

Returns a string containing a hex dump of a block of binary data.Parameters

 data the binary data to use as input 
 
 size how many bytes of data to use 
 groupSize how many bytes are grouped together before inserting a space into the output. e.g. group size 0 has no spaces, group size 1 looks like: "be a1 c2 ff", group size 2 looks like "bea1 c2ff".