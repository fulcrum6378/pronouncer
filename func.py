import soundfile as sf
import matplotlib.pyplot as plt


def audioToArray(file, fold='example', ext='wav'):
    return sf.read(fold + '/' + file + '.' + ext)


def arrayToAudio(data, file, fold='learn', ext='wav'):  # CANNOT CREATE FOLDER
    with sf.SoundFile(fold + '/' + file + '.' + ext, 'w', 44100, 1, 'PCM_24') as f:
        f.write(data)
        f.close()


def visualizeFile(file, fold='learn', ext='wav'):
    plt.plot(audioToArray(file, fold, ext)[0])
    plt.show()


def visualizeData(data):
    plt.plot(data)
    plt.show()
