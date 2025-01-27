#### withParameterInfoChanged()


 ChangeDetails AudioProcessorListener::ChangeDetails::withParameterInfoChanged ( bool b ) const nodiscardnoexcept 
 

Indicates that some attributes of the AudioProcessor's parameters have changed.When this flag is set, the host should rescan the AudioProcessor's parameters, and update its controls to match. This is often used to update the names of a plugin's parameters in the host.See alsoparameterInfoChanged Referenced by getDefaultFlags().