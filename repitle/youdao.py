import urllib.request
import urllib.parse,json
import PySimpleGUI as sg


def repitle(values):
    str_values=values['value']
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = '%s'%str_values
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15858226063868'
    data['sign'] = '415dbc6073e29500e6fc52a9de26f18e'
    data['ts'] = '1585822606386'
    data['bv'] = '70244e0061db49a9ee62d341c5fed82a'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    aim = target['translateResult'][0][0]['tgt']
    return aim


sg.theme('LightGrey3')
layout = [[sg.Text('有道翻译')],
            [sg.Text('输入需要翻译的内容:'),sg.InputText(key='value')],
            [sg.Button('翻译'),sg.Output(key='out')],
            [sg.Button('关闭')]
            ]
window = sg.Window('有道翻译',layout)

while True:
    event,values = window.read()
    if event in (None,'关闭'):
        break
    if event == '翻译':
        if values['value'] != None:
            out_values = repitle(values)
        else:
            out_values = '请输入需要翻译内容！'
        window['out'].update(out_values)
window.close()

