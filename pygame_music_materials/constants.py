"""音楽データの定義"""
from dataclasses import dataclass
from pathlib import Path

MUSIC_DIR = Path(__file__).parent / "musics"


@dataclass(frozen=True)
class Music:
    """音楽データを表すクラス"""
    id: str
    filename: str
    title: str
    loop: bool

    @property
    def path(self) -> Path:
        """音楽ファイルの絶対パスを返す"""
        return MUSIC_DIR / self.filename


# 音楽データの定義
night = Music(
    id="night",
    filename="shinmiri.wav",
    title="静かな夜",
    loop=True
)

boss_battle = Music(
    id="boss_battle",
    filename="boss.wav",
    title="最終決戦",
    loop=True
)

lava = Music(
    id="lava",
    filename="yougan.wav",
    title="溶岩の洞窟",
    loop=True
)

stage_clear = Music(
    id="stage_clear",
    filename="clear.wav",
    title="クリア！",
    loop=False
)

field = Music(
    id="field",
    filename="sougen.wav",
    title="草原のテーマ",
    loop=True
)

# 全ての音楽データをリストとして保持
ALL_MUSIC = [night, boss_battle, lava, stage_clear, field]
