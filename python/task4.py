from automator import LabAutomator
import numpy as np
import matplotlib.pyplot as plt

lab = LabAutomator()

lab.select_lfv()
lab.noise_on()
lab.set_noise(4)
lab.set_frequency(1000)
lab.set_deviation(700)
lab.set_amplitude(1)

# Число реализаций
N = 10
# Шаг по длительности
step = 5
tau = np.arange(10, 100, 5)

for t in tay:
    lab.set_duration(t)
    for i in range(N):
        lab.build()
        lab.save_screenshot("task4/t4s4_%.0f_%s.png" % (t, i))
        lab.clean()