#!/usr/bin/env python
import sg_core
import sg_gui
import wx
import fire

def main(cui:bool=False, fs:float=1.0, length:int=1024, ampl:float=1.0, freq:float=0.1, initial_phase:float=0.0):
    if cui == True:
        # CUI
        cw = sg_core.CW(fs=fs, ampl=ampl, freq=freq, initial_phase=initial_phase)
        
        # 信号生成
        sg = sg_core.SG()
        sg.generate(output_file_name='waveform.csv', length=length, waveforms=[cw])
        return
    
    else:
        # GUI
        app = wx.App(False)
        frame = sg_gui.GUI(None)
        frame.Show(True)
        app.MainLoop()

if __name__ == "__main__":
    fire.Fire(main)