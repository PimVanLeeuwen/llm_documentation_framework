#### bindDocumentToPluginInstance()


 ARAHostModel::PlugInExtensionInstance ARAHostDocumentController::bindDocumentToPluginInstance ( AudioPluginInstance & instance, 
 
 ARA::ARAPlugInInstanceRoleFlags knownRoles, 
 ARA::ARAPlugInInstanceRoleFlags assignedRoles ) 

Binds the ARAHostDocumentController and its enclosed document to a plugin instance.The resulting ARAHostModel::PlugInExtensionInstance is responsible for fulfilling the ARA specific roles of the plugin.A single DocumentController can be bound to multiple plugin instances, which is a typical practice among hosts.