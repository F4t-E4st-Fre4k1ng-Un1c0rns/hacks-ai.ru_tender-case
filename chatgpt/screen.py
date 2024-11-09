import time
from pynput import mouse
import pyautogui
import clipboard

class Screen:
    def __init__(self):
        self.current_handler = 0
        self.new_chat_position = (0, 0)
        self.start_prompt_position = (0, 0)
        self.copy_result_position = (0, 0)
        self.continue_prompt_position = (0, 0)

        listener = mouse.Listener(on_click=self.click_handler)
        listener.start()
        while True:
            time.sleep(0.1)
            if self.current_handler > 4:
                listener.stop()
                print(
                    self.start_prompt_position,
                    self.copy_result_position,
                    self.continue_prompt_position,
                    self.new_chat_position,
                    "\n",
                    "screen is ready"
                )
                return


    def click_handler(self, position1, position2, button, is_pressed):
        if is_pressed:
            self.current_handler += 1
            print(position1, position2, button, is_pressed)
            match self.current_handler:
                case 1:
                    self.new_chat_position = (position1, position2)
                case 2:
                    self.start_prompt_position = (position1, position2)
                case 3:
                    self.copy_result_position = (position1, position2)
                case 4:
                    self.continue_prompt_position = (position1, position2)
                    self.current_handler += 1
                case _:
                    return
                
    def create_new_chat(self):
        pyautogui.click(self.new_chat_position)
        time.sleep(1)
    
    def start_prompt(self, prompt: str):
        pyautogui.click(self.start_prompt_position)
        clipboard.copy(prompt)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("enter")
        time.sleep(1)

    def continue_prompt(self, prompt: str):
        pyautogui.click(self.continue_prompt_position)
        clipboard.copy(prompt)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey("enter")
        time.sleep(1)
    
    def copy_response(self) -> str:
        clipboard.copy("")
        while True:
            time.sleep(0.1)
            pyautogui.scroll(-1000)
            pyautogui.click(self.copy_result_position)
            pyautogui.moveTo(
                self.copy_result_position[0]+20,
                self.copy_result_position[1]+60,
                0.2
            )
            paste = clipboard.paste()
            if paste != "":
                time.sleep(0.5)
                return paste
            