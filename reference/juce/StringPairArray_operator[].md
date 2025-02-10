#### operator[]()


 const String & StringPairArray::operator[] ( StringRef key ) const 
 

Finds the value corresponding to a key string.If no such key is found, this will just return an empty string. To check whether a given key actually exists (because it might actually be paired with an empty string), use the getAllKeys() method to obtain a list.Obviously the reference returned shouldn't be stored for later use, as the string it refers to may disappear when the array changes.See alsogetValue