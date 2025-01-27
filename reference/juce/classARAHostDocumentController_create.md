#### create()


 static std::unique\_ptr< ARAHostDocumentController > ARAHostDocumentController::create ( ARAFactoryWrapper factory, const String & documentName, std::unique\_ptr< ARA::Host::AudioAccessControllerInterface > audioAccessController, std::unique\_ptr< ARA::Host::ArchivingControllerInterface > archivingController, std::unique\_ptr< ARA::Host::ContentAccessControllerInterface > contentAccessController = nullptr, std::unique\_ptr< ARA::Host::ModelUpdateControllerInterface > modelUpdateController = nullptr, std::unique\_ptr< ARA::Host::PlaybackControllerInterface > playbackController = nullptr ) static 
 

Factory function.You must check if the returned pointer is valid.