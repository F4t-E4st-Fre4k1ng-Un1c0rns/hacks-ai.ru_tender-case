from random import randint

import time
from pynput import mouse
import pyautogui
import clipboard

import chime


class Screen:
    def __init__(self):
        self.new_chat_position = (346, 170)
        self.start_prompt_position = (750, 565)
        self.copy_result_position = (713, 780)
        self.continue_prompt_position = (813, 952)


        # self.current_handler = 0
        # listener = mouse.Listener(on_click=self.click_handler)
        # listener.start()
        # while True:
        #     time.sleep(0.1)
        #     if self.current_handler > 4:
        #         listener.stop()
        #         return


    def click_handler(self, position1, position2, button, is_pressed):
        if is_pressed:
            self.current_handler += 1
            match self.current_handler:
                case 1:
                    print(f"self.new_chat_position = ({position1}, {position2})")
                    self.new_chat_position = (position1, position2)
                case 2:
                    print(f"self.start_prompt_position = ({position1}, {position2})")
                    self.start_prompt_position = (position1, position2)
                case 3:
                    print(f"self.copy_result_position = ({position1}, {position2})")
                    self.copy_result_position = (position1, position2)
                case 4:
                    print(f"self.continue_prompt_position = ({position1}, {position2})")
                    self.continue_prompt_position = (position1, position2)
                    self.current_handler += 1
                case _:
                    return
                
    def create_new_chat(self):
        pyautogui.click(*self.new_chat_position, duration=randint(1, 3))
        time.sleep(1)
    
    def start_prompt(self, prompt: str):
        pyautogui.click(*self.start_prompt_position, duration=randint(1, 3))
        clipboard.copy(prompt)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("enter")
        time.sleep(1)

    def continue_prompt(self, prompt: str):
        pyautogui.click(*self.continue_prompt_position, duration=randint(1, 3))
        clipboard.copy(prompt)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("enter")
        time.sleep(1)
    
    def copy_response(self) -> str:
        clipboard.copy("")
        start_time = time.time()
        

        while True:
            if 3*60 > (time.time() - start_time) > 1.5*60:
                chime.warning()
                self.sleep_random(25, 30)
            if (time.time() - start_time) > 3*60:
                chime.error()

            time.sleep(0.1)
            pyautogui.scroll(-1000)
            pyautogui.click(*self.copy_result_position, duration=0.2)

            pyautogui.click(
                self.copy_result_position[0],
                self.copy_result_position[1] - 50,
                duration=0.05)
            pyautogui.click(
                self.copy_result_position[0],
                self.copy_result_position[1] - 60,
                duration=0.05)
            pyautogui.click(
                self.copy_result_position[0],
                self.copy_result_position[1] - 70,
                duration=0.05)
            pyautogui.click(
                self.copy_result_position[0],
                self.copy_result_position[1] - 80,
                duration=0.05)

            pyautogui.moveTo(
                self.copy_result_position[0]+20,
                self.copy_result_position[1]+60,
                0.2
            )
            paste = clipboard.paste()
            if paste != "":
                time.sleep(0.5)
                return paste
            
    def sleep_random(self, st=5, en=25):
        time.sleep(randint(st, en))
    


# 24522452
# 5785