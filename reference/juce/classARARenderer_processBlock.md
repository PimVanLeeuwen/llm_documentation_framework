#### processBlock() [2/2]


 virtual bool ARARenderer::processBlock ( AudioBuffer< double > & buffer, AudioProcessor::Realtime realtime, const AudioPlayHead::PositionInfo & positionInfo ) virtualnoexcept 
 

Renders the output into the given buffer.Returns true if rendering executed without error, false otherwise.Parameters

 buffer The output buffer for the rendering. ARAPlaybackRenderers will replace the sample data, while ARAEditorRenderer will add to it. 
 
 realtime Indicates whether the call is executed under real time constraints. The value of this parameter may change from one call to the next, and if the value is yes, the rendering may fail if the required samples cannot be obtained in time. 
 positionInfo Current song position, playback state and playback loop location. There should be no need to access the bpm, timeSig and ppqPosition members in any ARA renderer since ARA provides that information with random access in its model graph. 


Returns false if nonARA fallback rendering is required and true otherwise.Reimplemented in ARAEditorRenderer, and ARAPlaybackRenderer.