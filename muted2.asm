
mutated:	file format elf64-x86-64

Disassembly of section .init:

0000000000001000 <_init>:
    1000: f3 0f 1e fa                  	endbr64
    1004: 48 83 ec 08                  	subq	$0x8, %rsp
    1008: 48 8b 05 c9 3f 00 00         	movq	0x3fc9(%rip), %rax      # 0x4fd8 <_GLOBAL_OFFSET_TABLE_+0xc0>
    100f: 48 85 c0                     	testq	%rax, %rax
    1012: 74 02                        	je	0x1016 <_init+0x16>
    1014: ff d0                        	callq	*%rax
    1016: 48 83 c4 08                  	addq	$0x8, %rsp
    101a: c3                           	retq

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020: ff 35 fa 3e 00 00            	pushq	0x3efa(%rip)            # 0x4f20 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026: f2 ff 25 fb 3e 00 00         	repne		jmpq	*0x3efb(%rip)   # 0x4f28 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d: 0f 1f 00                     	nopl	(%rax)
    1030: f3 0f 1e fa                  	endbr64
    1034: 68 00 00 00 00               	pushq	$0x0
    1039: f2 e9 e1 ff ff ff            	repne		jmp	0x1020 <.plt>
    103f: 90                           	nop
    1040: f3 0f 1e fa                  	endbr64
    1044: 68 01 00 00 00               	pushq	$0x1
    1049: f2 e9 d1 ff ff ff            	repne		jmp	0x1020 <.plt>
    104f: 90                           	nop
    1050: f3 0f 1e fa                  	endbr64
    1054: 68 02 00 00 00               	pushq	$0x2
    1059: f2 e9 c1 ff ff ff            	repne		jmp	0x1020 <.plt>
    105f: 90                           	nop
    1060: f3 0f 1e fa                  	endbr64
    1064: 68 03 00 00 00               	pushq	$0x3
    1069: f2 e9 b1 ff ff ff            	repne		jmp	0x1020 <.plt>
    106f: 90                           	nop
    1070: f3 0f 1e fa                  	endbr64
    1074: 68 04 00 00 00               	pushq	$0x4
    1079: f2 e9 a1 ff ff ff            	repne		jmp	0x1020 <.plt>
    107f: 90                           	nop
    1080: f3 0f 1e fa                  	endbr64
    1084: 68 05 00 00 00               	pushq	$0x5
    1089: f2 e9 91 ff ff ff            	repne		jmp	0x1020 <.plt>
    108f: 90                           	nop
    1090: f3 0f 1e fa                  	endbr64
    1094: 68 06 00 00 00               	pushq	$0x6
    1099: f2 e9 81 ff ff ff            	repne		jmp	0x1020 <.plt>
    109f: 90                           	nop
    10a0: f3 0f 1e fa                  	endbr64
    10a4: 68 07 00 00 00               	pushq	$0x7
    10a9: f2 e9 71 ff ff ff            	repne		jmp	0x1020 <.plt>
    10af: 90                           	nop
    10b0: f3 0f 1e fa                  	endbr64
    10b4: 68 08 00 00 00               	pushq	$0x8
    10b9: f2 e9 61 ff ff ff            	repne		jmp	0x1020 <.plt>
    10bf: 90                           	nop
    10c0: f3 0f 1e fa                  	endbr64
    10c4: 68 09 00 00 00               	pushq	$0x9
    10c9: f2 e9 51 ff ff ff            	repne		jmp	0x1020 <.plt>
    10cf: 90                           	nop
    10d0: f3 0f 1e fa                  	endbr64
    10d4: 68 0a 00 00 00               	pushq	$0xa
    10d9: f2 e9 41 ff ff ff            	repne		jmp	0x1020 <.plt>
    10df: 90                           	nop
    10e0: f3 0f 1e fa                  	endbr64
    10e4: 68 0b 00 00 00               	pushq	$0xb
    10e9: f2 e9 31 ff ff ff            	repne		jmp	0x1020 <.plt>
    10ef: 90                           	nop
    10f0: f3 0f 1e fa                  	endbr64
    10f4: 68 0c 00 00 00               	pushq	$0xc
    10f9: f2 e9 21 ff ff ff            	repne		jmp	0x1020 <.plt>
    10ff: 90                           	nop
    1100: f3 0f 1e fa                  	endbr64
    1104: 68 0d 00 00 00               	pushq	$0xd
    1109: f2 e9 11 ff ff ff            	repne		jmp	0x1020 <.plt>
    110f: 90                           	nop
    1110: f3 0f 1e fa                  	endbr64
    1114: 68 0e 00 00 00               	pushq	$0xe
    1119: f2 e9 01 ff ff ff            	repne		jmp	0x1020 <.plt>
    111f: 90                           	nop
    1120: f3 0f 1e fa                  	endbr64
    1124: 68 0f 00 00 00               	pushq	$0xf
    1129: f2 e9 f1 fe ff ff            	repne		jmp	0x1020 <.plt>
    112f: 90                           	nop
    1130: f3 0f 1e fa                  	endbr64
    1134: 68 10 00 00 00               	pushq	$0x10
    1139: f2 e9 e1 fe ff ff            	repne		jmp	0x1020 <.plt>
    113f: 90                           	nop
    1140: f3 0f 1e fa                  	endbr64
    1144: 68 11 00 00 00               	pushq	$0x11
    1149: f2 e9 d1 fe ff ff            	repne		jmp	0x1020 <.plt>
    114f: 90                           	nop
    1150: f3 0f 1e fa                  	endbr64
    1154: 68 12 00 00 00               	pushq	$0x12
    1159: f2 e9 c1 fe ff ff            	repne		jmp	0x1020 <.plt>
    115f: 90                           	nop
    1160: f3 0f 1e fa                  	endbr64
    1164: 68 13 00 00 00               	pushq	$0x13
    1169: f2 e9 b1 fe ff ff            	repne		jmp	0x1020 <.plt>
    116f: 90                           	nop
    1170: f3 0f 1e fa                  	endbr64
    1174: 68 14 00 00 00               	pushq	$0x14
    1179: f2 e9 a1 fe ff ff            	repne		jmp	0x1020 <.plt>
    117f: 90                           	nop

Disassembly of section .plt.got:

0000000000001180 <.plt.got>:
    1180: f3 0f 1e fa                  	endbr64
    1184: f2 ff 25 65 3e 00 00         	repne		jmpq	*0x3e65(%rip)   # 0x4ff0 <_GLOBAL_OFFSET_TABLE_+0xd8>

0000000000001185 <__cxa_finalize@plt>:
    1185: ff 25 65 3e 00 00            	jmpq	*0x3e65(%rip)           # 0x4ff0 <_GLOBAL_OFFSET_TABLE_+0xd8>
    118b: 0f 1f 44 00 00               	nopl	(%rax,%rax)

Disassembly of section .plt.sec:

0000000000001190 <.plt.sec>:
    1190: f3 0f 1e fa                  	endbr64
    1194: f2 ff 25 95 3d 00 00         	repne		jmpq	*0x3d95(%rip)   # 0x4f30 <_GLOBAL_OFFSET_TABLE_+0x18>
    119b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    11a0: f3 0f 1e fa                  	endbr64
    11a4: f2 ff 25 8d 3d 00 00         	repne		jmpq	*0x3d8d(%rip)   # 0x4f38 <_GLOBAL_OFFSET_TABLE_+0x20>
    11ab: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    11b0: f3 0f 1e fa                  	endbr64
    11b4: f2 ff 25 85 3d 00 00         	repne		jmpq	*0x3d85(%rip)   # 0x4f40 <_GLOBAL_OFFSET_TABLE_+0x28>
    11bb: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    11c0: f3 0f 1e fa                  	endbr64
    11c4: f2 ff 25 7d 3d 00 00         	repne		jmpq	*0x3d7d(%rip)   # 0x4f48 <_GLOBAL_OFFSET_TABLE_+0x30>
    11cb: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    11d0: f3 0f 1e fa                  	endbr64
    11d4: f2 ff 25 75 3d 00 00         	repne		jmpq	*0x3d75(%rip)   # 0x4f50 <_GLOBAL_OFFSET_TABLE_+0x38>
    11db: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    11e0: f3 0f 1e fa                  	endbr64
    11e4: f2 ff 25 6d 3d 00 00         	repne		jmpq	*0x3d6d(%rip)   # 0x4f58 <_GLOBAL_OFFSET_TABLE_+0x40>
    11eb: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    11f0: f3 0f 1e fa                  	endbr64
    11f4: f2 ff 25 65 3d 00 00         	repne		jmpq	*0x3d65(%rip)   # 0x4f60 <_GLOBAL_OFFSET_TABLE_+0x48>
    11fb: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1200: f3 0f 1e fa                  	endbr64
    1204: f2 ff 25 5d 3d 00 00         	repne		jmpq	*0x3d5d(%rip)   # 0x4f68 <_GLOBAL_OFFSET_TABLE_+0x50>
    120b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1210: f3 0f 1e fa                  	endbr64
    1214: f2 ff 25 55 3d 00 00         	repne		jmpq	*0x3d55(%rip)   # 0x4f70 <_GLOBAL_OFFSET_TABLE_+0x58>
    121b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1220: f3 0f 1e fa                  	endbr64
    1224: f2 ff 25 4d 3d 00 00         	repne		jmpq	*0x3d4d(%rip)   # 0x4f78 <_GLOBAL_OFFSET_TABLE_+0x60>
    122b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1230: f3 0f 1e fa                  	endbr64
    1234: f2 ff 25 45 3d 00 00         	repne		jmpq	*0x3d45(%rip)   # 0x4f80 <_GLOBAL_OFFSET_TABLE_+0x68>
    123b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1240: f3 0f 1e fa                  	endbr64
    1244: f2 ff 25 3d 3d 00 00         	repne		jmpq	*0x3d3d(%rip)   # 0x4f88 <_GLOBAL_OFFSET_TABLE_+0x70>
    124b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1250: f3 0f 1e fa                  	endbr64
    1254: f2 ff 25 35 3d 00 00         	repne		jmpq	*0x3d35(%rip)   # 0x4f90 <_GLOBAL_OFFSET_TABLE_+0x78>
    125b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1260: f3 0f 1e fa                  	endbr64
    1264: f2 ff 25 2d 3d 00 00         	repne		jmpq	*0x3d2d(%rip)   # 0x4f98 <_GLOBAL_OFFSET_TABLE_+0x80>
    126b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1270: f3 0f 1e fa                  	endbr64
    1274: f2 ff 25 25 3d 00 00         	repne		jmpq	*0x3d25(%rip)   # 0x4fa0 <_GLOBAL_OFFSET_TABLE_+0x88>
    127b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1280: f3 0f 1e fa                  	endbr64
    1284: f2 ff 25 1d 3d 00 00         	repne		jmpq	*0x3d1d(%rip)   # 0x4fa8 <_GLOBAL_OFFSET_TABLE_+0x90>
    128b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    1290: f3 0f 1e fa                  	endbr64
    1294: f2 ff 25 15 3d 00 00         	repne		jmpq	*0x3d15(%rip)   # 0x4fb0 <_GLOBAL_OFFSET_TABLE_+0x98>
    129b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    12a0: f3 0f 1e fa                  	endbr64
    12a4: f2 ff 25 0d 3d 00 00         	repne		jmpq	*0x3d0d(%rip)   # 0x4fb8 <_GLOBAL_OFFSET_TABLE_+0xa0>
    12ab: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    12b0: f3 0f 1e fa                  	endbr64
    12b4: f2 ff 25 05 3d 00 00         	repne		jmpq	*0x3d05(%rip)   # 0x4fc0 <_GLOBAL_OFFSET_TABLE_+0xa8>
    12bb: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    12c0: f3 0f 1e fa                  	endbr64
    12c4: f2 ff 25 fd 3c 00 00         	repne		jmpq	*0x3cfd(%rip)   # 0x4fc8 <_GLOBAL_OFFSET_TABLE_+0xb0>
    12cb: 0f 1f 44 00 00               	nopl	(%rax,%rax)
    12d0: f3 0f 1e fa                  	endbr64
    12d4: f2 ff 25 f5 3c 00 00         	repne		jmpq	*0x3cf5(%rip)   # 0x4fd0 <_GLOBAL_OFFSET_TABLE_+0xb8>
    12db: 0f 1f 44 00 00               	nopl	(%rax,%rax)

Disassembly of section .text:

00000000000012e0 <_start>:
    12e0: f3 0f 1e fa                  	endbr64
    12e4: 31 ed                        	xorl	%ebp, %ebp
    12e6: 49 89 d1                     	movq	%rdx, %r9
    12e9: 5e                           	popq	%rsi
    12ea: 48 89 e2                     	movq	%rsp, %rdx
    12ed: 48 83 e4 f0                  	andq	$-0x10, %rsp
    12f1: 50                           	pushq	%rax
    12f2: 54                           	pushq	%rsp
    12f3: 45 29 c0                     	subl	%r8d, %r8d
    12f6: 31 c9                        	xorl	%ecx, %ecx
    12f8: 48 8d 3d 46 0e 00 00         	leaq	0xe46(%rip), %rdi       # 0x2145 <main>
    12ff: ff 15 f3 3c 00 00            	callq	*0x3cf3(%rip)           # 0x4ff8 <_GLOBAL_OFFSET_TABLE_+0xe0>
    1305: f4                           	hlt
    1306: 66 2e 0f 1f 84 00 00 00 00 00	nopw	%cs:(%rax,%rax)

0000000000001310 <deregister_tm_clones>:
    1310: 48 8d 3d f9 3c 00 00         	leaq	0x3cf9(%rip), %rdi      # 0x5010 <_edata>
    1317: 48 8d 05 f2 3c 00 00         	leaq	0x3cf2(%rip), %rax      # 0x5010 <_edata>
    131e: 48 39 f8                     	cmpq	%rdi, %rax
    1321: 74 15                        	je	0x1338 <deregister_tm_clones+0x28>
    1323: 48 8b 05 b6 3c 00 00         	movq	0x3cb6(%rip), %rax      # 0x4fe0 <_GLOBAL_OFFSET_TABLE_+0xc8>
    132a: 48 09 c0                     	orq	%rax, %rax
    132d: 74 09                        	je	0x1338 <deregister_tm_clones+0x28>
    132f: ff e0                        	jmpq	*%rax
    1331: 0f 1f 80 00 00 00 00         	nopl	(%rax)
    1338: c3                           	retq
    1339: 0f 1f 80 00 00 00 00         	nopl	(%rax)

0000000000001340 <register_tm_clones>:
    1340: 48 8d 3d c9 3c 00 00         	leaq	0x3cc9(%rip), %rdi      # 0x5010 <_edata>
    1347: 48 8d 35 c2 3c 00 00         	leaq	0x3cc2(%rip), %rsi      # 0x5010 <_edata>
    134e: 48 29 fe                     	subq	%rdi, %rsi
    1351: 48 89 f0                     	movq	%rsi, %rax
    1354: 48 c1 ee 3f                  	shrq	$0x3f, %rsi
    1358: 48 c1 f8 03                  	sarq	$0x3, %rax
    135c: 48 01 c6                     	addq	%rax, %rsi
    135f: 48 d1 fe                     	sarq	%rsi
    1362: 74 14                        	je	0x1378 <register_tm_clones+0x38>
    1364: 48 8b 05 7d 3c 00 00         	movq	0x3c7d(%rip), %rax      # 0x4fe8 <_GLOBAL_OFFSET_TABLE_+0xd0>
    136b: 48 09 c0                     	orq	%rax, %rax
    136e: 74 08                        	je	0x1378 <register_tm_clones+0x38>
    1370: ff e0                        	jmpq	*%rax
    1372: 66 0f 1f 44 00 00            	nopw	(%rax,%rax)
    1378: c3                           	retq
    1379: 0f 1f 80 00 00 00 00         	nopl	(%rax)

0000000000001380 <__do_global_dtors_aux>:
    1380: f3 0f 1e fa                  	endbr64
    1384: 80 3d 9d 3c 00 00 00         	cmpb	$0x0, 0x3c9d(%rip)      # 0x5028 <completed.0>
    138b: 75 2b                        	jne	0x13b8 <__do_global_dtors_aux+0x38>
    138d: 55                           	pushq	%rbp
    138e: 48 83 3d 5a 3c 00 00 00      	cmpq	$0x0, 0x3c5a(%rip)      # 0x4ff0 <_GLOBAL_OFFSET_TABLE_+0xd8>
    1396: 54                           	pushq	%rsp
    1397: 90                           	nop
    1398: 5d                           	popq	%rbp
    1399: 74 0c                        	je	0x13a7 <__do_global_dtors_aux+0x27>
    139b: 48 8b 3d 66 3c 00 00         	movq	0x3c66(%rip), %rdi      # 0x5008 <__dso_handle>
    13a2: e8 d9 fd ff ff               	callq	0x1180 <.plt.got>
    13a7: e8 64 ff ff ff               	callq	0x1310 <deregister_tm_clones>
    13ac: c6 05 75 3c 00 00 01         	movb	$0x1, 0x3c75(%rip)      # 0x5028 <completed.0>
    13b3: 5d                           	popq	%rbp
    13b4: c3                           	retq
    13b5: 0f 1f 00                     	nopl	(%rax)
    13b8: c3                           	retq
    13b9: 0f 1f 80 00 00 00 00         	nopl	(%rax)

00000000000013c0 <frame_dummy>:
    13c0: f3 0f 1e fa                  	endbr64
    13c4: e9 77 ff ff ff               	jmp	0x1340 <register_tm_clones>

00000000000013c9 <init_store>:
    13c9: f3 0f 1e fa                  	endbr64
    13cd: 55                           	pushq	%rbp
    13ce: 54                           	pushq	%rsp
    13cf: 90                           	nop
    13d0: 5d                           	popq	%rbp
    13d1: c7 45 fc 00 00 00 00         	movl	$0x0, -0x4(%rbp)
    13d8: eb 29                        	jmp	0x1403 <init_store+0x3a>
    13da: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    13dd: 48 63 d0                     	movslq	%eax, %rdx
    13e0: 52                           	pushq	%rdx
    13e1: 90                           	nop
    13e2: 58                           	popq	%rax
    13e3: 48 c1 e0 05                  	shlq	$0x5, %rax
    13e7: 48 01 d0                     	addq	%rdx, %rax
    13ea: 48 c1 e0 03                  	shlq	$0x3, %rax
    13ee: 90                           	nop
    13ef: 50                           	pushq	%rax
    13f0: 5a                           	popq	%rdx
    13f1: 48 8d 05 4c 3d 00 00         	leaq	0x3d4c(%rip), %rax      # 0x5144 <store+0x104>
    13f8: c7 04 02 00 00 00 00         	movl	$0x0, (%rdx,%rax)
    13ff: 83 45 fc 01                  	addl	$0x1, -0x4(%rbp)
    1403: 83 7d fc 09                  	cmpl	$0x9, -0x4(%rbp)
    1407: 7e d1                        	jle	0x13da <init_store+0x11>
    1409: 53                           	pushq	%rbx
    140a: 5b                           	popq	%rbx
    140b: 5d                           	popq	%rbp
    140c: c3                           	retq

000000000000140d <find_index>:
    140d: f3 0f 1e fa                  	endbr64
    1411: 55                           	pushq	%rbp
    1412: 48 89 e5                     	movq	%rsp, %rbp
    1415: 89 7d ec                     	movl	%edi, -0x14(%rbp)
    1418: c7 45 fc 00 00 00 00         	movl	$0x0, -0x4(%rbp)
    141f: eb 54                        	jmp	0x1475 <find_index+0x68>
    1421: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    1424: 48 63 d0                     	movslq	%eax, %rdx
    1427: 52                           	pushq	%rdx
    1428: 58                           	popq	%rax
    1429: 90                           	nop
    142a: 48 c1 e0 05                  	shlq	$0x5, %rax
    142e: 48 01 d0                     	addq	%rdx, %rax
    1431: 48 c1 e0 03                  	shlq	$0x3, %rax
    1435: 90                           	nop
    1436: 50                           	pushq	%rax
    1437: 5a                           	popq	%rdx
    1438: 48 8d 05 05 3d 00 00         	leaq	0x3d05(%rip), %rax      # 0x5144 <store+0x104>
    143f: 8b 04 02                     	movl	(%rdx,%rax), %eax
    1442: 85 c0                        	testl	%eax, %eax
    1444: 74 2b                        	je	0x1471 <find_index+0x64>
    1446: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    1449: 48 63 d0                     	movslq	%eax, %rdx
    144c: 48 89 d0                     	movq	%rdx, %rax
    144f: 48 c1 e0 05                  	shlq	$0x5, %rax
    1453: 48 01 d0                     	addq	%rdx, %rax
    1456: 48 c1 e0 03                  	shlq	$0x3, %rax
    145a: 90                           	nop
    145b: 50                           	pushq	%rax
    145c: 5a                           	popq	%rdx
    145d: 48 8d 05 dc 3b 00 00         	leaq	0x3bdc(%rip), %rax      # 0x5040 <store>
    1464: 8b 04 02                     	movl	(%rdx,%rax), %eax
    1467: 39 45 ec                     	cmpl	%eax, -0x14(%rbp)
    146a: 75 05                        	jne	0x1471 <find_index+0x64>
    146c: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    146f: eb 0f                        	jmp	0x1480 <find_index+0x73>
    1471: 83 45 fc 01                  	addl	$0x1, -0x4(%rbp)
    1475: 83 7d fc 09                  	cmpl	$0x9, -0x4(%rbp)
    1479: 7e a6                        	jle	0x1421 <find_index+0x14>
    147b: b8 ff ff ff ff               	movl	$0xffffffff, %eax       # imm = 0xFFFFFFFF
    1480: 5d                           	popq	%rbp
    1481: c3                           	retq

0000000000001482 <add_item>:
    1482: f3 0f 1e fa                  	endbr64
    1486: 55                           	pushq	%rbp
    1487: 54                           	pushq	%rsp
    1488: 90                           	nop
    1489: 5d                           	popq	%rbp
    148a: 48 83 ec 20                  	subq	$0x20, %rsp
    148e: 89 7d ec                     	movl	%edi, -0x14(%rbp)
    1491: 48 89 75 e0                  	movq	%rsi, -0x20(%rbp)
    1495: 8b 45 ec                     	movl	-0x14(%rbp), %eax
    1498: 89 c7                        	movl	%eax, %edi
    149a: e8 6e ff ff ff               	callq	0x140d <find_index>
    149f: 83 f8 ff                     	cmpl	$-0x1, %eax
    14a2: 74 0a                        	je	0x14ae <add_item+0x2c>
    14a4: b8 ff ff ff ff               	movl	$0xffffffff, %eax       # imm = 0xFFFFFFFF
    14a9: e9 f0 00 00 00               	jmp	0x159e <add_item+0x11c>
    14ae: c7 45 fc 00 00 00 00         	movl	$0x0, -0x4(%rbp)
    14b5: e9 d5 00 00 00               	jmp	0x158f <add_item+0x10d>
    14ba: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    14bd: 48 63 d0                     	movslq	%eax, %rdx
    14c0: 90                           	nop
    14c1: 52                           	pushq	%rdx
    14c2: 58                           	popq	%rax
    14c3: 48 c1 e0 05                  	shlq	$0x5, %rax
    14c7: 48 01 d0                     	addq	%rdx, %rax
    14ca: 48 c1 e0 03                  	shlq	$0x3, %rax
    14ce: 90                           	nop
    14cf: 50                           	pushq	%rax
    14d0: 5a                           	popq	%rdx
    14d1: 48 8d 05 6c 3c 00 00         	leaq	0x3c6c(%rip), %rax      # 0x5144 <store+0x104>
    14d8: 8b 04 02                     	movl	(%rdx,%rax), %eax
    14db: 09 c0                        	orl	%eax, %eax
    14dd: 0f 85 a8 00 00 00            	jne	0x158b <add_item+0x109>
    14e3: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    14e6: 48 63 d0                     	movslq	%eax, %rdx
    14e9: 52                           	pushq	%rdx
    14ea: 58                           	popq	%rax
    14eb: 90                           	nop
    14ec: 48 c1 e0 05                  	shlq	$0x5, %rax
    14f0: 48 01 d0                     	addq	%rdx, %rax
    14f3: 48 c1 e0 03                  	shlq	$0x3, %rax
    14f7: 48 89 c1                     	movq	%rax, %rcx
    14fa: 48 8d 15 3f 3b 00 00         	leaq	0x3b3f(%rip), %rdx      # 0x5040 <store>
    1501: 8b 45 ec                     	movl	-0x14(%rbp), %eax
    1504: 89 04 11                     	movl	%eax, (%rcx,%rdx)
    1507: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    150a: 48 63 d0                     	movslq	%eax, %rdx
    150d: 52                           	pushq	%rdx
    150e: 90                           	nop
    150f: 58                           	popq	%rax
    1510: 48 c1 e0 05                  	shlq	$0x5, %rax
    1514: 48 01 d0                     	addq	%rdx, %rax
    1517: 48 c1 e0 03                  	shlq	$0x3, %rax
    151b: 48 8d 15 1e 3b 00 00         	leaq	0x3b1e(%rip), %rdx      # 0x5040 <store>
    1522: 48 01 d0                     	addq	%rdx, %rax
    1525: 48 8d 48 04                  	leaq	0x4(%rax), %rcx
    1529: 48 8b 45 e0                  	movq	-0x20(%rbp), %rax
    152d: ba ff 00 00 00               	movl	$0xff, %edx
    1532: 50                           	pushq	%rax
    1533: 90                           	nop
    1534: 5e                           	popq	%rsi
    1535: 51                           	pushq	%rcx
    1536: 5f                           	popq	%rdi
    1537: 90                           	nop
    1538: e8 43 fd ff ff               	callq	0x1280 <.plt.sec+0xf0>
    153d: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    1540: 48 63 d0                     	movslq	%eax, %rdx
    1543: 52                           	pushq	%rdx
    1544: 58                           	popq	%rax
    1545: 90                           	nop
    1546: 48 c1 e0 05                  	shlq	$0x5, %rax
    154a: 48 01 d0                     	addq	%rdx, %rax
    154d: 48 c1 e0 03                  	shlq	$0x3, %rax
    1551: 90                           	nop
    1552: 50                           	pushq	%rax
    1553: 5a                           	popq	%rdx
    1554: 48 8d 05 e8 3b 00 00         	leaq	0x3be8(%rip), %rax      # 0x5143 <store+0x103>
    155b: c6 04 02 00                  	movb	$0x0, (%rdx,%rax)
    155f: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    1562: 48 63 d0                     	movslq	%eax, %rdx
    1565: 52                           	pushq	%rdx
    1566: 90                           	nop
    1567: 58                           	popq	%rax
    1568: 48 c1 e0 05                  	shlq	$0x5, %rax
    156c: 48 01 d0                     	addq	%rdx, %rax
    156f: 48 c1 e0 03                  	shlq	$0x3, %rax
    1573: 50                           	pushq	%rax
    1574: 5a                           	popq	%rdx
    1575: 90                           	nop
    1576: 48 8d 05 c7 3b 00 00         	leaq	0x3bc7(%rip), %rax      # 0x5144 <store+0x104>
    157d: c7 04 02 01 00 00 00         	movl	$0x1, (%rdx,%rax)
    1584: b8 00 00 00 00               	movl	$0x0, %eax
    1589: eb 13                        	jmp	0x159e <add_item+0x11c>
    158b: 83 45 fc 01                  	addl	$0x1, -0x4(%rbp)
    158f: 83 7d fc 09                  	cmpl	$0x9, -0x4(%rbp)
    1593: 0f 8e 21 ff ff ff            	jle	0x14ba <add_item+0x38>
    1599: b8 fe ff ff ff               	movl	$0xfffffffe, %eax       # imm = 0xFFFFFFFE
    159e: c9                           	leave
    159f: c3                           	retq

00000000000015a0 <get_item_data>:
    15a0: f3 0f 1e fa                  	endbr64
    15a4: 55                           	pushq	%rbp
    15a5: 48 89 e5                     	movq	%rsp, %rbp
    15a8: 48 83 ec 18                  	subq	$0x18, %rsp
    15ac: 89 7d ec                     	movl	%edi, -0x14(%rbp)
    15af: 8b 45 ec                     	movl	-0x14(%rbp), %eax
    15b2: 89 c7                        	movl	%eax, %edi
    15b4: e8 54 fe ff ff               	callq	0x140d <find_index>
    15b9: 89 45 fc                     	movl	%eax, -0x4(%rbp)
    15bc: 83 7d fc ff                  	cmpl	$-0x1, -0x4(%rbp)
    15c0: 74 24                        	je	0x15e6 <get_item_data+0x46>
    15c2: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    15c5: 48 63 d0                     	movslq	%eax, %rdx
    15c8: 90                           	nop
    15c9: 52                           	pushq	%rdx
    15ca: 58                           	popq	%rax
    15cb: 48 c1 e0 05                  	shlq	$0x5, %rax
    15cf: 48 01 d0                     	addq	%rdx, %rax
    15d2: 48 c1 e0 03                  	shlq	$0x3, %rax
    15d6: 48 8d 15 63 3a 00 00         	leaq	0x3a63(%rip), %rdx      # 0x5040 <store>
    15dd: 48 01 d0                     	addq	%rdx, %rax
    15e0: 48 83 c0 04                  	addq	$0x4, %rax
    15e4: eb 05                        	jmp	0x15eb <get_item_data+0x4b>
    15e6: b8 00 00 00 00               	movl	$0x0, %eax
    15eb: c9                           	leave
    15ec: c3                           	retq

00000000000015ed <update_item>:
    15ed: f3 0f 1e fa                  	endbr64
    15f1: 55                           	pushq	%rbp
    15f2: 54                           	pushq	%rsp
    15f3: 5d                           	popq	%rbp
    15f4: 90                           	nop
    15f5: 48 83 ec 20                  	subq	$0x20, %rsp
    15f9: 89 7d ec                     	movl	%edi, -0x14(%rbp)
    15fc: 48 89 75 e0                  	movq	%rsi, -0x20(%rbp)
    1600: 8b 45 ec                     	movl	-0x14(%rbp), %eax
    1603: 89 c7                        	movl	%eax, %edi
    1605: e8 03 fe ff ff               	callq	0x140d <find_index>
    160a: 89 45 fc                     	movl	%eax, -0x4(%rbp)
    160d: 83 7d fc ff                  	cmpl	$-0x1, -0x4(%rbp)
    1611: 75 07                        	jne	0x161a <update_item+0x2d>
    1613: b8 ff ff ff ff               	movl	$0xffffffff, %eax       # imm = 0xFFFFFFFF
    1618: eb 5d                        	jmp	0x1677 <update_item+0x8a>
    161a: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    161d: 48 63 d0                     	movslq	%eax, %rdx
    1620: 52                           	pushq	%rdx
    1621: 90                           	nop
    1622: 58                           	popq	%rax
    1623: 48 c1 e0 05                  	shlq	$0x5, %rax
    1627: 48 01 d0                     	addq	%rdx, %rax
    162a: 48 c1 e0 03                  	shlq	$0x3, %rax
    162e: 48 8d 15 0b 3a 00 00         	leaq	0x3a0b(%rip), %rdx      # 0x5040 <store>
    1635: 48 01 d0                     	addq	%rdx, %rax
    1638: 48 8d 48 04                  	leaq	0x4(%rax), %rcx
    163c: 48 8b 45 e0                  	movq	-0x20(%rbp), %rax
    1640: ba ff 00 00 00               	movl	$0xff, %edx
    1645: 50                           	pushq	%rax
    1646: 90                           	nop
    1647: 5e                           	popq	%rsi
    1648: 51                           	pushq	%rcx
    1649: 5f                           	popq	%rdi
    164a: 90                           	nop
    164b: e8 30 fc ff ff               	callq	0x1280 <.plt.sec+0xf0>
    1650: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    1653: 48 63 d0                     	movslq	%eax, %rdx
    1656: 90                           	nop
    1657: 52                           	pushq	%rdx
    1658: 58                           	popq	%rax
    1659: 48 c1 e0 05                  	shlq	$0x5, %rax
    165d: 48 01 d0                     	addq	%rdx, %rax
    1660: 48 c1 e0 03                  	shlq	$0x3, %rax
    1664: 50                           	pushq	%rax
    1665: 90                           	nop
    1666: 5a                           	popq	%rdx
    1667: 48 8d 05 d5 3a 00 00         	leaq	0x3ad5(%rip), %rax      # 0x5143 <store+0x103>
    166e: c6 04 02 00                  	movb	$0x0, (%rdx,%rax)
    1672: b8 00 00 00 00               	movl	$0x0, %eax
    1677: c9                           	leave
    1678: c3                           	retq

0000000000001679 <delete_item>:
    1679: f3 0f 1e fa                  	endbr64
    167d: 55                           	pushq	%rbp
    167e: 48 89 e5                     	movq	%rsp, %rbp
    1681: 48 83 ec 18                  	subq	$0x18, %rsp
    1685: 89 7d ec                     	movl	%edi, -0x14(%rbp)
    1688: 8b 45 ec                     	movl	-0x14(%rbp), %eax
    168b: 89 c7                        	movl	%eax, %edi
    168d: e8 7b fd ff ff               	callq	0x140d <find_index>
    1692: 89 45 fc                     	movl	%eax, -0x4(%rbp)
    1695: 83 7d fc ff                  	cmpl	$-0x1, -0x4(%rbp)
    1699: 75 07                        	jne	0x16a2 <delete_item+0x29>
    169b: b8 ff ff ff ff               	movl	$0xffffffff, %eax       # imm = 0xFFFFFFFF
    16a0: eb 2a                        	jmp	0x16cc <delete_item+0x53>
    16a2: 8b 45 fc                     	movl	-0x4(%rbp), %eax
    16a5: 48 63 d0                     	movslq	%eax, %rdx
    16a8: 90                           	nop
    16a9: 52                           	pushq	%rdx
    16aa: 58                           	popq	%rax
    16ab: 48 c1 e0 05                  	shlq	$0x5, %rax
    16af: 48 01 d0                     	addq	%rdx, %rax
    16b2: 48 c1 e0 03                  	shlq	$0x3, %rax
    16b6: 50                           	pushq	%rax
    16b7: 5a                           	popq	%rdx
    16b8: 90                           	nop
    16b9: 48 8d 05 84 3a 00 00         	leaq	0x3a84(%rip), %rax      # 0x5144 <store+0x104>
    16c0: c7 04 02 00 00 00 00         	movl	$0x0, (%rdx,%rax)
    16c7: b8 00 00 00 00               	movl	$0x0, %eax
    16cc: c9                           	leave
    16cd: c3                           	retq

00000000000016ce <list_items_str>:
    16ce: f3 0f 1e fa                  	endbr64
    16d2: 55                           	pushq	%rbp
    16d3: 54                           	pushq	%rsp
    16d4: 90                           	nop
    16d5: 5d                           	popq	%rbp
    16d6: 48 81 ec 60 01 00 00         	subq	$0x160, %rsp            # imm = 0x160
    16dd: 48 89 bd a8 fe ff ff         	movq	%rdi, -0x158(%rbp)
    16e4: 48 89 b5 a0 fe ff ff         	movq	%rsi, -0x160(%rbp)
    16eb: 64 48 8b 04 25 28 00 00 00   	movq	%fs:0x28, %rax
    16f4: 48 89 45 f8                  	movq	%rax, -0x8(%rbp)
    16f8: 29 c0                        	subl	%eax, %eax
    16fa: 48 8b 8d a0 fe ff ff         	movq	-0x160(%rbp), %rcx
    1701: 48 8b 85 a8 fe ff ff         	movq	-0x158(%rbp), %rax
    1708: 48 8d 15 f5 18 00 00         	leaq	0x18f5(%rip), %rdx      # 0x3004 <_IO_stdin_used+0x4>
    170f: 90                           	nop
    1710: 51                           	pushq	%rcx
    1711: 5e                           	popq	%rsi
    1712: 50                           	pushq	%rax
    1713: 90                           	nop
    1714: 5f                           	popq	%rdi
    1715: b8 00 00 00 00               	movl	$0x0, %eax
    171a: e8 81 fa ff ff               	callq	0x11a0 <.plt.sec+0x10>
    171f: c7 85 bc fe ff ff 00 00 00 00	movl	$0x0, -0x144(%rbp)
    1729: e9 da 00 00 00               	jmp	0x1808 <list_items_str+0x13a>
    172e: 8b 85 bc fe ff ff            	movl	-0x144(%rbp), %eax
    1734: 48 63 d0                     	movslq	%eax, %rdx
    1737: 90                           	nop
    1738: 52                           	pushq	%rdx
    1739: 58                           	popq	%rax
    173a: 48 c1 e0 05                  	shlq	$0x5, %rax
    173e: 48 01 d0                     	addq	%rdx, %rax
    1741: 48 c1 e0 03                  	shlq	$0x3, %rax
    1745: 90                           	nop
    1746: 50                           	pushq	%rax
    1747: 5a                           	popq	%rdx
    1748: 48 8d 05 f5 39 00 00         	leaq	0x39f5(%rip), %rax      # 0x5144 <store+0x104>
    174f: 8b 04 02                     	movl	(%rdx,%rax), %eax
    1752: 85 c0                        	testl	%eax, %eax
    1754: 0f 84 a7 00 00 00            	je	0x1801 <list_items_str+0x133>
    175a: 8b 85 bc fe ff ff            	movl	-0x144(%rbp), %eax
    1760: 48 63 d0                     	movslq	%eax, %rdx
    1763: 52                           	pushq	%rdx
    1764: 90                           	nop
    1765: 58                           	popq	%rax
    1766: 48 c1 e0 05                  	shlq	$0x5, %rax
    176a: 48 01 d0                     	addq	%rdx, %rax
    176d: 48 c1 e0 03                  	shlq	$0x3, %rax
    1771: 48 8d 15 c8 38 00 00         	leaq	0x38c8(%rip), %rdx      # 0x5040 <store>
    1778: 48 01 d0                     	addq	%rdx, %rax
    177b: 48 8d 48 04                  	leaq	0x4(%rax), %rcx
    177f: 8b 85 bc fe ff ff            	movl	-0x144(%rbp), %eax
    1785: 48 63 d0                     	movslq	%eax, %rdx
    1788: 52                           	pushq	%rdx
    1789: 90                           	nop
    178a: 58                           	popq	%rax
    178b: 48 c1 e0 05                  	shlq	$0x5, %rax
    178f: 48 01 d0                     	addq	%rdx, %rax
    1792: 48 c1 e0 03                  	shlq	$0x3, %rax
    1796: 50                           	pushq	%rax
    1797: 5a                           	popq	%rdx
    1798: 90                           	nop
    1799: 48 8d 05 a0 38 00 00         	leaq	0x38a0(%rip), %rax      # 0x5040 <store>
    17a0: 8b 14 02                     	movl	(%rdx,%rax), %edx
    17a3: 48 8d 85 c0 fe ff ff         	leaq	-0x140(%rbp), %rax
    17aa: 49 89 c8                     	movq	%rcx, %r8
    17ad: 89 d1                        	movl	%edx, %ecx
    17af: 48 8d 15 56 18 00 00         	leaq	0x1856(%rip), %rdx      # 0x300c <_IO_stdin_used+0xc>
    17b6: be 2c 01 00 00               	movl	$0x12c, %esi            # imm = 0x12C
    17bb: 50                           	pushq	%rax
    17bc: 90                           	nop
    17bd: 5f                           	popq	%rdi
    17be: b8 00 00 00 00               	movl	$0x0, %eax
    17c3: e8 d8 f9 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    17c8: 48 8b 85 a8 fe ff ff         	movq	-0x158(%rbp), %rax
    17cf: 48 89 c7                     	movq	%rax, %rdi
    17d2: e8 29 fa ff ff               	callq	0x1200 <.plt.sec+0x70>
    17d7: 48 89 c2                     	movq	%rax, %rdx
    17da: 48 8b 85 a0 fe ff ff         	movq	-0x160(%rbp), %rax
    17e1: 48 29 d0                     	subq	%rdx, %rax
    17e4: 48 8d 50 ff                  	leaq	-0x1(%rax), %rdx
    17e8: 48 8d 8d c0 fe ff ff         	leaq	-0x140(%rbp), %rcx
    17ef: 48 8b 85 a8 fe ff ff         	movq	-0x158(%rbp), %rax
    17f6: 48 89 ce                     	movq	%rcx, %rsi
    17f9: 50                           	pushq	%rax
    17fa: 5f                           	popq	%rdi
    17fb: 90                           	nop
    17fc: e8 af f9 ff ff               	callq	0x11b0 <.plt.sec+0x20>
    1801: 83 85 bc fe ff ff 01         	addl	$0x1, -0x144(%rbp)
    1808: 83 bd bc fe ff ff 09         	cmpl	$0x9, -0x144(%rbp)
    180f: 0f 8e 19 ff ff ff            	jle	0x172e <list_items_str+0x60>
    1815: 90                           	nop
    1816: 48 8b 45 f8                  	movq	-0x8(%rbp), %rax
    181a: 64 48 2b 04 25 28 00 00 00   	subq	%fs:0x28, %rax
    1823: 74 05                        	je	0x182a <list_items_str+0x15c>
    1825: e8 26 fa ff ff               	callq	0x1250 <.plt.sec+0xc0>
    182a: c9                           	leave
    182b: c3                           	retq

000000000000182c <request_handler>:
    182c: f3 0f 1e fa                  	endbr64
    1830: 55                           	pushq	%rbp
    1831: 90                           	nop
    1832: 54                           	pushq	%rsp
    1833: 5d                           	popq	%rbp
    1834: 48 81 ec c0 04 00 00         	subq	$0x4c0, %rsp            # imm = 0x4C0
    183b: 48 89 bd 78 fb ff ff         	movq	%rdi, -0x488(%rbp)
    1842: 48 89 b5 70 fb ff ff         	movq	%rsi, -0x490(%rbp)
    1849: 48 89 95 68 fb ff ff         	movq	%rdx, -0x498(%rbp)
    1850: 48 89 8d 60 fb ff ff         	movq	%rcx, -0x4a0(%rbp)
    1857: 4c 89 85 58 fb ff ff         	movq	%r8, -0x4a8(%rbp)
    185e: 4c 89 8d 50 fb ff ff         	movq	%r9, -0x4b0(%rbp)
    1865: 48 8b 45 10                  	movq	0x10(%rbp), %rax
    1869: 48 89 85 48 fb ff ff         	movq	%rax, -0x4b8(%rbp)
    1870: 48 8b 45 18                  	movq	0x18(%rbp), %rax
    1874: 48 89 85 40 fb ff ff         	movq	%rax, -0x4c0(%rbp)
    187b: 64 48 8b 04 25 28 00 00 00   	movq	%fs:0x28, %rax
    1884: 48 89 45 f8                  	movq	%rax, -0x8(%rbp)
    1888: 29 c0                        	subl	%eax, %eax
    188a: 48 8b 85 40 fb ff ff         	movq	-0x4c0(%rbp), %rax
    1891: 48 8b 00                     	movq	(%rax), %rax
    1894: 48 09 c0                     	orq	%rax, %rax
    1897: 75 5d                        	jne	0x18f6 <request_handler+0xca>
    1899: bf 10 00 00 00               	movl	$0x10, %edi
    189e: e8 3d f9 ff ff               	callq	0x11e0 <.plt.sec+0x50>
    18a3: 48 89 85 e8 fb ff ff         	movq	%rax, -0x418(%rbp)
    18aa: 48 83 bd e8 fb ff ff 00      	cmpq	$0x0, -0x418(%rbp)
    18b2: 75 0a                        	jne	0x18be <request_handler+0x92>
    18b4: b8 00 00 00 00               	movl	$0x0, %eax
    18b9: e9 71 08 00 00               	jmp	0x212f <request_handler+0x903>
    18be: 48 8b 85 e8 fb ff ff         	movq	-0x418(%rbp), %rax
    18c5: 48 c7 00 00 00 00 00         	movq	$0x0, (%rax)
    18cc: 48 8b 85 e8 fb ff ff         	movq	-0x418(%rbp), %rax
    18d3: 48 c7 40 08 00 00 00 00      	movq	$0x0, 0x8(%rax)
    18db: 48 8b 85 40 fb ff ff         	movq	-0x4c0(%rbp), %rax
    18e2: 48 8b 95 e8 fb ff ff         	movq	-0x418(%rbp), %rdx
    18e9: 48 89 10                     	movq	%rdx, (%rax)
    18ec: b8 01 00 00 00               	movl	$0x1, %eax
    18f1: e9 39 08 00 00               	jmp	0x212f <request_handler+0x903>
    18f6: 48 8b 85 40 fb ff ff         	movq	-0x4c0(%rbp), %rax
    18fd: 48 8b 00                     	movq	(%rax), %rax
    1900: 48 89 85 a8 fb ff ff         	movq	%rax, -0x458(%rbp)
    1907: 48 8b 85 48 fb ff ff         	movq	-0x4b8(%rbp), %rax
    190e: 48 8b 00                     	movq	(%rax), %rax
    1911: 48 85 c0                     	testq	%rax, %rax
    1914: 0f 84 09 01 00 00            	je	0x1a23 <request_handler+0x1f7>
    191a: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1921: 48 8b 50 08                  	movq	0x8(%rax), %rdx
    1925: 48 8b 85 48 fb ff ff         	movq	-0x4b8(%rbp), %rax
    192c: 48 8b 00                     	movq	(%rax), %rax
    192f: 48 01 d0                     	addq	%rdx, %rax
    1932: 48 89 85 d8 fb ff ff         	movq	%rax, -0x428(%rbp)
    1939: 48 8b 85 d8 fb ff ff         	movq	-0x428(%rbp), %rax
    1940: 48 8d 50 01                  	leaq	0x1(%rax), %rdx
    1944: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    194b: 48 8b 00                     	movq	(%rax), %rax
    194e: 48 89 d6                     	movq	%rdx, %rsi
    1951: 48 89 c7                     	movq	%rax, %rdi
    1954: e8 57 f9 ff ff               	callq	0x12b0 <.plt.sec+0x120>
    1959: 48 89 85 e0 fb ff ff         	movq	%rax, -0x420(%rbp)
    1960: 48 83 bd e0 fb ff ff 00      	cmpq	$0x0, -0x420(%rbp)
    1968: 75 39                        	jne	0x19a3 <request_handler+0x177>
    196a: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1971: 48 8b 00                     	movq	(%rax), %rax
    1974: 90                           	nop
    1975: 50                           	pushq	%rax
    1976: 5f                           	popq	%rdi
    1977: e8 74 f8 ff ff               	callq	0x11f0 <.plt.sec+0x60>
    197c: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1983: 48 89 c7                     	movq	%rax, %rdi
    1986: e8 65 f8 ff ff               	callq	0x11f0 <.plt.sec+0x60>
    198b: 48 8b 85 40 fb ff ff         	movq	-0x4c0(%rbp), %rax
    1992: 48 c7 00 00 00 00 00         	movq	$0x0, (%rax)
    1999: b8 00 00 00 00               	movl	$0x0, %eax
    199e: e9 8c 07 00 00               	jmp	0x212f <request_handler+0x903>
    19a3: 48 8b 85 48 fb ff ff         	movq	-0x4b8(%rbp), %rax
    19aa: 48 8b 10                     	movq	(%rax), %rdx
    19ad: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    19b4: 48 8b 48 08                  	movq	0x8(%rax), %rcx
    19b8: 48 8b 85 e0 fb ff ff         	movq	-0x420(%rbp), %rax
    19bf: 48 01 c1                     	addq	%rax, %rcx
    19c2: 48 8b 85 50 fb ff ff         	movq	-0x4b0(%rbp), %rax
    19c9: 48 89 c6                     	movq	%rax, %rsi
    19cc: 51                           	pushq	%rcx
    19cd: 90                           	nop
    19ce: 5f                           	popq	%rdi
    19cf: e8 fc f8 ff ff               	callq	0x12d0 <.plt.sec+0x140>
    19d4: 48 8b 95 e0 fb ff ff         	movq	-0x420(%rbp), %rdx
    19db: 48 8b 85 d8 fb ff ff         	movq	-0x428(%rbp), %rax
    19e2: 48 01 d0                     	addq	%rdx, %rax
    19e5: c6 00 00                     	movb	$0x0, (%rax)
    19e8: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    19ef: 48 8b 95 e0 fb ff ff         	movq	-0x420(%rbp), %rdx
    19f6: 48 89 10                     	movq	%rdx, (%rax)
    19f9: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1a00: 48 8b 95 d8 fb ff ff         	movq	-0x428(%rbp), %rdx
    1a07: 48 89 50 08                  	movq	%rdx, 0x8(%rax)
    1a0b: 48 8b 85 48 fb ff ff         	movq	-0x4b8(%rbp), %rax
    1a12: 48 c7 00 00 00 00 00         	movq	$0x0, (%rax)
    1a19: b8 01 00 00 00               	movl	$0x1, %eax
    1a1e: e9 0c 07 00 00               	jmp	0x212f <request_handler+0x903>
    1a23: 48 c7 85 f0 fb ff ff 00 00 00 00     	movq	$0x0, -0x410(%rbp)
    1a2e: 48 c7 85 f8 fb ff ff 00 00 00 00     	movq	$0x0, -0x408(%rbp)
    1a39: 48 8d 95 00 fc ff ff         	leaq	-0x400(%rbp), %rdx
    1a40: b8 00 00 00 00               	movl	$0x0, %eax
    1a45: b9 7e 00 00 00               	movl	$0x7e, %ecx
    1a4a: 52                           	pushq	%rdx
    1a4b: 5f                           	popq	%rdi
    1a4c: 90                           	nop
    1a4d: f3 48 ab                     	rep		stosq	%rax, %es:(%rdi)
    1a50: c7 85 84 fb ff ff c8 00 00 00	movl	$0xc8, -0x47c(%rbp)
    1a5a: 48 8b 85 60 fb ff ff         	movq	-0x4a0(%rbp), %rax
    1a61: 48 8d 15 b6 15 00 00         	leaq	0x15b6(%rip), %rdx      # 0x301e <_IO_stdin_used+0x1e>
    1a68: 52                           	pushq	%rdx
    1a69: 90                           	nop
    1a6a: 5e                           	popq	%rsi
    1a6b: 90                           	nop
    1a6c: 50                           	pushq	%rax
    1a6d: 5f                           	popq	%rdi
    1a6e: e8 ed f7 ff ff               	callq	0x1260 <.plt.sec+0xd0>
    1a73: 09 c0                        	orl	%eax, %eax
    1a75: 0f 85 28 01 00 00            	jne	0x1ba3 <request_handler+0x377>
    1a7b: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1a82: 48 8d 15 99 15 00 00         	leaq	0x1599(%rip), %rdx      # 0x3022 <_IO_stdin_used+0x22>
    1a89: 52                           	pushq	%rdx
    1a8a: 90                           	nop
    1a8b: 5e                           	popq	%rsi
    1a8c: 50                           	pushq	%rax
    1a8d: 90                           	nop
    1a8e: 5f                           	popq	%rdi
    1a8f: e8 cc f7 ff ff               	callq	0x1260 <.plt.sec+0xd0>
    1a94: 85 c0                        	testl	%eax, %eax
    1a96: 75 19                        	jne	0x1ab1 <request_handler+0x285>
    1a98: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1a9f: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1aa4: 50                           	pushq	%rax
    1aa5: 90                           	nop
    1aa6: 5f                           	popq	%rdi
    1aa7: e8 22 fc ff ff               	callq	0x16ce <list_items_str>
    1aac: e9 d7 05 00 00               	jmp	0x2088 <request_handler+0x85c>
    1ab1: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1ab8: ba 07 00 00 00               	movl	$0x7, %edx
    1abd: 48 8d 0d 65 15 00 00         	leaq	0x1565(%rip), %rcx      # 0x3029 <_IO_stdin_used+0x29>
    1ac4: 48 89 ce                     	movq	%rcx, %rsi
    1ac7: 48 89 c7                     	movq	%rax, %rdi
    1aca: e8 01 f7 ff ff               	callq	0x11d0 <.plt.sec+0x40>
    1acf: 09 c0                        	orl	%eax, %eax
    1ad1: 0f 85 9d 00 00 00            	jne	0x1b74 <request_handler+0x348>
    1ad7: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1ade: 48 83 c0 07                  	addq	$0x7, %rax
    1ae2: 50                           	pushq	%rax
    1ae3: 90                           	nop
    1ae4: 5f                           	popq	%rdi
    1ae5: e8 36 f7 ff ff               	callq	0x1220 <.plt.sec+0x90>
    1aea: 89 85 a0 fb ff ff            	movl	%eax, -0x460(%rbp)
    1af0: 8b 85 a0 fb ff ff            	movl	-0x460(%rbp), %eax
    1af6: 89 c7                        	movl	%eax, %edi
    1af8: e8 a3 fa ff ff               	callq	0x15a0 <get_item_data>
    1afd: 48 89 85 c8 fb ff ff         	movq	%rax, -0x438(%rbp)
    1b04: 48 83 bd c8 fb ff ff 00      	cmpq	$0x0, -0x438(%rbp)
    1b0c: 74 37                        	je	0x1b45 <request_handler+0x319>
    1b0e: 48 8b 8d c8 fb ff ff         	movq	-0x438(%rbp), %rcx
    1b15: 8b 95 a0 fb ff ff            	movl	-0x460(%rbp), %edx
    1b1b: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1b22: 49 89 c8                     	movq	%rcx, %r8
    1b25: 89 d1                        	movl	%edx, %ecx
    1b27: 48 8d 15 03 15 00 00         	leaq	0x1503(%rip), %rdx      # 0x3031 <_IO_stdin_used+0x31>
    1b2e: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1b33: 50                           	pushq	%rax
    1b34: 90                           	nop
    1b35: 5f                           	popq	%rdi
    1b36: b8 00 00 00 00               	movl	$0x0, %eax
    1b3b: e8 60 f6 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1b40: e9 43 05 00 00               	jmp	0x2088 <request_handler+0x85c>
    1b45: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1b4c: 48 8d 15 ef 14 00 00         	leaq	0x14ef(%rip), %rdx      # 0x3042 <_IO_stdin_used+0x42>
    1b53: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1b58: 50                           	pushq	%rax
    1b59: 90                           	nop
    1b5a: 5f                           	popq	%rdi
    1b5b: b8 00 00 00 00               	movl	$0x0, %eax
    1b60: e8 3b f6 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1b65: c7 85 84 fb ff ff 94 01 00 00	movl	$0x194, -0x47c(%rbp)    # imm = 0x194
    1b6f: e9 14 05 00 00               	jmp	0x2088 <request_handler+0x85c>
    1b74: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1b7b: 48 8d 15 cf 14 00 00         	leaq	0x14cf(%rip), %rdx      # 0x3051 <_IO_stdin_used+0x51>
    1b82: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1b87: 48 89 c7                     	movq	%rax, %rdi
    1b8a: b8 00 00 00 00               	movl	$0x0, %eax
    1b8f: e8 0c f6 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1b94: c7 85 84 fb ff ff 94 01 00 00	movl	$0x194, -0x47c(%rbp)    # imm = 0x194
    1b9e: e9 e5 04 00 00               	jmp	0x2088 <request_handler+0x85c>
    1ba3: 48 8b 85 60 fb ff ff         	movq	-0x4a0(%rbp), %rax
    1baa: 48 8d 15 aa 14 00 00         	leaq	0x14aa(%rip), %rdx      # 0x305b <_IO_stdin_used+0x5b>
    1bb1: 52                           	pushq	%rdx
    1bb2: 5e                           	popq	%rsi
    1bb3: 90                           	nop
    1bb4: 48 89 c7                     	movq	%rax, %rdi
    1bb7: e8 a4 f6 ff ff               	callq	0x1260 <.plt.sec+0xd0>
    1bbc: 85 c0                        	testl	%eax, %eax
    1bbe: 0f 85 f2 01 00 00            	jne	0x1db6 <request_handler+0x58a>
    1bc4: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1bcb: 48 8d 15 50 14 00 00         	leaq	0x1450(%rip), %rdx      # 0x3022 <_IO_stdin_used+0x22>
    1bd2: 52                           	pushq	%rdx
    1bd3: 5e                           	popq	%rsi
    1bd4: 90                           	nop
    1bd5: 50                           	pushq	%rax
    1bd6: 90                           	nop
    1bd7: 5f                           	popq	%rdi
    1bd8: e8 83 f6 ff ff               	callq	0x1260 <.plt.sec+0xd0>
    1bdd: 09 c0                        	orl	%eax, %eax
    1bdf: 0f 85 a2 01 00 00            	jne	0x1d87 <request_handler+0x55b>
    1be5: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1bec: 48 8b 00                     	movq	(%rax), %rax
    1bef: 48 85 c0                     	testq	%rax, %rax
    1bf2: 75 2f                        	jne	0x1c23 <request_handler+0x3f7>
    1bf4: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1bfb: 48 8d 15 5e 14 00 00         	leaq	0x145e(%rip), %rdx      # 0x3060 <_IO_stdin_used+0x60>
    1c02: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1c07: 48 89 c7                     	movq	%rax, %rdi
    1c0a: b8 00 00 00 00               	movl	$0x0, %eax
    1c0f: e8 8c f5 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1c14: c7 85 84 fb ff ff 90 01 00 00	movl	$0x190, -0x47c(%rbp)    # imm = 0x190
    1c1e: e9 65 04 00 00               	jmp	0x2088 <request_handler+0x85c>
    1c23: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1c2a: 48 8b 00                     	movq	(%rax), %rax
    1c2d: 48 8d 15 39 14 00 00         	leaq	0x1439(%rip), %rdx      # 0x306d <_IO_stdin_used+0x6d>
    1c34: 48 89 d6                     	movq	%rdx, %rsi
    1c37: 50                           	pushq	%rax
    1c38: 90                           	nop
    1c39: 5f                           	popq	%rdi
    1c3a: e8 d1 f5 ff ff               	callq	0x1210 <.plt.sec+0x80>
    1c3f: 48 89 85 b8 fb ff ff         	movq	%rax, -0x448(%rbp)
    1c46: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1c4d: 48 8b 00                     	movq	(%rax), %rax
    1c50: 48 8d 15 1a 14 00 00         	leaq	0x141a(%rip), %rdx      # 0x3071 <_IO_stdin_used+0x71>
    1c57: 52                           	pushq	%rdx
    1c58: 5e                           	popq	%rsi
    1c59: 90                           	nop
    1c5a: 48 89 c7                     	movq	%rax, %rdi
    1c5d: e8 ae f5 ff ff               	callq	0x1210 <.plt.sec+0x80>
    1c62: 48 89 85 c0 fb ff ff         	movq	%rax, -0x440(%rbp)
    1c69: 48 83 bd b8 fb ff ff 00      	cmpq	$0x0, -0x448(%rbp)
    1c71: 0f 84 e1 00 00 00            	je	0x1d58 <request_handler+0x52c>
    1c77: 48 83 bd c0 fb ff ff 00      	cmpq	$0x0, -0x440(%rbp)
    1c7f: 0f 84 d3 00 00 00            	je	0x1d58 <request_handler+0x52c>
    1c85: 48 8b 85 b8 fb ff ff         	movq	-0x448(%rbp), %rax
    1c8c: 48 83 c0 03                  	addq	$0x3, %rax
    1c90: 48 89 c7                     	movq	%rax, %rdi
    1c93: e8 88 f5 ff ff               	callq	0x1220 <.plt.sec+0x90>
    1c98: 89 85 98 fb ff ff            	movl	%eax, -0x468(%rbp)
    1c9e: 48 83 85 c0 fb ff ff 05      	addq	$0x5, -0x440(%rbp)
    1ca6: 48 8b 95 c0 fb ff ff         	movq	-0x440(%rbp), %rdx
    1cad: 8b 85 98 fb ff ff            	movl	-0x468(%rbp), %eax
    1cb3: 48 89 d6                     	movq	%rdx, %rsi
    1cb6: 89 c7                        	movl	%eax, %edi
    1cb8: e8 c5 f7 ff ff               	callq	0x1482 <add_item>
    1cbd: 89 85 9c fb ff ff            	movl	%eax, -0x464(%rbp)
    1cc3: 83 bd 9c fb ff ff 00         	cmpl	$0x0, -0x464(%rbp)
    1cca: 75 25                        	jne	0x1cf1 <request_handler+0x4c5>
    1ccc: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1cd3: 48 8d 15 9d 13 00 00         	leaq	0x139d(%rip), %rdx      # 0x3077 <_IO_stdin_used+0x77>
    1cda: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1cdf: 50                           	pushq	%rax
    1ce0: 5f                           	popq	%rdi
    1ce1: 90                           	nop
    1ce2: b8 00 00 00 00               	movl	$0x0, %eax
    1ce7: e8 b4 f4 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1cec: e9 97 03 00 00               	jmp	0x2088 <request_handler+0x85c>
    1cf1: 83 bd 9c fb ff ff ff         	cmpl	$-0x1, -0x464(%rbp)
    1cf8: 75 2f                        	jne	0x1d29 <request_handler+0x4fd>
    1cfa: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1d01: 48 8d 15 7a 13 00 00         	leaq	0x137a(%rip), %rdx      # 0x3082 <_IO_stdin_used+0x82>
    1d08: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1d0d: 50                           	pushq	%rax
    1d0e: 5f                           	popq	%rdi
    1d0f: 90                           	nop
    1d10: b8 00 00 00 00               	movl	$0x0, %eax
    1d15: e8 86 f4 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1d1a: c7 85 84 fb ff ff 90 01 00 00	movl	$0x190, -0x47c(%rbp)    # imm = 0x190
    1d24: e9 5f 03 00 00               	jmp	0x2088 <request_handler+0x85c>
    1d29: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1d30: 48 8d 15 5f 13 00 00         	leaq	0x135f(%rip), %rdx      # 0x3096 <_IO_stdin_used+0x96>
    1d37: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1d3c: 50                           	pushq	%rax
    1d3d: 90                           	nop
    1d3e: 5f                           	popq	%rdi
    1d3f: b8 00 00 00 00               	movl	$0x0, %eax
    1d44: e8 57 f4 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1d49: c7 85 84 fb ff ff f7 01 00 00	movl	$0x1f7, -0x47c(%rbp)    # imm = 0x1F7
    1d53: e9 30 03 00 00               	jmp	0x2088 <request_handler+0x85c>
    1d58: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1d5f: 48 8d 15 fa 12 00 00         	leaq	0x12fa(%rip), %rdx      # 0x3060 <_IO_stdin_used+0x60>
    1d66: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1d6b: 90                           	nop
    1d6c: 50                           	pushq	%rax
    1d6d: 5f                           	popq	%rdi
    1d6e: b8 00 00 00 00               	movl	$0x0, %eax
    1d73: e8 28 f4 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1d78: c7 85 84 fb ff ff 90 01 00 00	movl	$0x190, -0x47c(%rbp)    # imm = 0x190
    1d82: e9 01 03 00 00               	jmp	0x2088 <request_handler+0x85c>
    1d87: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1d8e: 48 8d 15 bc 12 00 00         	leaq	0x12bc(%rip), %rdx      # 0x3051 <_IO_stdin_used+0x51>
    1d95: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1d9a: 50                           	pushq	%rax
    1d9b: 90                           	nop
    1d9c: 5f                           	popq	%rdi
    1d9d: b8 00 00 00 00               	movl	$0x0, %eax
    1da2: e8 f9 f3 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1da7: c7 85 84 fb ff ff 94 01 00 00	movl	$0x194, -0x47c(%rbp)    # imm = 0x194
    1db1: e9 d2 02 00 00               	jmp	0x2088 <request_handler+0x85c>
    1db6: 48 8b 85 60 fb ff ff         	movq	-0x4a0(%rbp), %rax
    1dbd: 48 8d 15 dd 12 00 00         	leaq	0x12dd(%rip), %rdx      # 0x30a1 <_IO_stdin_used+0xa1>
    1dc4: 52                           	pushq	%rdx
    1dc5: 90                           	nop
    1dc6: 5e                           	popq	%rsi
    1dc7: 50                           	pushq	%rax
    1dc8: 5f                           	popq	%rdi
    1dc9: 90                           	nop
    1dca: e8 91 f4 ff ff               	callq	0x1260 <.plt.sec+0xd0>
    1dcf: 85 c0                        	testl	%eax, %eax
    1dd1: 0f 85 8e 01 00 00            	jne	0x1f65 <request_handler+0x739>
    1dd7: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1dde: ba 07 00 00 00               	movl	$0x7, %edx
    1de3: 48 8d 0d 3f 12 00 00         	leaq	0x123f(%rip), %rcx      # 0x3029 <_IO_stdin_used+0x29>
    1dea: 90                           	nop
    1deb: 51                           	pushq	%rcx
    1dec: 5e                           	popq	%rsi
    1ded: 50                           	pushq	%rax
    1dee: 5f                           	popq	%rdi
    1def: 90                           	nop
    1df0: e8 db f3 ff ff               	callq	0x11d0 <.plt.sec+0x40>
    1df5: 85 c0                        	testl	%eax, %eax
    1df7: 0f 85 39 01 00 00            	jne	0x1f36 <request_handler+0x70a>
    1dfd: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1e04: 48 83 c0 07                  	addq	$0x7, %rax
    1e08: 50                           	pushq	%rax
    1e09: 90                           	nop
    1e0a: 5f                           	popq	%rdi
    1e0b: e8 10 f4 ff ff               	callq	0x1220 <.plt.sec+0x90>
    1e10: 89 85 90 fb ff ff            	movl	%eax, -0x470(%rbp)
    1e16: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1e1d: 48 8b 00                     	movq	(%rax), %rax
    1e20: 48 85 c0                     	testq	%rax, %rax
    1e23: 75 2f                        	jne	0x1e54 <request_handler+0x628>
    1e25: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1e2c: 48 8d 15 2d 12 00 00         	leaq	0x122d(%rip), %rdx      # 0x3060 <_IO_stdin_used+0x60>
    1e33: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1e38: 48 89 c7                     	movq	%rax, %rdi
    1e3b: b8 00 00 00 00               	movl	$0x0, %eax
    1e40: e8 5b f3 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1e45: c7 85 84 fb ff ff 90 01 00 00	movl	$0x190, -0x47c(%rbp)    # imm = 0x190
    1e4f: e9 34 02 00 00               	jmp	0x2088 <request_handler+0x85c>
    1e54: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    1e5b: 48 8b 00                     	movq	(%rax), %rax
    1e5e: 48 8d 15 0c 12 00 00         	leaq	0x120c(%rip), %rdx      # 0x3071 <_IO_stdin_used+0x71>
    1e65: 48 89 d6                     	movq	%rdx, %rsi
    1e68: 50                           	pushq	%rax
    1e69: 5f                           	popq	%rdi
    1e6a: 90                           	nop
    1e6b: e8 a0 f3 ff ff               	callq	0x1210 <.plt.sec+0x80>
    1e70: 48 89 85 b0 fb ff ff         	movq	%rax, -0x450(%rbp)
    1e77: 48 83 bd b0 fb ff ff 00      	cmpq	$0x0, -0x450(%rbp)
    1e7f: 0f 84 82 00 00 00            	je	0x1f07 <request_handler+0x6db>
    1e85: 48 83 85 b0 fb ff ff 05      	addq	$0x5, -0x450(%rbp)
    1e8d: 48 8b 95 b0 fb ff ff         	movq	-0x450(%rbp), %rdx
    1e94: 8b 85 90 fb ff ff            	movl	-0x470(%rbp), %eax
    1e9a: 52                           	pushq	%rdx
    1e9b: 90                           	nop
    1e9c: 5e                           	popq	%rsi
    1e9d: 89 c7                        	movl	%eax, %edi
    1e9f: e8 49 f7 ff ff               	callq	0x15ed <update_item>
    1ea4: 89 85 94 fb ff ff            	movl	%eax, -0x46c(%rbp)
    1eaa: 83 bd 94 fb ff ff 00         	cmpl	$0x0, -0x46c(%rbp)
    1eb1: 75 25                        	jne	0x1ed8 <request_handler+0x6ac>
    1eb3: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1eba: 48 8d 15 e4 11 00 00         	leaq	0x11e4(%rip), %rdx      # 0x30a5 <_IO_stdin_used+0xa5>
    1ec1: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1ec6: 48 89 c7                     	movq	%rax, %rdi
    1ec9: b8 00 00 00 00               	movl	$0x0, %eax
    1ece: e8 cd f2 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1ed3: e9 b0 01 00 00               	jmp	0x2088 <request_handler+0x85c>
    1ed8: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1edf: 48 8d 15 5c 11 00 00         	leaq	0x115c(%rip), %rdx      # 0x3042 <_IO_stdin_used+0x42>
    1ee6: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1eeb: 48 89 c7                     	movq	%rax, %rdi
    1eee: b8 00 00 00 00               	movl	$0x0, %eax
    1ef3: e8 a8 f2 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1ef8: c7 85 84 fb ff ff 94 01 00 00	movl	$0x194, -0x47c(%rbp)    # imm = 0x194
    1f02: e9 81 01 00 00               	jmp	0x2088 <request_handler+0x85c>
    1f07: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1f0e: 48 8d 15 4b 11 00 00         	leaq	0x114b(%rip), %rdx      # 0x3060 <_IO_stdin_used+0x60>
    1f15: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1f1a: 50                           	pushq	%rax
    1f1b: 90                           	nop
    1f1c: 5f                           	popq	%rdi
    1f1d: b8 00 00 00 00               	movl	$0x0, %eax
    1f22: e8 79 f2 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1f27: c7 85 84 fb ff ff 90 01 00 00	movl	$0x190, -0x47c(%rbp)    # imm = 0x190
    1f31: e9 52 01 00 00               	jmp	0x2088 <request_handler+0x85c>
    1f36: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1f3d: 48 8d 15 0d 11 00 00         	leaq	0x110d(%rip), %rdx      # 0x3051 <_IO_stdin_used+0x51>
    1f44: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1f49: 50                           	pushq	%rax
    1f4a: 5f                           	popq	%rdi
    1f4b: 90                           	nop
    1f4c: b8 00 00 00 00               	movl	$0x0, %eax
    1f51: e8 4a f2 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    1f56: c7 85 84 fb ff ff 94 01 00 00	movl	$0x194, -0x47c(%rbp)    # imm = 0x194
    1f60: e9 23 01 00 00               	jmp	0x2088 <request_handler+0x85c>
    1f65: 48 8b 85 60 fb ff ff         	movq	-0x4a0(%rbp), %rax
    1f6c: 48 8d 15 3f 11 00 00         	leaq	0x113f(%rip), %rdx      # 0x30b2 <_IO_stdin_used+0xb2>
    1f73: 52                           	pushq	%rdx
    1f74: 90                           	nop
    1f75: 5e                           	popq	%rsi
    1f76: 50                           	pushq	%rax
    1f77: 90                           	nop
    1f78: 5f                           	popq	%rdi
    1f79: e8 e2 f2 ff ff               	callq	0x1260 <.plt.sec+0xd0>
    1f7e: 85 c0                        	testl	%eax, %eax
    1f80: 0f 85 d8 00 00 00            	jne	0x205e <request_handler+0x832>
    1f86: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1f8d: ba 07 00 00 00               	movl	$0x7, %edx
    1f92: 48 8d 0d 90 10 00 00         	leaq	0x1090(%rip), %rcx      # 0x3029 <_IO_stdin_used+0x29>
    1f99: 51                           	pushq	%rcx
    1f9a: 5e                           	popq	%rsi
    1f9b: 90                           	nop
    1f9c: 90                           	nop
    1f9d: 50                           	pushq	%rax
    1f9e: 5f                           	popq	%rdi
    1f9f: e8 2c f2 ff ff               	callq	0x11d0 <.plt.sec+0x40>
    1fa4: 09 c0                        	orl	%eax, %eax
    1fa6: 0f 85 86 00 00 00            	jne	0x2032 <request_handler+0x806>
    1fac: 48 8b 85 68 fb ff ff         	movq	-0x498(%rbp), %rax
    1fb3: 48 83 c0 07                  	addq	$0x7, %rax
    1fb7: 90                           	nop
    1fb8: 50                           	pushq	%rax
    1fb9: 5f                           	popq	%rdi
    1fba: e8 61 f2 ff ff               	callq	0x1220 <.plt.sec+0x90>
    1fbf: 89 85 88 fb ff ff            	movl	%eax, -0x478(%rbp)
    1fc5: 8b 85 88 fb ff ff            	movl	-0x478(%rbp), %eax
    1fcb: 89 c7                        	movl	%eax, %edi
    1fcd: e8 a7 f6 ff ff               	callq	0x1679 <delete_item>
    1fd2: 89 85 8c fb ff ff            	movl	%eax, -0x474(%rbp)
    1fd8: 83 bd 8c fb ff ff 00         	cmpl	$0x0, -0x474(%rbp)
    1fdf: 75 25                        	jne	0x2006 <request_handler+0x7da>
    1fe1: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    1fe8: 48 8d 15 ca 10 00 00         	leaq	0x10ca(%rip), %rdx      # 0x30b9 <_IO_stdin_used+0xb9>
    1fef: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    1ff4: 50                           	pushq	%rax
    1ff5: 90                           	nop
    1ff6: 5f                           	popq	%rdi
    1ff7: b8 00 00 00 00               	movl	$0x0, %eax
    1ffc: e8 9f f1 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    2001: e9 82 00 00 00               	jmp	0x2088 <request_handler+0x85c>
    2006: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    200d: 48 8d 15 2e 10 00 00         	leaq	0x102e(%rip), %rdx      # 0x3042 <_IO_stdin_used+0x42>
    2014: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    2019: 48 89 c7                     	movq	%rax, %rdi
    201c: b8 00 00 00 00               	movl	$0x0, %eax
    2021: e8 7a f1 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    2026: c7 85 84 fb ff ff 94 01 00 00	movl	$0x194, -0x47c(%rbp)    # imm = 0x194
    2030: eb 56                        	jmp	0x2088 <request_handler+0x85c>
    2032: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    2039: 48 8d 15 11 10 00 00         	leaq	0x1011(%rip), %rdx      # 0x3051 <_IO_stdin_used+0x51>
    2040: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    2045: 90                           	nop
    2046: 50                           	pushq	%rax
    2047: 5f                           	popq	%rdi
    2048: b8 00 00 00 00               	movl	$0x0, %eax
    204d: e8 4e f1 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    2052: c7 85 84 fb ff ff 94 01 00 00	movl	$0x194, -0x47c(%rbp)    # imm = 0x194
    205c: eb 2a                        	jmp	0x2088 <request_handler+0x85c>
    205e: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    2065: 48 8d 15 5a 10 00 00         	leaq	0x105a(%rip), %rdx      # 0x30c6 <_IO_stdin_used+0xc6>
    206c: be 00 04 00 00               	movl	$0x400, %esi            # imm = 0x400
    2071: 50                           	pushq	%rax
    2072: 5f                           	popq	%rdi
    2073: 90                           	nop
    2074: b8 00 00 00 00               	movl	$0x0, %eax
    2079: e8 22 f1 ff ff               	callq	0x11a0 <.plt.sec+0x10>
    207e: c7 85 84 fb ff ff 95 01 00 00	movl	$0x195, -0x47c(%rbp)    # imm = 0x195
    2088: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    208f: 90                           	nop
    2090: 50                           	pushq	%rax
    2091: 5f                           	popq	%rdi
    2092: e8 69 f1 ff ff               	callq	0x1200 <.plt.sec+0x70>
    2097: 50                           	pushq	%rax
    2098: 59                           	popq	%rcx
    2099: 90                           	nop
    209a: 48 8d 85 f0 fb ff ff         	leaq	-0x410(%rbp), %rax
    20a1: ba 02 00 00 00               	movl	$0x2, %edx
    20a6: 50                           	pushq	%rax
    20a7: 90                           	nop
    20a8: 5e                           	popq	%rsi
    20a9: 48 89 cf                     	movq	%rcx, %rdi
    20ac: e8 bf f1 ff ff               	callq	0x1270 <.plt.sec+0xe0>
    20b1: 48 89 85 d0 fb ff ff         	movq	%rax, -0x430(%rbp)
    20b8: 8b 8d 84 fb ff ff            	movl	-0x47c(%rbp), %ecx
    20be: 48 8b 95 d0 fb ff ff         	movq	-0x430(%rbp), %rdx
    20c5: 48 8b 85 70 fb ff ff         	movq	-0x490(%rbp), %rax
    20cc: 89 ce                        	movl	%ecx, %esi
    20ce: 50                           	pushq	%rax
    20cf: 5f                           	popq	%rdi
    20d0: 90                           	nop
    20d1: e8 ea f0 ff ff               	callq	0x11c0 <.plt.sec+0x30>
    20d6: 89 85 a4 fb ff ff            	movl	%eax, -0x45c(%rbp)
    20dc: 48 8b 85 d0 fb ff ff         	movq	-0x430(%rbp), %rax
    20e3: 50                           	pushq	%rax
    20e4: 5f                           	popq	%rdi
    20e5: 90                           	nop
    20e6: e8 a5 f1 ff ff               	callq	0x1290 <.plt.sec+0x100>
    20eb: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    20f2: 48 8b 00                     	movq	(%rax), %rax
    20f5: 48 85 c0                     	testq	%rax, %rax
    20f8: 74 12                        	je	0x210c <request_handler+0x8e0>
    20fa: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    2101: 48 8b 00                     	movq	(%rax), %rax
    2104: 50                           	pushq	%rax
    2105: 90                           	nop
    2106: 5f                           	popq	%rdi
    2107: e8 e4 f0 ff ff               	callq	0x11f0 <.plt.sec+0x60>
    210c: 48 8b 85 a8 fb ff ff         	movq	-0x458(%rbp), %rax
    2113: 48 89 c7                     	movq	%rax, %rdi
    2116: e8 d5 f0 ff ff               	callq	0x11f0 <.plt.sec+0x60>
    211b: 48 8b 85 40 fb ff ff         	movq	-0x4c0(%rbp), %rax
    2122: 48 c7 00 00 00 00 00         	movq	$0x0, (%rax)
    2129: 8b 85 a4 fb ff ff            	movl	-0x45c(%rbp), %eax
    212f: 48 8b 55 f8                  	movq	-0x8(%rbp), %rdx
    2133: 64 48 2b 14 25 28 00 00 00   	subq	%fs:0x28, %rdx
    213c: 74 05                        	je	0x2143 <request_handler+0x917>
    213e: e8 0d f1 ff ff               	callq	0x1250 <.plt.sec+0xc0>
    2143: c9                           	leave
    2144: c3                           	retq

0000000000002145 <main>:
    2145: f3 0f 1e fa                  	endbr64
    2149: 55                           	pushq	%rbp
    214a: 48 89 e5                     	movq	%rsp, %rbp
    214d: 48 83 ec 10                  	subq	$0x10, %rsp
    2151: b8 00 00 00 00               	movl	$0x0, %eax
    2156: e8 6e f2 ff ff               	callq	0x13c9 <init_store>
    215b: 48 83 ec 08                  	subq	$0x8, %rsp
    215f: 6a 00                        	pushq	$0x0
    2161: 41 b9 00 00 00 00            	movl	$0x0, %r9d
    2167: 4c 8d 05 be f6 ff ff         	leaq	-0x942(%rip), %r8       # 0x182c <request_handler>
    216e: b9 00 00 00 00               	movl	$0x0, %ecx
    2173: ba 00 00 00 00               	movl	$0x0, %edx
    2178: be b8 22 00 00               	movl	$0x22b8, %esi           # imm = 0x22B8
    217d: bf 08 00 00 00               	movl	$0x8, %edi
    2182: b8 00 00 00 00               	movl	$0x0, %eax
    2187: e8 a4 f0 ff ff               	callq	0x1230 <.plt.sec+0xa0>
    218c: 48 83 c4 10                  	addq	$0x10, %rsp
    2190: 48 89 45 f8                  	movq	%rax, -0x8(%rbp)
    2194: 48 83 7d f8 00               	cmpq	$0x0, -0x8(%rbp)
    2199: 75 2a                        	jne	0x21c5 <main+0x80>
    219b: 48 8b 05 7e 2e 00 00         	movq	0x2e7e(%rip), %rax      # 0x5020 <stderr@GLIBC_2.2.5>
    21a2: 50                           	pushq	%rax
    21a3: 59                           	popq	%rcx
    21a4: 90                           	nop
    21a5: ba 17 00 00 00               	movl	$0x17, %edx
    21aa: be 01 00 00 00               	movl	$0x1, %esi
    21af: 48 8d 05 23 0f 00 00         	leaq	0xf23(%rip), %rax       # 0x30d9 <_IO_stdin_used+0xd9>
    21b6: 90                           	nop
    21b7: 50                           	pushq	%rax
    21b8: 5f                           	popq	%rdi
    21b9: e8 e2 f0 ff ff               	callq	0x12a0 <.plt.sec+0x110>
    21be: b8 01 00 00 00               	movl	$0x1, %eax
    21c3: eb 2f                        	jmp	0x21f4 <main+0xaf>
    21c5: be b8 22 00 00               	movl	$0x22b8, %esi           # imm = 0x22B8
    21ca: 48 8d 05 20 0f 00 00         	leaq	0xf20(%rip), %rax       # 0x30f1 <_IO_stdin_used+0xf1>
    21d1: 48 89 c7                     	movq	%rax, %rdi
    21d4: b8 00 00 00 00               	movl	$0x0, %eax
    21d9: e8 b2 ef ff ff               	callq	0x1190 <.plt.sec>
    21de: e8 5d f0 ff ff               	callq	0x1240 <.plt.sec+0xb0>
    21e3: 48 8b 45 f8                  	movq	-0x8(%rbp), %rax
    21e7: 90                           	nop
    21e8: 50                           	pushq	%rax
    21e9: 5f                           	popq	%rdi
    21ea: e8 d1 f0 ff ff               	callq	0x12c0 <.plt.sec+0x130>
    21ef: b8 00 00 00 00               	movl	$0x0, %eax
    21f4: c9                           	leave
    21f5: c3                           	retq

Disassembly of section .fini:

00000000000021f8 <_fini>:
    21f8: f3 0f 1e fa                  	endbr64
    21fc: 48 83 ec 08                  	subq	$0x8, %rsp
    2200: 48 83 c4 08                  	addq	$0x8, %rsp
    2204: c3                           	retq
