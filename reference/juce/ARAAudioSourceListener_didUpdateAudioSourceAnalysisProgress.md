#### didUpdateAudioSourceAnalysisProgress()


 virtual void ARAAudioSourceListener::didUpdateAudioSourceAnalysisProgress ( ARAAudioSource \* audioSource, ARA::ARAAnalysisProgressState state, float progress ) virtual 
 

Called to notify progress when an audio source is being analyzed.Parameters

 audioSource The audio source being analyzed. 
 
 state Indicates start, intermediate update or completion of the analysis. 
 progress Progress normalized to the 0..1 range.