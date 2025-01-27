#### withNonParameterStateChanged()


 ChangeDetails AudioProcessorListener::ChangeDetails::withNonParameterStateChanged ( bool b ) const nodiscardnoexcept 
 

Indicates that the plugin state has changed (but not its parameters!).An AudioProcessor can call updateHostDisplay with this flag set to notify the host that its state has changed in a way that requires resaving.If a host receives a call to audioProcessorChanged with this flag set, it should offer to save the plugin state before taking any actions that might irrevocably destroy the current plugin state, such as closing the project.See alsononParameterStateChanged