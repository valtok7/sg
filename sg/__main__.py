#!/usr/bin/env python
import sg_core
import sg_gui
import wx
import fire
import os

def main(cui:bool=False, fs:float=1.0, length:int=1024, ampl:float=1.0, freq:float=0.1, initial_phase:float=0.0, output_file_name:str='waveform.csv', output_file_type:str='CSV'):
    if cui == True:
        # output file typeをstrからFileTypeに変換する
        output_file_type = sg_core.FileType[output_file_type]

        # 信号生成
        cw = sg_core.CW(fs=fs, ampl=ampl, freq=freq, initial_phase=initial_phase)        
        sg = sg_core.SG()
        sg.generate(output_file_name=output_file_name, output_file_type=output_file_type, length=length, waveforms=[cw])
        return
    
    else:
        # GUI
        app = wx.App(False)
        frame = sg_gui.GUI(None)
        dirname = os.path.dirname(os.path.abspath(__file__))
        icon = wx.Icon(f"{dirname}/sg.ico", wx.BITMAP_TYPE_ICO)
        frame.SetIcon(icon)
        frame.Show(True)
        app.MainLoop()

if __name__ == "__main__":
    fire.Fire(main)