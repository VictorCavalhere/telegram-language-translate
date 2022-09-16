import translators
import json

def translate(message):
    """_summary_

    _extended_summary_

    Args:
        payload (_type_): _description_

    Returns:
        _type_: _description_
    """


    return translators.google(to_language='en',query_text=message)