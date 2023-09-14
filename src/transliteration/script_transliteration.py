from transliterate import translit


def script_to_translit(city: str) -> str:
    """Преобразует город в нужный формат"""
    return translit(city.lower(), 'ru', reversed=True).replace('\'', '')
