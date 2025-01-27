#### duplicateIfShared()


 void Image::duplicateIfShared ( ) 
 

Makes sure that no other Image objects share the same underlying data as this one.If no other Image objects refer to the same shared data as this one, this method has no effect. But if there are other references to the data, this will create a new copy of the data internally.Call this if you want to draw onto the image, but want to make sure that this doesn't affect any other code that may be sharing the same data.See alsogetReferenceCount