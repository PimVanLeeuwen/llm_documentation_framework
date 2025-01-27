#### get32BitResolution()


template<typename SampleFormat , typename Endianness , typename InterleavingType , typename Constness > 

 static int AudioData::Pointer< SampleFormat, Endianness, InterleavingType, Constness >::get32BitResolution ( ) staticnoexcept 
 

Returns the accuracy of this format when represented as a 32bit integer.This is the smallest number above 0 that can be represented in the sample format, converted to a 32bit range. E,g. if the format is 8bit, its resolution is 0x01000000; if the format is 24bit, its resolution is 0x100.