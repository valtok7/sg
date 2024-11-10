import numpy as np
import math
from enum import Enum, auto
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

# File Type
class FileType(Enum):
    CSV = auto()
    BIN = auto()    # 16bit float, IQ順 

class SG():
    # constractor
    def __init__(self):
        pass

    def generate(self, output_file_name:str, output_file_type:FileType, length:int, waveforms:list[Waveform]) -> None:
        waveform:np.ndarray[np.complex128] = np.zeros(length)
        for w in waveforms:
            waveform = w.add_signal(waveform)
        match output_file_type:
            case FileType.CSV:
                save_complex_csv(output_file_name, waveform)
            case FileType.BIN:
                save_complex_binary(output_file_name, waveform)
            case _:
                raise ValueError(f"Unsupported file type: {output_file_type}")           

# Complex csvデータ保存
def save_complex_csv(file_name:str, data:np.ndarray[np.complex128]) -> None:
    # 実部と虚部を分離
    real_part = np.real(data)
    imag_part = np.imag(data)
    # 実部と虚部を結合
    merged_data = np.column_stack((real_part, imag_part))
    # csvファイルに保存
    np.savetxt(file_name, merged_data, delimiter=",")

# Complex float binaryデータ保存
def save_complex_binary(file_name:str, data:np.ndarray[np.complex128]) -> None:
    # 実部と虚部を分離
    real_part = np.real(data).astype(np.float32)
    imag_part = np.imag(data).astype(np.float32)
    # I,Q順に結合
    merged_data = np.ravel(np.column_stack((real_part, imag_part)))
    # バイナリファイルに保存
    merged_data.tofile(file_name)
