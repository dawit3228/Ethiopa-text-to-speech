#Ethiopian Text-to-speech.

 Before we start here is what i did.

  *Main Download Ubuntu 20.04 so it will install python 3.8.10
 <a href="https://www.microsoft.com/store/productId/9MTTCL66CPXJ">Here is Ubuntu 20.04</a> 

 I highly recommend you to only if u have GPU 8 and 16 ram and above which i recommend you to use CUDA  but if u don't have GPU you can use CPU just  CUDA:  True make it False just change True to False and your good to go
  > to set CUDA what this video <a href="https://youtu.be/1HzYU2_t3yc">NVIDIA CUDA installation</a>.

 > and at last download and install git<a href="https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.1/Git-2.41.0-64-bit.exe"> here to download GIT</a>.

 ##Lets Start
 1. Clone   
 ```bash
https://github.com/dawit3228/Ethiopa-text-to-speech.git
```

 2. Create virtual Enviromet 
```bash   
   python3 -m venv name 
```
   

 3. To activate
 ```bash  
source name/bin/activate 
```
 4. you need to install all the requirements.txt  
```bash
pip install -r requirements.txt
```
don't forget to install TTS 
```bash 
pip install TTS
```

 5. i upload The Audio (.wav) so you can use it ➡️<a href="https://github.com/dawit3228/Ethiopa-text-to-speech/tree/master/TTS/tts/datasets/wavs/wavs">Audio datasets</a> this is for the Text dataset to download click the link➡️<a href="https://github.com/dawit3228/Ethiopa-text-to-speech/blob/master/TTS/tts/datasets/Amharic.txt">text Dataset</a><br><br>
 6. <p>Paste this in your terminal </p> 
```bash
sudo apt-get install espeak
```
 7.<p>This wil make it editable </p> 
```bash
pip install -e .
```
<h2> If your thinking to make your own audio and train with your own voice </h2>
Prerequisites for Training a Model
For the best results when training a model, you will need:

8. Short audio recordings (at least 100) that are:<br>
        &#x2022;In 16-bit, mono PCM WAV format.<br>
        &#x2022;Between 1 and 10 seconds each.<br>
        &#x2022;Have a sample rate of 22050 Hz.<br>
        &#x2022;Have a minimum of background noise and distortion.<br>
        &#x2022;Have no long pauses of silence at the beginning 
        &#x2022;throughout the middle, and at the end.<br>
9. indicates what text is spoken in the WAV file.
10. A configuration file tailored to your data set and chosen vocoder (e.g. Tacotron, WavGrad, etc).
11. A machine with a fast CPU (ideally an nVidia GPU with CUDA support and at least 12 GB of GPU RAM; you cannot effectively use CUDA if you have less than 8 GB OF GPU RAM).
12. Lots of RAM (at least 16 GB of RAM is preferable).

<center><h2>Preparing the config.json</h2></center>
<p>You need to prepare a configuration file that describes how your custom TTS will be configured. This file is used by multiple parts of Mozilla TTS when preparing for training, performing training, and generating audio from your custom TTS. Unfortunately, though this file is very important, the documentation for Mozilla TTS largely glosses over how to customize this file.

costomize you the config.json file  <a href="https://github.com/dawit3228/Ethiopa-text-to-speech/blob/master/TTS/tts/configs/config.json"> config.json</a> </p>
so now you need to prepare the  .npy here is  
```bash
python3 TTS/bin/compute_statistics.py --config_path /path/to/your/project/config.json --out_path /path/to/your/project/scale_stats.npy
```

<b>*NOTE*</b> Don't Change  scale_stats leave it as it is .


If successful, this will generate a scale_stats.npy file under /path/to/your/project/scale_stats.npy. Be sure that the path in the audio.stats_path setting of your config.json file matches this path.
raining the Model.

It's now time for the moment of truth -- it's time to start training your model!.

<b>Only if you have GPU </b>
 
 ```bash
CUDA_VISIBLE_DEVICES="0" python3 TTS/bin/train_tacotron.py --config_path TTS/tts/configs/ljspeech_tacotron2_dynamic_conv_attn.json
```

to make sure you are using your GPU open a new terminal and paste this.
```bash
nvidia-smi
```


if you want to see your tensorboard how is train log here is it.
```bash
tensorboard --logdir=add/this/to/your/path
```
if you don't have GPU use this
```bash
python3 TTS/bin/train_tacotron.py --config_path TTS/tts/configs/ljspeech_tacotron2_dynamic_conv_attn.json
```
<br>


<p>This process will take several hours, if not days. If your machine supports CUDA and has it properly configured, the process will run more quickly than if you are just relying on CPU alone.</p>
<h1>

<b>if you have any question ask here is my instagram page</b> <a href="https://www.zemenu.org/contact.html"><b>Contact US</b></a>
</h1>

<h1><b>REMEMBER </b> if you had less dataset use more epoch </h1>
<h3>Read Documentation <a href="https://github.com/mozilla/TTS">Mozilla TTS <h3>
