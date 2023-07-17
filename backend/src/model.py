import spacy


class SpacyModel(object):
    smallModel = None
    mediumModel = None

    @classmethod
    def get_small_model(cls):
        """Get the small spacy model object for this instance,
        loading it if it's not already loaded."""
        if cls.smallModel is None:
            cls.smallModel = spacy.load("en_core_web_sm")
        return cls.smallModel

    @classmethod
    def get_medium_model(cls):
        """Get the mediuem spacy model object for this instance,
        loading it if it's not already loaded."""
        if cls.mediumModel is None:
            cls.mediumModel = spacy.load("en_core_web_md")
        return cls.mediumModel
