import os

class Start:
    def __init__(self):
        self.themes = self.get_themes()
        self.colmpliance_levels = self.get_colmpliance_levels()
        self.prompts = {
            id: self.get_prompt(id)
            for id in range(1, 4+1)
        }

        self.queue = self.generate_queue()

    def get_themes(self):
        res = dict()
        with open("prompt_data/themes.txt") as F:
            for i in F.read().split("\n"):
                id, theme = i.split(".")
                res[int(id)] = theme
        return res


    def get_colmpliance_levels(self):
        res = dict()
        with open("prompt_data/colmpliance_levels.txt") as F:
            for i in F.read().split("\n"):
                id, colmpliance_level = i.split(".")
                res[int(id)] = colmpliance_level
        return res
        
    def get_prompt(self, prompt_num: int) -> str:
        with open(f"prompt_data/prompt/{prompt_num}.txt", encoding="utf-8") as F:
            prompt = F.read()
            return prompt

    def generate_queue(self):
        queue = set()
        for theme_id in self.themes.keys():
            for complience_level_id in self.colmpliance_levels.keys():
                queue.add((theme_id, complience_level_id))

        ready_items = set()

        for name in os.listdir("data/uc"):
            theme_id, complience_level_id = name.replace(".txt", "").split("_")
            ready_items.add((int(theme_id), int(complience_level_id)))

        return sorted(queue - ready_items)