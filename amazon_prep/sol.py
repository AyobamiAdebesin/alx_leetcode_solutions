#!/usr/bin/python3
"""
You are provided with a list of commands, containing
the linux standard commands 'mv', 'cp', 'ls'. The list can also contain
the command '!<index>' where '!<index>' can reference any of 
the previous commands. The goal is to return an array of how
many times each standard command ('ls', 'cp', 'mv') was called.

The output array should be in the format:
out_arr = [#times cp, #times ls, #times mv]


For example: commands = ['cp', 'mv', 'ls', '!3', '!1']

Calling !3 will call command at index 3, which is ls(1-index based)

"""
def solution(commands):
    out = [0] * 3
    for i in range(len(commands)):
        cmd = commands[i]
        if check_command(cmd, commands) == 'cp':
            out[0] += 1
        elif check_command(cmd, commands) == 'ls':
            out[1] += 1
        elif check_command(cmd, commands) == 'mv':
            out[2] += 1
    return out

def check_command(cmd, commands):
    if cmd == 'cp':
        return 'cp'
    elif cmd == 'ls':
        return 'ls'
    elif cmd == 'mv':
        return 'mv'
    else:
        arr = str(cmd).split('!')
        idx = arr[1]
        cmd = commands[int(idx)]
        return check_command(cmd, commands)
    





            
