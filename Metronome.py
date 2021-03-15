import time as t
import  keyboard as k
from winsound import Beep

class Metronome:
    tapTempo = 0
    timeDuration = 0
    metrum = 0
    def MetronomeMsInputNormal(self):
        tapTempoIsCorrect = False
        while tapTempoIsCorrect == False:
            tapTempoInput = int(input("Insert tempo in bpm: "))
            if tapTempoInput <= 240:
                Metronome.tapTempo = tapTempoInput
                tapTempoIsCorrect = True
            else:
                print("Wrong! Input has to be equal 240bpm or lower!")
        metronome = Metronome()
        metronome.MetronomeInputs()
    def MetronomeMsInputTapTempo(self):
        tapTempoIsCorrect = False
        print("Press any key 10 times in wanted tempo.")
        while tapTempoIsCorrect == False:
            lista = []
            for i in range(10):
                k.read_hotkey()
                time = t.time()
                lista.append(time)
            tapTempoInput = (1/(lista[-1] - lista[-2]))*60
            print("\nYour tempo in bpm:\n", tapTempoInput)
            if tapTempoInput <= 240:
                Metronome.tapTempo = tapTempoInput
                tapTempoIsCorrect = True
            else:
                print("Wrong! Input has to be equal 240bpm or lower!")
        metronome = Metronome()
        metronome.MetronomeInputs()
    def MetronomeInputs(self):
        timeDurationIsCorrect = False
        while timeDurationIsCorrect == False:
            timeDurationInput = int(input("Insert time duration in seconds: "))
            if timeDurationInput <= 300:
                Metronome.timeDuration = timeDurationInput
                timeDurationIsCorrect = True
            else:
                print("Wrong! Input has to be equal 300s or lower!")
        metrumIsCorrect = False
        while metrumIsCorrect == False:
            metrumInput = int(input("Insert metrum: "))
            if metrumInput <= 7:
                Metronome.metrum = metrumInput
                metrumIsCorrect = True
            else:
                print("Wrong! Input has to be equal 7 or lower!")
        metronome = Metronome()
        metronome.MetronomeBody()
    def MetronomeBody(self):
        frequency = Metronome.tapTempo/60
        bpmPeriod=(1/frequency)
        frequencyDuration = Metronome.tapTempo/60
        time = Metronome.timeDuration*frequencyDuration
        for i in range(int(time)):
            if i%Metronome.metrum==0:
                Beep(2000,50)
                print("Pik!")
            elif i==0:
                Beep(2000,50)
                print("Pik!")
            else:
                Beep(1000,50)
                print("Pok!")
            t.sleep(bpmPeriod)

metronome = Metronome()
choiceDone = True
choice = int(input("If you want to input tempo manualy, enter 1.\nIf you want to input tempo as number, enter 2.\n"))
while choiceDone:
    if choice == 1:
        metronome.MetronomeMsInputTapTempo()
        break
    elif choice == 2:
        metronome.MetronomeMsInputNormal()
        break
    else:
        print("Wrong input. Try again.")