#### getMachineIdentifiers()


 static StringArray SystemStats::getMachineIdentifiers ( MachineIdFlags flags ) static 
 

Returns a list of strings that can be used to uniquely identify a machine.To get multiple kinds of identifier at once, you can combine flags using bitwiseor, e.g. `uniqueId legacyUniqueId`.If a particular kind of identifier isn't available, it will be omitted from the StringArray of results, so passing `uniqueId legacyUniqueId` may return 0, 1, or 2 results, depending on the platform and whether any errors are encountered.If you've previously generated a machine ID and just want to check it against all possible identifiers, you can enable all of the flags and check whether the stored identifier matches any of the results.