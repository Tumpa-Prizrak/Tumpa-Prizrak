import os

lines = 0

def doSomethingWithDir(path: str):
    for root, dirs, files in os.walk(path):
        for filename in files:
            doSomethingWithFile(os.path.join(root, filename))
        for dirname in dirs:
            doSomethingWithDir(os.path.join(root, dirname))

def doSomethingWithFile(path: str):
    global lines
    if not path.endswith('.py'): return
    try:
        egg = len(open(path).read().split('\n'))
    except UnicodeDecodeError: return
    print(f"{path}: {egg}", "lines")
    lines += egg
    

doSomethingWithDir("MoonCatBot")
print(lines, "lines")