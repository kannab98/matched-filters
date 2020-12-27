from automator import LabAutomator

lab.select_lfm()

# Неизменяемые параметры
lab.set_duration(10)
lab.set_frequency(1000)

lab.set_deviation()
# lab.build()
# lab.save_screenshot("task1/t1s1_10.png")
# lab.clean()