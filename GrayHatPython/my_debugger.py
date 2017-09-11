from ctypes import *
from my_debugger_defines import *
# -*- coding: utf-8 -*-

kernel32 = windll.kernel32


class debugger():
    def __init__(self):
        pass

    def load(self, path_to_exe):
        # 参数 dwCreationFlags中的标志位控制着进程的创建方式。
        # 若希望新创建的进程独占一个新的控制台窗口，而不是与父进程共用同一个控制台
        # 可以加上标志位CREATE_NEW_CONSOLE

        creation_flags = DEBUG_PROCESS

        # 实例化之前定义的结构体
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        '''
        在以下两个成员变量的共同作用下，新建进程将在一个单独的窗体中被显示，
        可以通过改变结构体STARTUPINFO中的各成员变量的值来控制debugee进程的行为
        '''

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        # 设置结构体STARTUPINFO中的成员变量cb的值，用以表示结构体本身的大小
        startupinfo.cb = sizeof(startupinfo)
        if kernel32.CreateProcessW(path_to_exe,
                                    None,
                                    None,
                                    None,
                                    None,
                                    creation_flags,
                                    None,
                                    None,
                                    byref(startupinfo),
                                    byref(process_information)):
            print("[*] We have successfully launched the process!")  # 问题出在这句之前，processInformation获取不到
            # print(path_to_exe)  # b'C:\\Windows\\System32\\calc.exe'
            print("[*] PID: %d" % process_information.dwProcessId)  # 获取PID的时候抛异常，其实是在启动进程的时候出了问题
            # Process finished with exit code -1073741819 (0xC0000005)

        else:
            print("[*] Error: 0x%08x." % kernel32.GetLastError())
