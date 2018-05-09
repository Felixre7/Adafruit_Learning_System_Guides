import neopixel
import analogio
import time
import board

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)
light = analogio.AnalogIn(board.LIGHT)

# Turn only pixel #1 green
pixels[1] = (0, 255, 0)

# How many light readings per sample
NUM_OVERSAMPLE = 10
# How many samples we take to calculate 'average'
NUMSAMPLES = 20
samples = [0] * NUMSAMPLES

while True:
    for i in range(NUMSAMPLES):
        # Take 'NUM_OVERSAMPLE'  # readings really fast
        oversample = 0
        for s in range(NUM_OVERSAMPLE):
            oversample += float(light.value)
        # and save the average from the oversamples
        samples[i] = oversample / NUM_OVERSAMPLE        # Find the aver

        mean = sum(samples) / float(len(samples))  # take the average
        print((samples[i]-mean,))                  # 'center' the reading
        time.sleep(0.025)                          # change to go faster/slower
