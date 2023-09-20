# Evaluation of Web Speech API for Text-to-Speech:

## Software Used

If you haven't configured [Windows Voice Recognition](https://support.microsoft.com/en-us/windows/use-voice-typing-to-talk-instead-of-type-on-your-pc-fec94565-c4bd-329d-e59a-af033fa5689f) yet, you'll need to complete the following steps:

Press Win + H, and you will receive a prompt if you need to grant permissions:

![Permission Request](./1-voice_recognition_requires_permission.png)

You can grant permissions here:

![Grant Permissions](./2-allow_voice_recognition.png)

Next, you'll need to select the spoken language you intend to use:

![Select Language](./3-installed_languages.PNG)

If you don't see your desired language, you can install it adding a preffered language or from the Windows Store:

![Install US English](./4-install_us_english.PNG)

Please check the options for installation:

![Configuration](./5-installing_us_english.PNG)

Afterward, you'll be prompted to relog. Be cautious when doing this, as the keyboard language may differ, and you may need to change it to input your credentials.

## Methodology

Press Win + H, select the location where you want to input your text, and click on the microphone to start.
Press stop when you're ready to finish.

## Initial Results

- **Conversion Speed**: Fast
- **Cost**: Free
- **Local Computer Usage Without Sending Information**: It does send information to Microsoft.
- **Limitations**: Only tested for short sentences and the results weren't bad. It didn't seem to include punctuation marks unless you use voice commands to insert them.
- **Compatibility**: Windows 10, 11
