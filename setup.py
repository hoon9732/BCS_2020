from cx_Freeze import setup, Executable
import os
import sys

includefiles = [('sfx\beep.wav', 'beep.wav'),
('sfx\death.wav', 'death.wav'),
('sfx\gameover.wav', 'gameoverwav'),
('sfx\jump.wav', 'jump.wav'),
('sfx\powerup.wav', 'powerup.wav'),
('sfx\start.wav', 'start.wav'),
('vfx\block_boost.png', 'block_boost.png'),
('vfx\block_heal.png', 'block_heal.png'),
('vfx\block_moving.png', 'block_moving.png'),
('vfx\block_mud.png', 'block_mud.png'),
('vfx\block_normal.png', 'block_normal.png'),
('vfx\count_00.png', 'count_00.png'),
('vfx\count_01.png', 'count_01.png'),
('vfx\count_02.png', 'count_02.png'),
('vfx\count_03.png', 'count_03.png'),
('vfx\covid.png', 'covid.png'),
('vfx\falling_01.png', 'falling_01.png'),
('vfx\falling_02.png', 'falling_02.png'),
('vfx\falling_03.png', 'falling_03.png'),
('vfx\instruction_01.png', 'instruction_01.png'),
('vfx\instruction_02.png', 'instruction_02.png'),
('vfx\instruction_03.png', 'instruction_03.png'),
('vfx\instruction_04.png', 'instruction_04.png'),
('vfx\logo_01.png', 'logo_01.png'),
('vfx\logo_02.png', 'logo_02.png'),
('vfx\main_00.png', 'main_00.png'),
('vfx\main_01.png', 'main_01.png'),
('vfx\main_02.png', 'main_02.png'),
('vfx\main_03.png', 'main_03.png'),
('vfx\main_04.png', 'main_04.png'),
('vfx\main_05.png', 'main_05.png'),
('vfx\mask_01.png', 'mask_01.png'),
('vfx\mask_02.png', 'mask_02.png'),
('vfx\mask_03.png', 'mask_03.png'),
('vfx\standing_01.png', 'standing_01.png'),
('vfx\standing_02.png', 'standing_02.png'),
('vfx\standing_03.png', 'standing_03.png'),
('vfx\standing_04.png', 'standing_04.png'),
('vfx\standing_05.png', 'standing_05.png'),
('vfx\start_01.png', 'start_01.png'),
('vfx\start_02.png', 'start_02.png'),
('vfx\title_01.png', 'title_01.png'),
('vfx\title_02.png', 'title_02.png'),
'settings.py', 'sound.py', 'sprites.py'
]

buildOptions = dict(packages=['pygame', 'os', 'math', 'random', 'datetime'], excludes = ['tkinter', 'numpy'])

base = 'Win64GUI' if sys.platform=='win64' else None
exe = [Executable("main.py", base=base)]

setup(
    name='2020',
    version = '0.1',
    author = '2018-17738',
    description = 'Final Project',
    options = dict(build_exe = buildOptions),
    executables = exe
)