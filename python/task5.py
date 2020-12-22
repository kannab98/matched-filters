from automator import LabAutomator

lab = LabAutomator()
# 1
# lab.signal2_on()
# lab.select_videopulse()
# lab.select_videopulse()
# lab.select_videopulse()
# lab.set_amplitude(1)
# lab.set_signal2_amplitude(1)
# lab.filter_on()

# durations = [10, 20, 40]
# delays = [5, 10, 15, 20, 30, 40]
# for delay in delays:
#     lab.set_signal2_delay(delay)
    # for dur in durations:
    #     lab.set_duration(dur)
    #     lab.build()
    #     lab.save_screenshot("task5/t5s1_dur{}_del{}.png".format(dur, delay))
    #     lab.clean()



# 2.1
deviations = [200]
# deviations = [200, 400, 800]
durations = [10]
# durations = [10, 20, 40]
delays = [5, 10, 15, 20, 30, 40]
delays = range(40)

lab.signal2_on()
lab.select_lfm()
lab.set_duration(30)
lab.set_frequency(3000)
lab.set_amplitude(1)
lab.filter_on()

lab.set_signal2_amplitude(1)
for delay in delays:
    lab.set_signal2_delay(delay)
    for dev in deviations:
        lab.set_deviation(dev)
        for dur in durations:
            lab.set_duration(dur)
            lab.build()
            lab.save_screenshot("task5/t5s21_dur{}_del{}_dev{}.png".format(dur, delay, dev))
            lab.clean()

# 2.2 
# lab.select_lfm()
# lab.set_amplitude(1)
# lab.set_signal2_amplitude(1/6)
# lab.set_signal2_delay(30)
# for dev in deviations:
#     for dur in durations:
#         lab.set_deviation(dev)
#         lab.build()
#         lab.save_screenshot("task5/t5s22_{}_{}.png".format(dur, dev))
#         lab.clean()