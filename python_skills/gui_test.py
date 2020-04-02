import PySimpleGUI as sg
'''
class GUI(object):
    @property
    def create_gui(self):
        sg.theme('DarkAmber')	# Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('模拟退火')],
                    [sg.Text('起始温度:'), sg.InputText()],
                    [sg.Text('终止温度:'),sg.InputText()],
                    [sg.Button('Ok'), sg.Button('Cancel')] ]

        # Create the Window
        window = sg.Window('模拟退火程序', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event in (None, 'Cancel'):	# if user closes window or clicks cancel
                break
            print('You entered ', int(values[0])+int(values[1]))

        window.close()
dis=GUI()
dis.create_gui
'''
