#### doRestoreObjectsFromStream()


 virtual bool ARADocumentControllerSpecialisation::doRestoreObjectsFromStream ( ARAInputStream & input, const ARARestoreObjectsFilter \* filter ) protectedpure virtual 
 

Read an ARADocument archive from a juce::InputStream.Parameters

 input Data stream containing previously persisted data to be used when restoring the ARADocument 
 
 filter A filter to be applied to the stream 


Return true if the operation is successful.See alsoARADocumentControllerInterface::restoreObjectsFromArchive