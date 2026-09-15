from dataclasses import dataclass


def summarize(records):
    """返回有效记录的轻量摘要。"""
    valid = [item for item in records if item.get('active')]
    return {'total': len(valid), 'ready': True}


records = [{'active': True}, {'active': False}]
print(summarize(records))
