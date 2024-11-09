#!/usr/bin/env python
import sg_core
import sg_gui
import wx
import fire

def main(cui:bool=False):
    if cui == True:
        # CUI
        # CWを2つ作成
        cw1 = sg_core.CW(fs=1.0, ampl=1.0, freq=0.1, initial_phase=0.0)
        cw2 = sg_core.CW(fs=1.0, ampl=0.5, freq=0.2, initial_phase=0.0)
        
        # 信号長1024で生成
        sg = sg_core.SG()
        sg.generate(output_file_name='waveform.csv', length=1024, waveforms=[cw1, cw2])
        return
    
    else:
        # GUI
        app = wx.App(False)
        frame = sg_gui.GUI(None)
        frame.Show(True)
        app.MainLoop()

if __name__ == "__main__":
    fire.Fire(main)