#### withProgramChanged()


 ChangeDetails AudioProcessorListener::ChangeDetails::withProgramChanged ( bool b ) const nodiscardnoexcept 
 

Indicates that the loaded program has changed.When this flag is set, the host should call AudioProcessor::getCurrentProgram() and update any preset list views to display the program that is currently in use.See alsoprogramChanged Referenced by getDefaultFlags().