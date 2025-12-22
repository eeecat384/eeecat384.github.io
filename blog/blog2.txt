标题：AI是怎么运作的——以GPT-2为例

关键词：AI，LLM，技术博客

发布时间：2025-12-22

开始写之前没想到这玩意工作量这么大.......然后搁置去学C语言了，学完C没忍住去学了stm32，stm32概念真的好多，且让我报一下菜名：

APB: Advanced Peripheral Bus (高级外设总线)
AHB: Advanced High-performance Bus (高级高性能总线)
PPB: Private Peripheral Bus (私有外设总线)
GPIO: General Purpose Input/Output (通用输入/输出)
AFIO: Alternate Function Input/Output (复用功能输入/输出)
Thumb: Thumb Instruction Set (Thumb 指令集)
Banked: Banked Register (分组寄存器)
MSP: Main Stack Pointer (主堆栈指针)
PSP: Process Stack Pointer (进程堆栈指针)
Tail-Chaining: Tail-Chaining (咬尾中断)
SRAM: Static Random Access Memory (静态随机存取存储器)
RAM: Random Access Memory (随机存取存储器)
ROM: Read-Only Memory (只读存储器)
DRAM: Dynamic Random Access Memory (动态随机存取存储器)
MPU Region: Memory Protection Unit Region (存储器保护单元区域)
NVIC: Nested Vectored Interrupt Controller (嵌套向量中断控制器)
Fault: Fault (异常/错误)
Flash: Flash Memory (闪存)
Periph: Peripheral (外设)
RCC: Reset and Clock Control (复位和时钟控制)
SDIO: Secure Digital Input/Output (安全数字输入/输出)
DMA: Direct Memory Access (直接存储器访问)
EXTI: External Interrupt/Event Controller (外部中断/事件控制器)
SysTick: System Timer (系统滴答定时器)
ICode: Instruction Code Bus (指令代码总线)
DCode: Data Code Bus (数据代码总线)

这些只是我看了参考手册几个小时（加上问ai的时间）看到的概念（理解这些概念肯定是不可能的，只能说有个印象）

这下也能理解我为什么不想写了吧......

所以，我就放几个在写这个文章的过程中参考的几篇资料，我想写的基本上这里面都有（说的好听叫深度理解，融合产出。说的不好听就是抄的wwwwww）

CNN笔记：通俗理解卷积神经网络 https://blog.csdn.net/v_JULY_v/article/details/51812459?fromshare=blogdetail&sharetype=blogdetail&sharerId=51812459&sharerefer=PC&sharesource=2502_92292360&sharefrom=from_link
从入门到精通，循环神经网络（RNN）这一篇彻底讲透！ https://blog.csdn.net/Python_cocola/article/details/155521876
史上最详细循环神经网络讲解（RNN/LSTM/GRU） https://zhuanlan.zhihu.com/p/123211148
《Attention Is All You Need》 https://arxiv.org/abs/1706.03762 
常学常新：《Attention Is All You Need》万字解读！ https://zhuanlan.zhihu.com/p/703292893
关于 AI 的深度研究：ChatGPT 正在产生心智吗？ https://www.bilibili.com/video/BV1uu4y1m7ak/?share_source=copy_web&vd_source=651a470a3f58f326e2a9cbe220814164

最后那个视频是优先级最高的的，其他都是可选项，但多学点总没坏处嘛。

等以后有时间再写吧（挖坑）

2025.12.22下午，遗憾收工。