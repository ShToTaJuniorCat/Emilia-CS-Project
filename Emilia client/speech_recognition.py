import pyaudio
import wave
import struct
from datetime import datetime
from threading import Thread
from constants import stt_const


class Recording:
    def __init__(self, threshold = 0):
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.current_chunk = b""
        self.stream = None
        self.threshold = threshold
        threshold_thread = Thread(target=self.calibrate_threshold)
        threshold_thread.run()
        

    def get_silence_rms(self):
        """
        Find the rms of the room when it's silent.
        This rms is good as a threshold:
            Every chunk of a recording that is above this threshold,
            is considered to be a non-silent chunk.
            Below this threshold is a silent chunk.
        """

        self.stream = self.p.open(format=stt_const.SAMPLE_FORMAT,
                                  channels=stt_const.CHANNELS,
                                  rate=stt_const.FS,
                                  frames_per_buffer=stt_const.CHUNK,
                                  input=True)

        print("A moment of silence, please...")
        start = datetime.now().timestamp()
        silent_chunk = self.stream.read(stt_const.CHUNK)
        avg_rms = self.calc_rms(silent_chunk)

        while datetime.now().timestamp() - start < stt_const.THRESHOLD_CALC_TIME:
            silent_chunk = self.stream.read(stt_const.CHUNK)
            avg_rms = (avg_rms + self.calc_rms(silent_chunk)) / 2

        self.stream.stop_stream()
        self.stream.close()

        return avg_rms


    @staticmethod
    def calc_rms(chunk):
        if chunk == b"":
            return 0.0

        count = len(chunk) / 2
        shorts = struct.unpack("%dh" % (count), chunk)

        sum_squares = 0.0
        for sample in shorts:
            sum_squares += pow(sample * (1.0 / 32768.0), 2)

        return pow(sum_squares / count, 0.5) * 1000


    def calibrate_threshold(self):
        self.threshold = self.get_silence_rms() + stt_const.ADD_THRESHOLD
        print(f"Calibration done. Threshold: {self.threshold}")
        return self.threshold
    

    def record_until_silence(self):
        self.frames = []
        start = datetime.now().timestamp()
        self.stream = self.p.open(format=stt_const.SAMPLE_FORMAT,
                                  channels=stt_const.CHANNELS,
                                  rate=stt_const.FS,
                                  frames_per_buffer=stt_const.CHUNK,
                                  input=True)

        # For when the user isn't talking.
        while self.calc_rms(self.current_chunk) < self.threshold and (datetime.now().timestamp() - start) < stt_const.MIN_DURATION:
            self.current_chunk = self.stream.read(stt_const.CHUNK)
            self.frames.append(self.current_chunk)

        start = datetime.now().timestamp()
        
        # For when the user has started talking.
        # Run until he's finished.
        while self.calc_rms(self.current_chunk) > self.threshold or datetime.now().timestamp() - start < stt_const.SILENCE_TIME:
            # Finally, the user is talking!
            self.current_chunk = self.stream.read(stt_const.CHUNK)
            self.frames.append(self.current_chunk)
            if self.calc_rms(self.current_chunk) > self.threshold:
                start = datetime.now().timestamp()

        print("Finished recording")

        # Stop and close the stream
        self.stream.stop_stream()
        self.stream.close()
        # Terminate the PortAudio interface
        # self.p.terminate()

        return self.frames

    def close_recorder(self):
        self.p.close()


def record_n_save(recorder):
    p = recorder.p
    frames = recorder.record_until_silence()

    # Save the recorded data as a WAV file
    wf = wave.open(stt_const.FILENAME, 'wb')
    wf.setnchannels(stt_const.CHANNELS)
    wf.setsampwidth(p.get_sample_size(stt_const.SAMPLE_FORMAT))
    wf.setframerate(stt_const.FS)
    wf.writeframes(b''.join(frames))
    wf.close()


def setup_whisper():
    import whisper
    global whisper
    global model
    model = whisper.load_model(stt_const.MODEL,
                               download_root=r"C:\Users\USER\AppData\Local\Programs\Python\Python310\whisper-models")


def transcribe():
    audio = whisper.load_audio(stt_const.FILENAME)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    result = model.transcribe(stt_const.FILENAME)
    return result["text"]


def get_input(recorder):
    # Record user input
    record_n_save(recorder)

    # Transcribe user's audio input into text and return it
    return transcribe()


whisper_thread = Thread(target=setup_whisper)
whisper_thread.run()
