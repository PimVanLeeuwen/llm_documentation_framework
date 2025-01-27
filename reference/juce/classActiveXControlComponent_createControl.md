#### createControl()


 bool ActiveXControlComponent::createControl ( const void \* controlIID ) 
 

Tries to create an ActiveX control and embed it in this peer.The peer controlIID is a pointer to an IID structure it's treated as a void\* because when including the JUCE headers, you might not always have included windows.h first, in which case IID wouldn't be defined.e.g.const IID myIID = \_\_uuidof (QTControl);
myControlComp>createControl (&myIID);