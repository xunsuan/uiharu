/***
 * init.c
 * ``````
 *   初始化模块调用
 */
#include "init.h"
#include "print.h"
#include "interrupt.h"
#include "timer.h"
#include "memory.h"
#include "thread.h"
#include "terminal.h"
#include "keyboard.h"
#include "tss.h"

void init_all(void) {
    /* init_all: 初始化所有模块
     */
    print_string("Info)-> init all\n");
    idt_init();      // 初始化中断向量表(描述符表)
    mem_init();      // 初始化内存管理
    thread_init();   // 初始化线程调度
    timer_init();    // 初始化8253PIC, 提高时钟中断频率(100HZ/S)
    terminal_init(); // 初始化终端设备
    keyboard_init(); // 初始化键盘驱动
    tss_init();      // 初始化tss
    print_string("Info)-> init done\n");
}
