import clipboard
import keyboard
import chime  # sounds to know status of generating

from helper import Helper


def wait_gpt(prompt: str, button_wait: str):
    clipboard.copy(prompt)
    while True:
        if keyboard.is_pressed(button_wait):
            return clipboard.paste()



helper = Helper()
chime.success()

for theme_id, complience_level_id in helper.queue:
    filename = f"{theme_id}_{complience_level_id}.txt"

    prompt = helper.generate_prompt(1, theme_id, complience_level_id)
    uc_response = wait_gpt(prompt, "1")
    print("catch - 1 - uc")
    chime.info()

    prompt = helper.generate_prompt(2, theme_id, complience_level_id)
    __skip = wait_gpt(prompt, "2")
    print("catch - 2 - skip")
    chime.info()

    prompt = helper.generate_prompt(3, theme_id, complience_level_id)
    ssts_response = wait_gpt(prompt, "3")
    print("catch - 3 - ssts")
    chime.info()

    prompt = helper.generate_prompt(4, theme_id, complience_level_id)
    table_response = wait_gpt(prompt, "4")
    print("catch - 4 - table")
    chime.info()

    # check to correct

    with open(f"data/uc/{filename}", "w") as F:
        F.write(uc_response)
    
    with open(f"data/ssts/{filename}", "w") as F:
        F.write(ssts_response)
    
    with open(f"data/table/{filename}", "w") as F:
        F.write(table_response)
    chime.success()

