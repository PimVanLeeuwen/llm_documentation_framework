#### getSystemRandom()


 static Random & Random::getSystemRandom ( ) staticnoexcept 
 

The overhead of creating a new Random object is fairly small, but if you want to avoid it, you can call this method to get a global shared Random object.Note this will return a different object per thread it's accessed from, making it thread safe. However, it's therefore important not store a reference to this object that will later be accessed from other threads.