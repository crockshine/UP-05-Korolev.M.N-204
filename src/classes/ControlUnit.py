from PySide6.QtGui import QIcon


class ControlUnit:
    def __init__(self, audio_player, main):
        super().__init__()
        self.audio_player = audio_player
        self.main = main
        self.settings = audio_player.settings
        
        self.main.play_pause_btn.clicked.connect(self.handle_play_pause)
        self.main.play_pause_btn.setIcon(QIcon(":/icons/icons/pause.svg"))
        
        self.main.nextButton.clicked.connect(self.handle_next)
        self.main.prevButton.clicked.connect(self.handle_prev)

        self.main.cycleButton.clicked.connect(self.handle_cycle)
        self.main.cycleButton.setIcon(QIcon(":icons/icons/no-cycle.svg"))


    def handle_cycle(self):
        loop = self.settings.get('loop')

        if loop is None:
            self.settings['loop'] = 'playlist'
            self.main.cycleButton.setIcon(QIcon(":icons/icons/cycle.svg"))
        elif loop == 'playlist':
            self.settings['loop'] = 'self'
            self.main.cycleButton.setIcon(QIcon(":icons/icons/self-cycle.svg"))
        elif loop == 'self':
            self.settings['loop'] = None
            self.main.cycleButton.setIcon(QIcon(":icons/icons/no-cycle.svg"))


    def handle_play_pause(self):
        if self.audio_player.device.running:
            self.update_ui_play_pause_button(True)
            self.audio_player.pause()
        else:
            self.update_ui_play_pause_button(False)
            self.audio_player.play()    
            
    def handle_next(self):
        self.audio_player.next(is_auto=False)

    def handle_prev(self):
        self.audio_player.prev()


    def update_ui_play_pause_button(self, is_played: bool):
        if is_played:
            self.main.play_pause_btn.setIcon(QIcon(":/icons/icons/pause.svg"))
        else:
            self.main.play_pause_btn.setIcon(QIcon(":/icons/icons/play.svg"))


