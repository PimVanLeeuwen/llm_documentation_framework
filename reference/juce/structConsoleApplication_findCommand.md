#### findCommand()


 const Command \* ConsoleApplication::findCommand ( const ArgumentList & , 
 
 bool optionMustBeFirstArg ) const 

Looks for the first command in the list which matches the given arguments.If none is found, this returns either the default command (if one is set) or nullptr. If optionMustBeFirstArg is true, then only the first argument will be looked at when searching the available commands this lets you do 'git' style commands where the executable name is followed by a verb.