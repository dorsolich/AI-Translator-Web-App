import deepl
from app import app


class Translate:
    def __init__(self, authorization_key = app.config['DEEPL_SECRET_KEY']) -> None:
        self.translator = deepl.Translator(authorization_key)

    def transform(self, target_language, text):
        self.translated_text = self.translator.translate_text(text, target_lang=target_language)
        self.original_language = self.translated_text.detected_source_lang
        self.original_text = text
        self.target_language = target_language
        return self