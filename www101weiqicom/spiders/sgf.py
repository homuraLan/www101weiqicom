import json
import random
import string
import re
from typing import List, Dict

# class ExtractPageVariable:
#     def __init__(self, variable_name: str) -> None:
#         self._variable_name = variable_name
#         self._handshake = self._generate_handshake()
#         self._data = self._listen()

#     @property
#     def data(self) -> Dict:
#         return self._data

#     def _generate_handshake(self) -> str:
#         return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

#     def _listen(self) -> Dict:
#         # Assuming the message event is handled elsewhere in the Python environment
#         # and the resolved data is directly returned here.
#         # You may need to adapt this part based on your specific environment.
#         pass

def save_data(data: str, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)

def normalize_location(board_size: int, string: str) -> str:
    return string

def calculate_prepositions(g_qq: Dict) -> str:
    board_size = g_qq['lu']
    prepos = g_qq['prepos']
    if g_qq.get('psm') and g_qq['psm'].get('prepos'):
        prepos = g_qq['psm']['prepos']

    abs_positions = ''.join(f"[{normalize_location(board_size, p)}]" for p in prepos[0])
    aws_positions = ''.join(f"[{normalize_location(board_size, p)}]" for p in prepos[1])
    return f"AB{abs_positions}AW{aws_positions}"

def escape_comment(string: str) -> str:
    return re.sub(r'[\[\]]', r'\\\g<0>', string)

def calculate_variant(board_size: int, black_first: bool, answer: Dict) -> str:
    current_color = 'B' if black_first else 'W'
    if 'pts' not in answer:
        answer['pts'] = []
    content = ''
    for pt in answer['pts']:
        result = f";{current_color}[{normalize_location(board_size, pt['p'])}]"
        if not content:
            if answer.get('ty') == 1:
                result += "N[正解]"
            elif answer.get('ty') == 3:
                result += "N[失败]"
        if pt.get('c'):
            result += f"C[{escape_comment(pt['c'].strip())}]"
        content += result
        current_color = 'W' if current_color == 'B' else 'B'
    return f"({content})"

def calculate_variants(g_qq: Dict) -> str:
    if not g_qq.get('answers'):
        return ''
    
    filtered_answers = filter(lambda answer: answer['st'] == 2 and (answer['ty'] == 1 or answer['ty'] == 3), g_qq['answers'])
    sorted_answers = sorted(filtered_answers, key=lambda answer: answer['ty'], reverse=True)

    result = ''.join([calculate_variant(g_qq['lu'], g_qq['blackfirst'], answer) for answer in sorted_answers])
    #answers = sorted((answer for answer in g_qq['answers'] if answer.get('st') == 2 and answer.get('ty') in {1, 3}), key=lambda x: x.get('ty'))
    return result
 
def convert_to_sgf(g_qq: Dict) -> str:
    title = '黑先' if g_qq['blackfirst'] else '白先'
    comment = f"C[{g_qq['title'].strip()}]" if g_qq.get('title') else ''
    size = f"SZ[{g_qq['lu']}]" if g_qq['lu'] != 19 else ''
    prepositions = calculate_prepositions(g_qq)
    variants = calculate_variants(g_qq)

    return f"(;PB[Black]PW[White]HA[0]{size}N[{title} {g_qq['qtypename']}]{comment}{prepositions}{variants})"

# Assuming message handling logic is handled elsewhere
def on_g_qq(level, g_qq) -> None:
    #if msg.get('text') == 'get_g_qq':
    #variable_data = {}  # Simulating the variable data retrieval
    #response = json.loads(g_qq)
    file_name = f"{level}/{g_qq.get('publicid', 101)}.sgf"
    sgf_data = convert_to_sgf(g_qq)
    save_data(sgf_data, file_name)
