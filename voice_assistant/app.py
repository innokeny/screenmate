import queue
import sounddevice as sd
import vosk
import json
from . import words
from .skills import *
from .voice import speaker
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.linear_model import LogisticRegression

q = queue.Queue()

model = vosk.Model('voice_assistant/model-small')

device = sd.default.device 
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def recognize(screen_mate):
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                trg = words.TRIGGERS.intersection(data.split())
                if trg:
                    screen_mate.set_talking_mode(True)
                    data = data.replace(list(trg)[0], '')
                    text_vector = vectorizer.transform([data]).toarray()[0]
                    answer = clf.predict([text_vector])[0]
                    print(answer)
                    func_name = answer.split()[0]
                    speaker(answer.replace(func_name, ''))
                    exec(func_name + '()')
                    screen_mate.set_talking_mode(False)
            else:
                print(rec.PartialResult())
