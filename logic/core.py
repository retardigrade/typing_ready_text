from re import sub


allowed_pattern_types = ['plain_text', 'regexp']
allowed_languages = ['ru', 'en', 'all']


class Rule:
    def __init__(self, description, old_text, new_text, pattern_type: str):
        self.description = description
        self.old_text = old_text
        self.new_text = new_text
        if pattern_type in allowed_pattern_types:
            self.pattern_type = pattern_type
        else:
            raise TypeError('unexpected value of pattern_type')

    def __repr__(self):
        return f'{self.old_text} -> {self.new_text}'

    def __str__(self):
        return f'{self.old_text} -> {self.new_text}'

    def apply_to(self, text):
        if self.pattern_type == 'plain_text':
            return text.replace(self.old_text, self.new_text)
        elif self.pattern_type == 'regexp':
            return sub(pattern=self.old_text, repl=self.new_text, string=text)


class RuleSet:
    def __init__(self, description, language, rules):
        self.description = description
        if language in allowed_languages:
            self.language = language
        else:
            raise TypeError('unexpected value of language')
        self.rules = rules

    def __repr__(self):
        return f'Set "{self.description}" for "{self.language}"'

    def __str__(self):
        return f'Set "{self.description}" for "{self.language}"'

    def apply_to(self, text):
        updated_text = text
        for rule in self.rules:
            updated_text = rule.apply_to(updated_text)
        return updated_text
