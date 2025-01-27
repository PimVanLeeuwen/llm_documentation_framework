#### doStoreObjectsToStream()


 virtual bool ARADocumentControllerSpecialisation::doStoreObjectsToStream ( ARAOutputStream & output, const ARAStoreObjectsFilter \* filter ) protectedpure virtual 
 

Write an ARADocument archive to a juce::OutputStream.Parameters

 output Data stream that should be used to write the persistent ARADocument data 
 
 filter A filter to be applied to the stream 


Returns true if the operation is successful.See alsoARADocumentControllerInterface::storeObjectsToArchive