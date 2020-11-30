
print('please give your browser path (ex : C:\Program Files\Google\Chrome\Application\chrome.exe)')
browser = input()
f = open('./browser_path.txt', 'w')
f.write(browser)


import subprocess as sp

sp.call('pip install pyttsx3')
sp.call('pip install discord')
sp.call('pip install youtube-search')
sp.call('pip install SpeechRecognition')
sp.call('pip install wikipedia')
sp.call('pip install urllib3')

pyAudioFile = open('./module/PyAudio-0.2.11-cp39-cp39-win_amd64.whl', 'r')
sp.call('pip install '+pyAudioFile.name)

