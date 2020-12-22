from automator import LabAutomator
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
import time


current_dir = os.getcwd()
app = subprocess.Popen(os.path.join(current_dir, "Match_filter.exe"))
time.sleep(5)

lab = LabAutomator()

lab.select_lfm()
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


for t in tau:
    lab.set_duration(t)
    for i in range(N):
        lab.build()
        lab.save_screenshot("task4/t4s4_%.0f_%s.png" % (t, i))
        lab.save_output("task4/t4s4_%.0f_%s_out.png" % (t, i))
        lab.clean()