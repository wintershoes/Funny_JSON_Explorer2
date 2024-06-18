import json
import sys
from builder import StrategyBuilder

'''
可选风格：
icon :'poker':
'default':
style :'tree':
'rectangle':
'''

if __name__ == "__main__":
    json_file = 'example.json'
    style = 'rectangle'
    icon = 'poker'

    # 从命令行参数中读取设置
    if '-f' in sys.argv:
        json_file = sys.argv[sys.argv.index('-f') + 1]
    if '-s' in sys.argv:
        style = sys.argv[sys.argv.index('-s') + 1]
    if '-i' in sys.argv:
        icon = sys.argv[sys.argv.index('-i') + 1]

    builder = StrategyBuilder(json_file, style, icon)
    builder.execute_strategy()