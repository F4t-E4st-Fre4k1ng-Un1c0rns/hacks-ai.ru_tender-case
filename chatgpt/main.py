import clipboard
import chime  # sounds to know status of generating

from helper import Helper
from screen import Screen

helper = Helper()
clipboard.copy(helper.start_prompt())
screen = Screen()



for theme_id, complience_level_id in helper.queue:
    filename = f"{theme_id}_{complience_level_id}.txt"

    screen.create_new_chat()

    prompt = helper.generate_prompt(1, theme_id, complience_level_id)
    screen.start_prompt(prompt)
    uc_response = screen.copy_response()
    print("catch - 1 - uc")
    

    prompt = helper.generate_prompt(2, theme_id, complience_level_id)
    screen.continue_prompt(prompt)
    __skip = screen.copy_response()
    print("catch - 2 - skip")

    prompt = helper.generate_prompt(3, theme_id, complience_level_id)
    screen.continue_prompt(prompt)
    ssts_response = screen.copy_response()
    print("catch - 3 - ssts")

    prompt = helper.generate_prompt(4, theme_id, complience_level_id)
    screen.continue_prompt(prompt)
    table_response = screen.copy_response()
    print("catch - 4 - table")


    # check to correct

    with open(f"data/uc/{filename}", "w") as F:
        F.write(uc_response)
    
    with open(f"data/ssts/{filename}", "w") as F:
        F.write(ssts_response)
    
    with open(f"data/table/{filename}", "w") as F:
        F.write(table_response)


