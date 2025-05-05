from PySide6.QtGui import QIcon


class ControlUnit:
    def __init__(self, audio_player):
        super().__init__()
        self.audio_player = audio_player

        self.audio_player.main_ui.play_pause_btn.clicked.connect(self.handle_play_pause_button)
        self.audio_player.main_ui.play_pause_btn.setIcon(QIcon(":/icons/icons/pause.svg"))

    def update_ui_play_pause_button(self, is_played: bool):
        if is_played:
            self.audio_player.main_ui.play_pause_btn.setIcon(QIcon(":/icons/icons/pause.svg"))
        else:
            self.audio_player.main_ui.play_pause_btn.setIcon(QIcon(":/icons/icons/play.svg"))

    def handle_play_pause_button(self):
        if self.audio_player.device.running:
            self.update_ui_play_pause_button(True)
            self.audio_player.pause()
        else:
            self.update_ui_play_pause_button(False)
            self.audio_player.play()

