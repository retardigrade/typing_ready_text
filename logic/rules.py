from logic.core import Rule, RuleSet
from logic.tools import replace_all_romans

r__end_dot = Rule('Space after sentence end', '\.(?=[А-Я]{1})', '. ', 'regexp')
r__current_era = Rule('No spaces in "н.э."', 'н. э.', 'н.э.', 'plain_text')
r__ascii_quotes = Rule('ascii quotes', '(«|»)', '"', 'regexp')

r__open_bracket = Rule('No space after opening brackets', '( ', '(', 'plain_text')
r__close_bracket = Rule('No space after closing brackets', ' )', ')', 'plain_text')
rs__brackets = RuleSet('No redundant spaces inside brackets', 'all',  [r__open_bracket, r__close_bracket])

ru_typing_set = RuleSet('Default ru set for typing', 'ru',
                        [r__end_dot, r__current_era, r__ascii_quotes, rs__brackets])

transformers = [replace_all_romans]


def fix_text(text, ruleset=ru_typing_set):
    new_text = ruleset.apply_to(text)
    for transformer_func in transformers:
        new_text = transformer_func(new_text)
    return new_text


def rules_list(ruleset=ru_typing_set):
    return '\n'.join([rule.description + ' | ' + str(rule) for rule in ruleset.rules])
