"""音楽再生を管理するモジュール"""
import pygame
from typing import Optional
from .constants import Music


class Mixer:
    """音楽再生を管理するクラス"""

    def __init__(self):
        """pygameのmixerを初期化"""
        pygame.mixer.init()
        self._current_music: Optional[Music] = None

    def play(self, music: Music) -> None:
        """音楽を再生

        Args:
            music: 再生する音楽データ
        """
        if self._current_music == music:
            if pygame.mixer.music.get_busy():
                # 同じ曲が再生中の場合は何もしない
                return
            elif pygame.mixer.music.get_pos() > 0:
                # 一時停止中の場合は再開
                pygame.mixer.music.unpause()
                return

        # 新しい曲の再生
        pygame.mixer.music.load(str(music.path))
        pygame.mixer.music.play(-1 if music.loop else 0)
        self._current_music = music

    def stop(self) -> None:
        """現在再生中の音楽を停止"""
        pygame.mixer.music.stop()
        self._current_music = None

    def pause(self) -> None:
        """現在再生中の音楽を一時停止"""
        pygame.mixer.music.pause()

    def unpause(self) -> None:
        """一時停止中の音楽を再開"""
        pygame.mixer.music.unpause()

    def set_volume(self, volume: float) -> None:
        """音量を設定

        Args:
            volume: 0.0から1.0の間の値
        """
        pygame.mixer.music.set_volume(max(0.0, min(1.0, volume)))
