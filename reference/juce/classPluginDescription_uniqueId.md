#### uniqueId


 int PluginDescription::uniqueId = 0 
 

A unique ID for the plugin.Note that this might not be unique between formats, e.g. a VST and some other format might actually have the same id.The uniqueId field replaces the deprecatedUid field, and fixes an issue where VST3 plugins with matching FUIDs would generate different uid values depending on the platform. The deprecatedUid field is kept for backwards compatibility, allowing existing hosts to migrate from the old uid to the new uniqueId.See alsocreateIdentifierString