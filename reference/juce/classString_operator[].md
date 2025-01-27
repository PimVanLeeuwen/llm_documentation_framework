#### operator[]()


 juce\_wchar String::operator[] ( int index ) const noexcept 
 

Returns the character at this index in the string.In a release build, no checks are made to see if the index is within a valid range, so be careful! In a debug build, the index is checked and an assertion fires if it's outofrange.Also beware that depending on the encoding format that the string is using internally, this method may execute in either O(1) or O(n) time, so be careful when using it in your algorithms. If you're scanning through a string to inspect its characters, you should never use this operator for random access, it's far more efficient to call getCharPointer() to return a pointer, and then to use that to iterate the string.See alsogetCharPointer