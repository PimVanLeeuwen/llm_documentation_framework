#### getSpecialisedDocumentController()


template<typename Specialisation = ARADocumentControllerSpecialisation> 

 static Specialisation \* ARADocumentControllerSpecialisation::getSpecialisedDocumentController ( ARA::PlugIn::DocumentController \* dc ) static 
 

Returns a pointer to the ARADocumentControllerSpecialisation instance that is referenced by the provided DocumentController.You can use this function to access your specialisation from anywhere where you have access to ARA::PlugIn::DocumentController\*.