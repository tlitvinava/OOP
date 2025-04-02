class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            cls.theme = "light"
            cls.font_size = 12
        return cls._instance