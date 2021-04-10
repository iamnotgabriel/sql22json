import sys
import re
import json
from typing import List, Tuple

def get_keys_values(stmt: str) -> Tuple[str, str]:
    format = lambda tks: [tk.strip() for tk in tks.split(',')]
    keys, _, values = re.search(r'\((.+?)\)(\s*values\s*)\((.+)\)', stmt).groups() 
    return format(keys), format(values)

def parse_stmt(keys: List[str], values: List[str]) -> List[Tuple[str, str]]:
    return dict([(k,v) for k, v in zip(keys, values)])

def sql2json(stmt: str) -> str:
    keys, values = get_keys_values(stmt)
    return parse_stmt(keys, values)

def read_input()-> str:
    if len(sys.argv) != 2:
        raise Exception('usage: json2sql "insert into table(column) values(1)"')
    return sys.argv[1]

def main():
    stmt = read_input()
    obj = sql2json(stmt)
    js = json.dumps(obj)
    print(js)
if __name__ == '__main__':
    main()