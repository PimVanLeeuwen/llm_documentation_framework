#### getVSTXML()


 static const XmlElement \* VSTPluginFormat::getVSTXML ( AudioPluginInstance \* plugin ) static 
 

Attempts to retrieve the VSTXML data from a plugin.Will return nullptr if the plugin isn't a VST, or if it doesn't have any VSTXML.