from automator import LabAutomator

lab = LabAutomator()

lab.select_videopulse()
lab.set_amplitude(1)
lab.set_duration(10)
lab.build()
lab.save_screenshot("task1/t1s1_10.png")
lab.clean()

lab.set_duration(20)
lab.build()
lab.save_screenshot("task1/t1s1_20.png")
lab.clean()



lab.select_radiopulse()
lab.set_amplitude(1)
lab.set_duration(10)
lab.set_frequency(400)
lab.build()
lab.save_screenshot("task1/t1s2_10.png")
lab.clean()

lab.set_duration(20)
lab.set_frequency(400)
lab.build()
lab.save_screenshot("task1/t1s2_20.png")
lab.clean()



lab.select_lfm()
lab.set_amplitude(1)
lab.set_duration(100)
lab.set_frequency(1000)
lab.set_deviation(500)
lab.build()
lab.save_screenshot("task1/t1s3_500.png")
lab.clean()

lab.set_deviation(1000)
lab.build()
lab.save_screenshot("task1/t1s3_1000.png")
lab.clean()



lab.select_barker()
lab.set_amplitude(1)
lab.set_duration(13)
lab.build()
lab.save_screenshot("task1/t1s4_13.png")
lab.clean()

lab.set_duration(26)
lab.build()
lab.save_screenshot("task1/t1s4_26.png")
lab.clean()