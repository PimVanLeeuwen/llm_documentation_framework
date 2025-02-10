#### setHWND()


 void HWNDComponent::setHWND ( void \* hwnd ) 
 

Assigns a HWND to this peer.The window will be retained and released by this component for as long as it is needed. To remove the current HWND, just call setHWND (nullptr).Note: A void\* is used here to avoid including the Windows headers as part of JuceHeader.h, but the method expects a HWND.