#### queryInterface()


 void \* ActiveXControlComponent::queryInterface ( const void \* iid ) const 
 

Does a QueryInterface call on the embedded control object.This allows you to cast the control to whatever type of COM object you need.The iid parameter is a pointer to an IID structure it's treated as a void\* because when including the JUCE headers, you might not always have included windows.h first, in which case IID wouldn't be defined, but you should just pass a pointer to an IID.e.g.const IID iid = \_\_uuidof (IOleWindow);
 
IOleWindow\* oleWindow = (IOleWindow\*) myControlComp>queryInterface (&iid);
 
if (oleWindow != nullptr)
{
 HWND hwnd;
 oleWindow>GetWindow (&hwnd);
 
 ...
 
 oleWindow>Release();
}