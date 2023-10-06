# SpeechToTextTests
The goal is to find a suitable software for converting speech to text. What will be evaluated is:
- Conversion's speed
- Cost
- Can it run on my local computer without sending information?
- Limits

## Results

- [Web Speech API for speech recognition](./web_speech_api): it isn't supported in many browsers, and it doesn't seem to add punctuation marks.
- [SeamlessM4T](./seamless_communication): [it doesn't work on my computer](https://github.com/facebookresearch/seamless_communication/issues/160).
- [Windows Voice Recognition](./windows): Only tested for short sentences and the results weren't bad. It didn't seem to include punctuation marks unless you use voice commands to insert them.
- [Whisper online](https://openai.com/research/whisper): I still have to try it.
- [Whisper local](https://github.com/openai/whisper): I still have to try it.
- [Gladia API](https://www.gladia.io/): I still have to try it.
