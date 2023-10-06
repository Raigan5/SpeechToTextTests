# Evaluation of SeamlessM4T for Speech-To-Text on my local computer:

## Software used

[SeamlessM4T](https://seamless.metademolab.com/) is Meta's model to translate between languages and perform speech recognition. The online demo do a really good job recognizing speech, and automatically adds puntuation marks.

There is a [Github's project](https://github.com/facebookresearch/seamless_communication/tree/main) and a few models available to test it. Smaller models can be found [here](https://github.com/facebookresearch/seamless_communication/blob/main/docs/m4t/on_device_README.md)

## Methodology

First, I downloaded the [smallest model](https://huggingface.co/facebook/seamless-m4t-unity-small-s2t/resolve/main/unity_on_device_s2t.ptl) on the same folder than my program.

Then, I did a simple program to record audio and use it as an input but it didn't work.

Finally, I tried to download some audios from the Internet and convert it but the result was the same, the program [always returned "- What?"](https://github.com/facebookresearch/seamless_communication/issues/160)

## Initial Results

- **Conversion's speed**: fast
- **Cost**: free
- **Can it run on my local computer without sending information?**: Yes
- **Parametrizable (gender, dialect, speed,...)**: I wasn't able to try it.
- **Limits**: I wasn't able to try it.




