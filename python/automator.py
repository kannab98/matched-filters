import pyautogui as pag
import time

width, height = pag.size()

# pag.PAUSE = 0.5
lab_width, lab_height = 1182, 745


class LabAutomator:
    def __init__(self):
        try:
            self._build_btn = pag.center(pag.locateOnScreen('materials/build.png'))
            try:
                self._clean_btn = pag.center(pag.locateOnScreen('materials/clean.png'))
            except Exception as e:
                self._clean_btn = pag.center(pag.locateOnScreen('materials/clean2.png'))
                print("Found de-activated CLEAN button")

            dur_loc_x, dur_loc_y = pag.center(
                pag.locateOnScreen('materials/duration.png'))
            dur_loc_x += 50
            self._dur_input = (dur_loc_x, dur_loc_y)

            amp_loc_x, amp_loc_y = pag.center(
                pag.locateOnScreen('materials/amplitude.png'))
            amp_loc_x += 50
            self._amp_input = (amp_loc_x, amp_loc_y)

            try:
                ff_loc_x, ff_loc_y = pag.center(
                    pag.locateOnScreen('materials/fill_freq.png'))
            except Exception as e:
                ff_loc_x, ff_loc_y = pag.center(pag.locateOnScreen('materials/fill_freq2.png'))
                print("Found de-activated freq button")
            ff_loc_x += 50
            self._freq_input = (ff_loc_x, ff_loc_y)

            try:
                dev_loc_x, dev_loc_y = pag.center(
                    pag.locateOnScreen('materials/deviation.png'))
            except Exception as e:
                dev_loc_x, dev_loc_y = pag.center(
                    pag.locateOnScreen('materials/deviation2.png'))
                print("Found de-activated deviation button")
            dev_loc_x += 50
            self._dev_input = (dev_loc_x, dev_loc_y)

            self._barker = pag.center(pag.locateOnScreen('materials/barker.png'))
            self._lfm = pag.center(pag.locateOnScreen('materials/lfm.png'))
            self._radiopulse = pag.center(pag.locateOnScreen('materials/radiopulse.png'))
            self._videopulse = pag.center(pag.locateOnScreen('materials/videopulse.png'))
            
            try:
                self._filter = pag.center(pag.locateOnScreen('materials/fill_off.png'))
            except Exception as e:
                self._filter = pag.center(pag.locateOnScreen('materials/fill_on.png'))
                print("Found activated Filter button")

            try:
                self._noise = pag.center(pag.locateOnScreen('materials/noise_off.png'))
            except Exception as e:
                self._noise = pag.center(pag.locateOnScreen('materials/noise_on.png'))
                print("Found activated Noise button")

            try:
                noise_loc_x, noise_loc_y = pag.center(
                    pag.locateOnScreen('materials/noise_input_on.png'))
            except Exception as e:
                noise_loc_x, noise_loc_y = pag.center(
                    pag.locateOnScreen('materials/noise_input_off.png'))
                print("Found de-activated Noise button")
            self._noise_input = (noise_loc_x, noise_loc_y)

        except Exception as e:
            raise Exception("Program is not present on the screen, or try removing values from the fields")
        
        left, top, width, height = pag.locateOnScreen('materials/matlab_logo.png')
        self.main_window = (left, top, lab_width, lab_height)
        # print(left, top, width, height)

    def __click(self, position: tuple, clicks: int=1):
        pag.click(position[0], position[1], clicks)

    def select_radiopulse(self):
        self.__click(self._radiopulse)
    
    def select_videopulse(self):
        self.__click(self._videopulse)

    def select_lfm(self):
        self.__click(self._lfm)

    def select_barker(self):
        self.__click(self._barker)

    def build(self):
        self.__click(self._build_btn)
        time.sleep(2)

    def clean(self):
        self.__click(self._clean_btn)

    def set_duration(self, duration: int):
        self.__click(self._dur_input, 2)
        pag.write(str(duration))
    
    def set_amplitude(self, amplitude: int):
        self.__click(self._amp_input, 2)
        pag.write(str(amplitude))
    
    def set_frequency(self, frequency: int):
        self.__click(self._freq_input, 2)
        pag.write(str(frequency))
    
    def set_deviation(self, deviation: int):
        self.__click(self._dev_input, 2)
        pag.write(str(deviation))
    
    def filter_on(self):
        try:
            res = pag.center(pag.locateOnScreen('materials/fill_on.png'))
        except Exception:
            res=None

        if res is None:
            print("Filter is off, clicking")
            self.__click(self._filter)
            print("Filter is on")
        else:
            print("Filter is on")
    
    def filter_off(self):
        try:
            res = pag.center(pag.locateOnScreen('materials/fill_off.png'))
        except Exception:
            res=None

        if res is None:
            print("Filter is on, clicking")
            self.__click(self._filter)
            print("Filter is off")
        else:
            print("Filter is off")
    
    def noise_on(self):
        try:
            res = pag.center(pag.locateOnScreen('materials/noise_on.png'))
        except Exception:
            res=None

        if res is None:
            print("Noise is off, clicking")
            self.__click(self._noise)
            print("Noise is on")
        else:
            print("Noise is on")
    
    def noise_off(self):
        try:
            res = pag.center(pag.locateOnScreen('materials/noise_off.png'))
        except Exception:
            res=None

        if res is None:
            print("Noise is on, clicking")
            self.__click(self._noise)
            print("Noise is off")
        else:
            print("Noise is off")
    
    def set_noise(self, noise: float):
        self.__click(self._noise_input, 2)
        pag.write(str(noise))

    def save_screenshot(self, path: str):
        im = pag.screenshot(region=self.main_window)
        im.save(path)

if __name__ == "__main__":
    lab = LabAutomator()
    lab.noise_off()