from frontend import TodoAppGUI
from backend import TodoAppBackend

def main():
    file_path = 'tasks.txt'
    backend = TodoAppBackend(file_path)
    gui = TodoAppGUI(backend)
    gui.run()

if __name__ == '__main__':
    main()
