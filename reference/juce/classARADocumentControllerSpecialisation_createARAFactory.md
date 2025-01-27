#### createARAFactory()


template<typename SpecialisationType > 

 static const ARA::ARAFactory \* ARADocumentControllerSpecialisation::createARAFactory ( ) static 
 

Helper function for implementing the global createARAFactory() function.For exampleclass MyDocumentController : public ARADocumentControllerSpecialisation
{
 //...
};
 
const ARA::ARAFactory\* JUCE\_CALLTYPE createARAFactory()
{
 return juce::ARADocumentControllerSpecialisation::createARAFactory<MyDocumentController>();
}