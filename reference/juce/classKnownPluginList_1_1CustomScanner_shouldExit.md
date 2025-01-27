#### shouldExit()


 bool KnownPluginList::CustomScanner::shouldExit ( ) const noexcept 
 

Returns true if the current scan should be abandoned.Any blocking methods should check this value repeatedly and return if if becomes true.