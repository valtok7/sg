import wx
import json
import sg_core
from sg_gui_builderMyFrame1 import sg_gui_builderMyFrame1

class GUI( sg_gui_builderMyFrame1 ):
    def __init__( self, parent ):
        sg_gui_builderMyFrame1.__init__( self, parent )
        self.waveforms:list[sg_core.Waveform] = []
        self.sg = sg_core.SG()
        self.config_file = 'sg_config.json'
        self.load_parameters()

    def load_parameters(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.m_fs.SetValue(str(config.get('fs', '1.0')))
                self.m_length.SetValue(str(config.get('length', '1024')))
                self.m_cwFreq.SetValue(str(config.get('cw_freq', '0.1'))) 
                self.m_cwAmpl.SetValue(str(config.get('cw_ampl', '1.0')))
                self.m_cwInitPhase.SetValue(str(config.get('cw_init_phase', '0.0')))
                self.m_outputFileType.SetSelection(int(config.get('output_file_type', '0')))
        except FileNotFoundError:
            pass # 初回起動時はデフォルト値を使用

    def save_parameters(self):
        config = {
            'fs': self.m_fs.GetValue(),
            'length': self.m_length.GetValue(),
            'cw_freq': self.m_cwFreq.GetValue(),
            'cw_ampl': self.m_cwAmpl.GetValue(), 
            'cw_init_phase': self.m_cwInitPhase.GetValue(),
            'output_file_type': self.m_outputFileType.GetSelection()
        }
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)

    # Handlers for MyFrame1 events.
    def OnClose( self, event ):
        self.save_parameters()
        event.Skip()  # イベントを伝播させて、ウィンドウを実際に閉じる
        
    def OnButtonClickAddCW( self, event ):
        fs = float(self.m_fs.GetValue())
        freq = float(self.m_cwFreq.GetValue())
        ampl = float(self.m_cwAmpl.GetValue())
        initial_phase = float(self.m_cwInitPhase.GetValue())
        cw = sg_core.CW(fs=fs, ampl=ampl, freq=freq, initial_phase=initial_phase)
        self.waveforms.append(cw)
        append_str = f"CW, frequency={freq}, amplitude={ampl}, initial phase={initial_phase}\n"
        current_list_str = self.m_waveformList.GetValue()
        self.m_waveformList.SetValue(f"{current_list_str}{append_str}")

    def OnButtonClickGenerate( self, event ):
        length = int(self.m_length.GetValue())
        output_file_type = sg_core.FileType.CSV if self.m_outputFileType.GetSelection() == 0 else sg_core.FileType.BIN
        extension = "csv" if output_file_type == sg_core.FileType.CSV else "bin"
        dialog = wx.FileDialog(None, "Select output file", wildcard=f"*.{extension}", style=wx.FD_SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            output_file_name:str = dialog.GetPath()
            self.sg.generate(output_file_name=output_file_name, output_file_type=output_file_type, length=length, waveforms=self.waveforms)
            dialog = wx.MessageDialog(None, "Completed", "Info", wx.OK)
            dialog.ShowModal()
            dialog.Destroy()

    def OnButtonClickClearList( self, event ):
        self.waveforms.clear()
        self.m_waveformList.SetValue("")
