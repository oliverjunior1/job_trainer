import FreeSimpleGUI as sg

from pythonProject.ardit_sulce.bonus.zip_creator import make_archive
from zip_creator import *

label1 = sg.Text('Select files to compress: ')
input1 = sg.Input()
chose_button1 = sg.FileBrowse('Choose', key='files')

label2 = sg.Text('Select destination folder ')
input2 = sg.Input()
chose_button2 = sg.FolderBrowse('Choose', key='folder')

compress_button = sg.Button('Compress')
output_label = sg.Text(key='Output', text_color='green')

window = sg.Window('File Compressor',
                   layout=[[label1, input1, chose_button1],
                           [label2, input2, chose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['Choose'].split(';')
    folder = values['Choose']
    make_archive(filepaths, folder)
    window['output'].update(value='Compression completed!')


window.close()