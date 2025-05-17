#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: MultiplexaPAM
# Author: labcom
# GNU Radio version: v3.10.11.0-89-ga17f69e7

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
import logging as log

def get_state_directory() -> str:
    oldpath = os.path.expanduser("~/.grc_gnuradio")
    try:
        from gnuradio.gr import paths
        newpath = paths.persistent()
        if os.path.exists(newpath):
            return newpath
        if os.path.exists(oldpath):
            log.warning(f"Found persistent state path '{newpath}', but file does not exist. " +
                     f"Old default persistent state path '{oldpath}' exists; using that. " +
                     "Please consider moving state to new location.")
            return oldpath
        # Default to the correct path if both are configured.
        # neither old, nor new path exist: create new path, return that
        os.makedirs(newpath, exist_ok=True)
        return newpath
    except (ImportError, NameError):
        log.warning("Could not retrieve GNU Radio persistent state directory from GNU Radio. " +
                 "Trying defaults.")
        xdgstate = os.getenv("XDG_STATE_HOME", os.path.expanduser("~/.local/state"))
        xdgcand = os.path.join(xdgstate, "gnuradio")
        if os.path.exists(xdgcand):
            return xdgcand
        if os.path.exists(oldpath):
            log.warning(f"Using legacy state path '{oldpath}'. Please consider moving state " +
                     f"files to '{xdgcand}'.")
            return oldpath
        # neither old, nor new path exist: create new path, return that
        os.makedirs(xdgcand, exist_ok=True)
        return xdgcand

sys.path.append(os.environ.get('GRC_HIER_PATH', get_state_directory()))

from ModuladorPulsos import ModuladorPulsos  # grc-generated hier_block
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
import sip
import threading



class MultiplexaPAM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MultiplexaPAM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MultiplexaPAM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "MultiplexaPAM")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 25e6/128
        self.fs = fs = samp_rate/100
        self.fm = fm = 100
        self.fc_LPF = fc_LPF = 100
        self.W = W = 25
        self.D4 = D4 = 0
        self.D3 = D3 = 75
        self.D2 = D2 = 50
        self.D1 = D1 = 25
        self.D = D = 25
        self.Am = Am = 1

        ##################################################
        # Blocks
        ##################################################

        self._fs_range = qtgui.Range(0, 100e3, 1, samp_rate/100, 200)
        self._fs_win = qtgui.RangeWidget(self._fs_range, self.set_fs, "Frecuencia pulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fs_win)
        self._fm_range = qtgui.Range(0, 10e3, 10, 100, 200)
        self._fm_win = qtgui.RangeWidget(self._fm_range, self.set_fm, "frecuencia mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self._fc_LPF_range = qtgui.Range(0, 10e3, 1, 100, 200)
        self._fc_LPF_win = qtgui.RangeWidget(self._fc_LPF_range, self.set_fc_LPF, "frecuencia filtro", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_LPF_win)
        self._W_range = qtgui.Range(0, 50, 1, 25, 200)
        self._W_win = qtgui.RangeWidget(self._W_range, self.set_W, "ancho de pulso selector", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._W_win)
        self._D4_range = qtgui.Range(0, 100, 1, 0, 200)
        self._D4_win = qtgui.RangeWidget(self._D4_range, self.set_D4, "Selector ", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D4_win)
        self._D3_range = qtgui.Range(0, 100, 1, 75, 200)
        self._D3_win = qtgui.RangeWidget(self._D3_range, self.set_D3, "retardo 3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D3_win)
        self._D2_range = qtgui.Range(0, 100, 1, 50, 200)
        self._D2_win = qtgui.RangeWidget(self._D2_range, self.set_D2, "retardo 2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D2_win)
        self._D1_range = qtgui.Range(0, 100, 1, 25, 200)
        self._D1_win = qtgui.RangeWidget(self._D1_range, self.set_D1, "retardo 1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D1_win)
        self._D_range = qtgui.Range(0, 50, 1, 25, 200)
        self._D_win = qtgui.RangeWidget(self._D_range, self.set_D, "Ancho Pulso", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_win)
        self._Am_range = qtgui.Range(0, 10, 100e-3, 1, 200)
        self._Am_win = qtgui.RangeWidget(self._Am_range, self.set_Am, "Amplitud del mesanaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_sink_0.set_center_freq(200e6, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(10, 0)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            (1024*8), #size
            samp_rate, #samp_rate
            "", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            (1024*4), #size
            samp_rate, #samp_rate
            "", #name
            5, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_RECTANGULAR, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.filter_fft_low_pass_filter_0 = filter.fft_filter_fff(1, firdes.low_pass(4, samp_rate, fc_LPF, 100, window.WIN_HAMMING, 6.76), 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/com1_E1C_G1/GNURADIO_LABCOMUIS_2025_1_E1C_G1/practica5/Parte A/file_example_WAV_1MG.wav', True)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, D3)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, D4)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, D2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, D1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fm, Am, 0, 0)
        self.ModuladorPulsos_0_2_0 = ModuladorPulsos(
            D=W,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPulsos_0_2 = ModuladorPulsos(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPulsos_0_1 = ModuladorPulsos(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPulsos_0_0 = ModuladorPulsos(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModuladorPulsos_0 = ModuladorPulsos(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModuladorPulsos_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.ModuladorPulsos_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ModuladorPulsos_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.ModuladorPulsos_0_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.ModuladorPulsos_0_2, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.ModuladorPulsos_0_2_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.ModuladorPulsos_0_2_0, 0), (self.filter_fft_low_pass_filter_0, 0))
        self.connect((self.ModuladorPulsos_0_2_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.ModuladorPulsos_0_2_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModuladorPulsos_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.ModuladorPulsos_0_1, 0))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.ModuladorPulsos_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0_0_0, 0), (self.ModuladorPulsos_0_2_0, 0))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.ModuladorPulsos_0, 0))
        self.connect((self.filter_fft_low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.filter_fft_low_pass_filter_0, 0), (self.qtgui_time_sink_x_1, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "MultiplexaPAM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_fs(self.samp_rate/100)
        self.ModuladorPulsos_0.set_samp_rate(self.samp_rate)
        self.ModuladorPulsos_0_0.set_samp_rate(self.samp_rate)
        self.ModuladorPulsos_0_1.set_samp_rate(self.samp_rate)
        self.ModuladorPulsos_0_2.set_samp_rate(self.samp_rate)
        self.ModuladorPulsos_0_2_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.filter_fft_low_pass_filter_0.set_taps(firdes.low_pass(4, self.samp_rate, self.fc_LPF, 100, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.ModuladorPulsos_0.set_fs(self.fs)
        self.ModuladorPulsos_0_0.set_fs(self.fs)
        self.ModuladorPulsos_0_1.set_fs(self.fs)
        self.ModuladorPulsos_0_2.set_fs(self.fs)
        self.ModuladorPulsos_0_2_0.set_fs(self.fs)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_1.set_frequency(self.fm)
        self.analog_sig_source_x_0_2.set_frequency(self.fm)

    def get_fc_LPF(self):
        return self.fc_LPF

    def set_fc_LPF(self, fc_LPF):
        self.fc_LPF = fc_LPF
        self.filter_fft_low_pass_filter_0.set_taps(firdes.low_pass(4, self.samp_rate, self.fc_LPF, 100, window.WIN_HAMMING, 6.76))

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W
        self.ModuladorPulsos_0_2_0.set_D(self.W)

    def get_D4(self):
        return self.D4

    def set_D4(self, D4):
        self.D4 = D4
        self.blocks_delay_0_0_0.set_dly(int(self.D4))

    def get_D3(self):
        return self.D3

    def set_D3(self, D3):
        self.D3 = D3
        self.blocks_delay_0_1.set_dly(int(self.D3))

    def get_D2(self):
        return self.D2

    def set_D2(self, D2):
        self.D2 = D2
        self.blocks_delay_0_0.set_dly(int(self.D2))

    def get_D1(self):
        return self.D1

    def set_D1(self, D1):
        self.D1 = D1
        self.blocks_delay_0.set_dly(int(self.D1))

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.ModuladorPulsos_0.set_D(self.D)
        self.ModuladorPulsos_0_0.set_D(self.D)
        self.ModuladorPulsos_0_1.set_D(self.D)
        self.ModuladorPulsos_0_2.set_D(self.D)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.analog_sig_source_x_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_1.set_amplitude(self.Am)
        self.analog_sig_source_x_0_2.set_amplitude(self.Am)




def main(top_block_cls=MultiplexaPAM, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
