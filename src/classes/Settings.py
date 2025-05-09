class Settings:
    def __init__(self):
        super().__init__()

        self.settings = {
            'loop': None, # None | 'playlist' | 'self'
            'random': False,
        }