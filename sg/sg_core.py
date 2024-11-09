import numpy as np
import math
from enum import Enum, Flag, auto
from typing import Tuple
from abc import ABCMeta, abstractmethod

# Waveform class
class Waveform(metaclass = ABCMeta):
    # constractor
    def __init__(self, fs:float):
        self.fs:float = fs

    # 信号の追加
    @abstractmethod
    def add_signal(self, signal:np.ndarray[np.complex128]) -> np.ndarray[np.complex128]:
        raise NotImplemented()

# CW class
class CW(Waveform):
    # constractor
    def __init__(self, fs:float, ampl:float, freq:float, initial_phase:float):
        super().__init__(fs=fs)
        self.ampl = ampl
        self.freq = freq
        self.initial_phase = initial_phase

    # 信号の追加
    def add_signal(self, src:np.ndarray[np.complex128]) -> np.ndarray[np.complex128]:
        i = np.arange(len(src))
        return src + self.ampl * np.exp(1j * (2.0*math.pi*self.freq*i/self.fs + self.initial_phase))

class SG():
    # constractor
    def __init__(self):
        pass

    def generate(self, output_file_name:str, length:int, waveforms:list[Waveform]) -> None:
        waveform:np.ndarray[np.complex128] = np.zeros(length)
        for w in waveforms:
            waveform = w.add_signal(waveform)
        save_complex_csv(output_file_name, waveform)

# Complex csvデータ保存
def save_complex_csv(file_name:str, data:np.ndarray[np.complex128]) -> None:
    # 実部と虚部を分離
    real_part = np.real(data)
    imag_part = np.imag(data)
    # 実部と虚部を結合
    merged_data = np.column_stack((real_part, imag_part))
    # csvファイルに保存
    np.savetxt(file_name, merged_data, delimiter=",")