#### AudioProcessorParameter() [2/2]


 AudioProcessorParameter::AudioProcessorParameter ( int versionHint ) explicit 
 

The version hint supplied to this constructor is used in Audio Unit plugins to aid ordering parameter identifiers when JUCE\_FORCE\_USE\_LEGACY\_PARAM\_IDS is not enabled.When adding a parameter that is not present in a previous version of the Audio Unit, you must ensure that the version hint supplied is a number higher than that of any parameter in any previous plugin version.For example, in the first release of a plugin, every parameter was created with "1" as a version hint. If you add some parameters in the second release of the plugin, all of the new parameters should have "2" as a version hint. Additional parameters added in subsequent plugin versions should have "3", "4", and so forth, increasing monotonically.Note that adding or removing parameters with a version hint that is lower than the maximum version hint of all parameters will break saved automation in some hosts, so be careful!A version hint of "0" will be treated as though the version hint has not been set explicitly. When targeting the AU format, the version hint may be checked at runtime in debug builds to ensure that it has been set.Rationale:According to Apple's Documentation:‍An audio unit parameter is uniquely identified by the combination of its scope, element, and ID.However, Logic Pro and GarageBand have a known limitation that causes them to use parameter indices instead of IDs to identify parameters. The effect of this is that adding parameters to a later version of a plugin can break automation saved with an earlier version of the plugin if the indices of existing parameters are changed. It is always unsafe to remove parameters from an Audio Unit plugin that will be used in one of these hosts, because removing a parameter will always modify the indices of following parameters.In order to work around this limitation, parameters in AUv2 plugins are sorted first by their version hint, and then by the hash of their string identifier. As long as the parameters from later versions of the plugin always have a version hint that is higher than the parameters from earlier versions of the plugin, recall of automation data will work as expected in Logic and GarageBand.Note that we can't just use the JUCE parameter index directly in order to preserve ordering. This would require all new parameters to be added at the end of the parameter list, which would make it impossible to add parameters to existing parameter groups. It would also make it awkward to structure code sensibly, undoing all of the benefits of stringbased parameter identifiers.At time of writing, AUv3 plugins seem to be affected by the same issue, but there does not appear to be any API to control parameter indices in this format. Therefore, when building AUv3 plugins you must not add or remove parameters in subsequent plugin versions if you wish to support Logic and GarageBand.

The documentation for this struct was generated from the following file:juce\_HostedAudioProcessorParameter.h
### Purchase

Get JUCE
### Discover

What's New in JUCEFeatures
### Learn

DocumentaionTutorialsMade with JUCEResources
### Support

JUCE ForumNewsletterArchive
### About

Contact UsJUCE LegalJUCE Licensing FAQ
### Events

Audio Developer Conference
Visit our FacebookVisit our TwitterVisit our LinkedInVisit our YouTube channel© Raw Material Software Limited
linkedin




facebook


pinterest


youtube


rss


twitter


instagram




facebookblank


rssblank


linkedinblank


pinterest


youtube


twitter


instagram