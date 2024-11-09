from starting import Start

class Helper(Start):

    def generate_prompt(self, prompt_num: int, theme_id: int, complience_level_id: int):
        template_of_prompt = self.prompts[prompt_num]
        return (
            template_of_prompt
            .replace("{TEXT_THEME}", self.themes[theme_id])
            .replace("{COMLIANCE_LEVEL}", self.colmpliance_levels[complience_level_id])
        )
    
    def start_prompt(self):
        return self.generate_prompt(1, 1, 1)
