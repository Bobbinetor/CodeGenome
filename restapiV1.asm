
restapiV1:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    $0x8,%rsp
    1008:	48 8b 05 c9 3f 00 00 	mov    0x3fc9(%rip),%rax        # 4fd8 <__gmon_start__@Base>
    100f:	48 85 c0             	test   %rax,%rax
    1012:	74 02                	je     1016 <_init+0x16>
    1014:	ff d0                	call   *%rax
    1016:	48 83 c4 08          	add    $0x8,%rsp
    101a:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:	ff 35 f2 3e 00 00    	push   0x3ef2(%rip)        # 4f18 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:	f2 ff 25 f3 3e 00 00 	bnd jmp *0x3ef3(%rip)        # 4f20 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:	0f 1f 00             	nopl   (%rax)
    1030:	f3 0f 1e fa          	endbr64 
    1034:	68 00 00 00 00       	push   $0x0
    1039:	f2 e9 e1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    103f:	90                   	nop
    1040:	f3 0f 1e fa          	endbr64 
    1044:	68 01 00 00 00       	push   $0x1
    1049:	f2 e9 d1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    104f:	90                   	nop
    1050:	f3 0f 1e fa          	endbr64 
    1054:	68 02 00 00 00       	push   $0x2
    1059:	f2 e9 c1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    105f:	90                   	nop
    1060:	f3 0f 1e fa          	endbr64 
    1064:	68 03 00 00 00       	push   $0x3
    1069:	f2 e9 b1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    106f:	90                   	nop
    1070:	f3 0f 1e fa          	endbr64 
    1074:	68 04 00 00 00       	push   $0x4
    1079:	f2 e9 a1 ff ff ff    	bnd jmp 1020 <_init+0x20>
    107f:	90                   	nop
    1080:	f3 0f 1e fa          	endbr64 
    1084:	68 05 00 00 00       	push   $0x5
    1089:	f2 e9 91 ff ff ff    	bnd jmp 1020 <_init+0x20>
    108f:	90                   	nop
    1090:	f3 0f 1e fa          	endbr64 
    1094:	68 06 00 00 00       	push   $0x6
    1099:	f2 e9 81 ff ff ff    	bnd jmp 1020 <_init+0x20>
    109f:	90                   	nop
    10a0:	f3 0f 1e fa          	endbr64 
    10a4:	68 07 00 00 00       	push   $0x7
    10a9:	f2 e9 71 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10af:	90                   	nop
    10b0:	f3 0f 1e fa          	endbr64 
    10b4:	68 08 00 00 00       	push   $0x8
    10b9:	f2 e9 61 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10bf:	90                   	nop
    10c0:	f3 0f 1e fa          	endbr64 
    10c4:	68 09 00 00 00       	push   $0x9
    10c9:	f2 e9 51 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10cf:	90                   	nop
    10d0:	f3 0f 1e fa          	endbr64 
    10d4:	68 0a 00 00 00       	push   $0xa
    10d9:	f2 e9 41 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10df:	90                   	nop
    10e0:	f3 0f 1e fa          	endbr64 
    10e4:	68 0b 00 00 00       	push   $0xb
    10e9:	f2 e9 31 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10ef:	90                   	nop
    10f0:	f3 0f 1e fa          	endbr64 
    10f4:	68 0c 00 00 00       	push   $0xc
    10f9:	f2 e9 21 ff ff ff    	bnd jmp 1020 <_init+0x20>
    10ff:	90                   	nop
    1100:	f3 0f 1e fa          	endbr64 
    1104:	68 0d 00 00 00       	push   $0xd
    1109:	f2 e9 11 ff ff ff    	bnd jmp 1020 <_init+0x20>
    110f:	90                   	nop
    1110:	f3 0f 1e fa          	endbr64 
    1114:	68 0e 00 00 00       	push   $0xe
    1119:	f2 e9 01 ff ff ff    	bnd jmp 1020 <_init+0x20>
    111f:	90                   	nop
    1120:	f3 0f 1e fa          	endbr64 
    1124:	68 0f 00 00 00       	push   $0xf
    1129:	f2 e9 f1 fe ff ff    	bnd jmp 1020 <_init+0x20>
    112f:	90                   	nop
    1130:	f3 0f 1e fa          	endbr64 
    1134:	68 10 00 00 00       	push   $0x10
    1139:	f2 e9 e1 fe ff ff    	bnd jmp 1020 <_init+0x20>
    113f:	90                   	nop
    1140:	f3 0f 1e fa          	endbr64 
    1144:	68 11 00 00 00       	push   $0x11
    1149:	f2 e9 d1 fe ff ff    	bnd jmp 1020 <_init+0x20>
    114f:	90                   	nop
    1150:	f3 0f 1e fa          	endbr64 
    1154:	68 12 00 00 00       	push   $0x12
    1159:	f2 e9 c1 fe ff ff    	bnd jmp 1020 <_init+0x20>
    115f:	90                   	nop
    1160:	f3 0f 1e fa          	endbr64 
    1164:	68 13 00 00 00       	push   $0x13
    1169:	f2 e9 b1 fe ff ff    	bnd jmp 1020 <_init+0x20>
    116f:	90                   	nop
    1170:	f3 0f 1e fa          	endbr64 
    1174:	68 14 00 00 00       	push   $0x14
    1179:	f2 e9 a1 fe ff ff    	bnd jmp 1020 <_init+0x20>
    117f:	90                   	nop
    1180:	f3 0f 1e fa          	endbr64 
    1184:	68 15 00 00 00       	push   $0x15
    1189:	f2 e9 91 fe ff ff    	bnd jmp 1020 <_init+0x20>
    118f:	90                   	nop

Disassembly of section .plt.got:

0000000000001190 <__cxa_finalize@plt>:
    1190:	f3 0f 1e fa          	endbr64 
    1194:	f2 ff 25 55 3e 00 00 	bnd jmp *0x3e55(%rip)        # 4ff0 <__cxa_finalize@GLIBC_2.2.5>
    119b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

00000000000011a0 <printf@plt>:
    11a0:	f3 0f 1e fa          	endbr64 
    11a4:	f2 ff 25 7d 3d 00 00 	bnd jmp *0x3d7d(%rip)        # 4f28 <printf@GLIBC_2.2.5>
    11ab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011b0 <memset@plt>:
    11b0:	f3 0f 1e fa          	endbr64 
    11b4:	f2 ff 25 75 3d 00 00 	bnd jmp *0x3d75(%rip)        # 4f30 <memset@GLIBC_2.2.5>
    11bb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011c0 <snprintf@plt>:
    11c0:	f3 0f 1e fa          	endbr64 
    11c4:	f2 ff 25 6d 3d 00 00 	bnd jmp *0x3d6d(%rip)        # 4f38 <snprintf@GLIBC_2.2.5>
    11cb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011d0 <strncat@plt>:
    11d0:	f3 0f 1e fa          	endbr64 
    11d4:	f2 ff 25 65 3d 00 00 	bnd jmp *0x3d65(%rip)        # 4f40 <strncat@GLIBC_2.2.5>
    11db:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011e0 <MHD_queue_response@plt>:
    11e0:	f3 0f 1e fa          	endbr64 
    11e4:	f2 ff 25 5d 3d 00 00 	bnd jmp *0x3d5d(%rip)        # 4f48 <MHD_queue_response@Base>
    11eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000011f0 <strncmp@plt>:
    11f0:	f3 0f 1e fa          	endbr64 
    11f4:	f2 ff 25 55 3d 00 00 	bnd jmp *0x3d55(%rip)        # 4f50 <strncmp@GLIBC_2.2.5>
    11fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001200 <malloc@plt>:
    1200:	f3 0f 1e fa          	endbr64 
    1204:	f2 ff 25 4d 3d 00 00 	bnd jmp *0x3d4d(%rip)        # 4f58 <malloc@GLIBC_2.2.5>
    120b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001210 <free@plt>:
    1210:	f3 0f 1e fa          	endbr64 
    1214:	f2 ff 25 45 3d 00 00 	bnd jmp *0x3d45(%rip)        # 4f60 <free@GLIBC_2.2.5>
    121b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001220 <strlen@plt>:
    1220:	f3 0f 1e fa          	endbr64 
    1224:	f2 ff 25 3d 3d 00 00 	bnd jmp *0x3d3d(%rip)        # 4f68 <strlen@GLIBC_2.2.5>
    122b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001230 <strstr@plt>:
    1230:	f3 0f 1e fa          	endbr64 
    1234:	f2 ff 25 35 3d 00 00 	bnd jmp *0x3d35(%rip)        # 4f70 <strstr@GLIBC_2.2.5>
    123b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001240 <atoi@plt>:
    1240:	f3 0f 1e fa          	endbr64 
    1244:	f2 ff 25 2d 3d 00 00 	bnd jmp *0x3d2d(%rip)        # 4f78 <atoi@GLIBC_2.2.5>
    124b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001250 <MHD_start_daemon@plt>:
    1250:	f3 0f 1e fa          	endbr64 
    1254:	f2 ff 25 25 3d 00 00 	bnd jmp *0x3d25(%rip)        # 4f80 <MHD_start_daemon@Base>
    125b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001260 <getchar@plt>:
    1260:	f3 0f 1e fa          	endbr64 
    1264:	f2 ff 25 1d 3d 00 00 	bnd jmp *0x3d1d(%rip)        # 4f88 <getchar@GLIBC_2.2.5>
    126b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001270 <__stack_chk_fail@plt>:
    1270:	f3 0f 1e fa          	endbr64 
    1274:	f2 ff 25 15 3d 00 00 	bnd jmp *0x3d15(%rip)        # 4f90 <__stack_chk_fail@GLIBC_2.4>
    127b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001280 <strcmp@plt>:
    1280:	f3 0f 1e fa          	endbr64 
    1284:	f2 ff 25 0d 3d 00 00 	bnd jmp *0x3d0d(%rip)        # 4f98 <strcmp@GLIBC_2.2.5>
    128b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

0000000000001290 <MHD_create_response_from_buffer@plt>:
    1290:	f3 0f 1e fa          	endbr64 
    1294:	f2 ff 25 05 3d 00 00 	bnd jmp *0x3d05(%rip)        # 4fa0 <MHD_create_response_from_buffer@Base>
    129b:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000012a0 <strncpy@plt>:
    12a0:	f3 0f 1e fa          	endbr64 
    12a4:	f2 ff 25 fd 3c 00 00 	bnd jmp *0x3cfd(%rip)        # 4fa8 <strncpy@GLIBC_2.2.5>
    12ab:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000012b0 <MHD_destroy_response@plt>:
    12b0:	f3 0f 1e fa          	endbr64 
    12b4:	f2 ff 25 f5 3c 00 00 	bnd jmp *0x3cf5(%rip)        # 4fb0 <MHD_destroy_response@Base>
    12bb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000012c0 <fwrite@plt>:
    12c0:	f3 0f 1e fa          	endbr64 
    12c4:	f2 ff 25 ed 3c 00 00 	bnd jmp *0x3ced(%rip)        # 4fb8 <fwrite@GLIBC_2.2.5>
    12cb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000012d0 <realloc@plt>:
    12d0:	f3 0f 1e fa          	endbr64 
    12d4:	f2 ff 25 e5 3c 00 00 	bnd jmp *0x3ce5(%rip)        # 4fc0 <realloc@GLIBC_2.2.5>
    12db:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000012e0 <MHD_stop_daemon@plt>:
    12e0:	f3 0f 1e fa          	endbr64 
    12e4:	f2 ff 25 dd 3c 00 00 	bnd jmp *0x3cdd(%rip)        # 4fc8 <MHD_stop_daemon@Base>
    12eb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

00000000000012f0 <memcpy@plt>:
    12f0:	f3 0f 1e fa          	endbr64 
    12f4:	f2 ff 25 d5 3c 00 00 	bnd jmp *0x3cd5(%rip)        # 4fd0 <memcpy@GLIBC_2.14>
    12fb:	0f 1f 44 00 00       	nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

0000000000001300 <_start>:
    1300:	f3 0f 1e fa          	endbr64 
    1304:	31 ed                	xor    %ebp,%ebp
    1306:	49 89 d1             	mov    %rdx,%r9
    1309:	5e                   	pop    %rsi
    130a:	48 89 e2             	mov    %rsp,%rdx
    130d:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
    1311:	50                   	push   %rax
    1312:	54                   	push   %rsp
    1313:	45 31 c0             	xor    %r8d,%r8d
    1316:	31 c9                	xor    %ecx,%ecx
    1318:	48 8d 3d 5a 0d 00 00 	lea    0xd5a(%rip),%rdi        # 2079 <main>
    131f:	ff 15 d3 3c 00 00    	call   *0x3cd3(%rip)        # 4ff8 <__libc_start_main@GLIBC_2.34>
    1325:	f4                   	hlt    
    1326:	66 2e 0f 1f 84 00 00 	cs nopw 0x0(%rax,%rax,1)
    132d:	00 00 00 

0000000000001330 <deregister_tm_clones>:
    1330:	48 8d 3d d9 3c 00 00 	lea    0x3cd9(%rip),%rdi        # 5010 <__TMC_END__>
    1337:	48 8d 05 d2 3c 00 00 	lea    0x3cd2(%rip),%rax        # 5010 <__TMC_END__>
    133e:	48 39 f8             	cmp    %rdi,%rax
    1341:	74 15                	je     1358 <deregister_tm_clones+0x28>
    1343:	48 8b 05 96 3c 00 00 	mov    0x3c96(%rip),%rax        # 4fe0 <_ITM_deregisterTMCloneTable@Base>
    134a:	48 85 c0             	test   %rax,%rax
    134d:	74 09                	je     1358 <deregister_tm_clones+0x28>
    134f:	ff e0                	jmp    *%rax
    1351:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)
    1358:	c3                   	ret    
    1359:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000001360 <register_tm_clones>:
    1360:	48 8d 3d a9 3c 00 00 	lea    0x3ca9(%rip),%rdi        # 5010 <__TMC_END__>
    1367:	48 8d 35 a2 3c 00 00 	lea    0x3ca2(%rip),%rsi        # 5010 <__TMC_END__>
    136e:	48 29 fe             	sub    %rdi,%rsi
    1371:	48 89 f0             	mov    %rsi,%rax
    1374:	48 c1 ee 3f          	shr    $0x3f,%rsi
    1378:	48 c1 f8 03          	sar    $0x3,%rax
    137c:	48 01 c6             	add    %rax,%rsi
    137f:	48 d1 fe             	sar    %rsi
    1382:	74 14                	je     1398 <register_tm_clones+0x38>
    1384:	48 8b 05 5d 3c 00 00 	mov    0x3c5d(%rip),%rax        # 4fe8 <_ITM_registerTMCloneTable@Base>
    138b:	48 85 c0             	test   %rax,%rax
    138e:	74 08                	je     1398 <register_tm_clones+0x38>
    1390:	ff e0                	jmp    *%rax
    1392:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
    1398:	c3                   	ret    
    1399:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000013a0 <__do_global_dtors_aux>:
    13a0:	f3 0f 1e fa          	endbr64 
    13a4:	80 3d 7d 3c 00 00 00 	cmpb   $0x0,0x3c7d(%rip)        # 5028 <completed.0>
    13ab:	75 2b                	jne    13d8 <__do_global_dtors_aux+0x38>
    13ad:	55                   	push   %rbp
    13ae:	48 83 3d 3a 3c 00 00 	cmpq   $0x0,0x3c3a(%rip)        # 4ff0 <__cxa_finalize@GLIBC_2.2.5>
    13b5:	00 
    13b6:	48 89 e5             	mov    %rsp,%rbp
    13b9:	74 0c                	je     13c7 <__do_global_dtors_aux+0x27>
    13bb:	48 8b 3d 46 3c 00 00 	mov    0x3c46(%rip),%rdi        # 5008 <__dso_handle>
    13c2:	e8 c9 fd ff ff       	call   1190 <__cxa_finalize@plt>
    13c7:	e8 64 ff ff ff       	call   1330 <deregister_tm_clones>
    13cc:	c6 05 55 3c 00 00 01 	movb   $0x1,0x3c55(%rip)        # 5028 <completed.0>
    13d3:	5d                   	pop    %rbp
    13d4:	c3                   	ret    
    13d5:	0f 1f 00             	nopl   (%rax)
    13d8:	c3                   	ret    
    13d9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000000013e0 <frame_dummy>:
    13e0:	f3 0f 1e fa          	endbr64 
    13e4:	e9 77 ff ff ff       	jmp    1360 <register_tm_clones>

00000000000013e9 <initialize_database>:
    13e9:	f3 0f 1e fa          	endbr64 
    13ed:	55                   	push   %rbp
    13ee:	48 89 e5             	mov    %rsp,%rbp
    13f1:	ba 50 0a 00 00       	mov    $0xa50,%edx
    13f6:	be 00 00 00 00       	mov    $0x0,%esi
    13fb:	48 8d 05 3e 3c 00 00 	lea    0x3c3e(%rip),%rax        # 5040 <database>
    1402:	48 89 c7             	mov    %rax,%rdi
    1405:	e8 a6 fd ff ff       	call   11b0 <memset@plt>
    140a:	90                   	nop
    140b:	5d                   	pop    %rbp
    140c:	c3                   	ret    

000000000000140d <locate_record>:
    140d:	f3 0f 1e fa          	endbr64 
    1411:	55                   	push   %rbp
    1412:	48 89 e5             	mov    %rsp,%rbp
    1415:	89 7d ec             	mov    %edi,-0x14(%rbp)
    1418:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
    141f:	eb 54                	jmp    1475 <locate_record+0x68>
    1421:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1424:	48 63 d0             	movslq %eax,%rdx
    1427:	48 89 d0             	mov    %rdx,%rax
    142a:	48 c1 e0 05          	shl    $0x5,%rax
    142e:	48 01 d0             	add    %rdx,%rax
    1431:	48 c1 e0 03          	shl    $0x3,%rax
    1435:	48 89 c2             	mov    %rax,%rdx
    1438:	48 8d 05 05 3d 00 00 	lea    0x3d05(%rip),%rax        # 5144 <database+0x104>
    143f:	8b 04 02             	mov    (%rdx,%rax,1),%eax
    1442:	85 c0                	test   %eax,%eax
    1444:	74 2b                	je     1471 <locate_record+0x64>
    1446:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1449:	48 63 d0             	movslq %eax,%rdx
    144c:	48 89 d0             	mov    %rdx,%rax
    144f:	48 c1 e0 05          	shl    $0x5,%rax
    1453:	48 01 d0             	add    %rdx,%rax
    1456:	48 c1 e0 03          	shl    $0x3,%rax
    145a:	48 89 c2             	mov    %rax,%rdx
    145d:	48 8d 05 dc 3b 00 00 	lea    0x3bdc(%rip),%rax        # 5040 <database>
    1464:	8b 04 02             	mov    (%rdx,%rax,1),%eax
    1467:	39 45 ec             	cmp    %eax,-0x14(%rbp)
    146a:	75 05                	jne    1471 <locate_record+0x64>
    146c:	8b 45 fc             	mov    -0x4(%rbp),%eax
    146f:	eb 0f                	jmp    1480 <locate_record+0x73>
    1471:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
    1475:	83 7d fc 09          	cmpl   $0x9,-0x4(%rbp)
    1479:	7e a6                	jle    1421 <locate_record+0x14>
    147b:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    1480:	5d                   	pop    %rbp
    1481:	c3                   	ret    

0000000000001482 <insert_record>:
    1482:	f3 0f 1e fa          	endbr64 
    1486:	55                   	push   %rbp
    1487:	48 89 e5             	mov    %rsp,%rbp
    148a:	48 83 ec 20          	sub    $0x20,%rsp
    148e:	89 7d ec             	mov    %edi,-0x14(%rbp)
    1491:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
    1495:	8b 45 ec             	mov    -0x14(%rbp),%eax
    1498:	89 c7                	mov    %eax,%edi
    149a:	e8 6e ff ff ff       	call   140d <locate_record>
    149f:	83 f8 ff             	cmp    $0xffffffff,%eax
    14a2:	74 0a                	je     14ae <insert_record+0x2c>
    14a4:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    14a9:	e9 f0 00 00 00       	jmp    159e <insert_record+0x11c>
    14ae:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
    14b5:	e9 d5 00 00 00       	jmp    158f <insert_record+0x10d>
    14ba:	8b 45 fc             	mov    -0x4(%rbp),%eax
    14bd:	48 63 d0             	movslq %eax,%rdx
    14c0:	48 89 d0             	mov    %rdx,%rax
    14c3:	48 c1 e0 05          	shl    $0x5,%rax
    14c7:	48 01 d0             	add    %rdx,%rax
    14ca:	48 c1 e0 03          	shl    $0x3,%rax
    14ce:	48 89 c2             	mov    %rax,%rdx
    14d1:	48 8d 05 6c 3c 00 00 	lea    0x3c6c(%rip),%rax        # 5144 <database+0x104>
    14d8:	8b 04 02             	mov    (%rdx,%rax,1),%eax
    14db:	85 c0                	test   %eax,%eax
    14dd:	0f 85 a8 00 00 00    	jne    158b <insert_record+0x109>
    14e3:	8b 45 fc             	mov    -0x4(%rbp),%eax
    14e6:	48 63 d0             	movslq %eax,%rdx
    14e9:	48 89 d0             	mov    %rdx,%rax
    14ec:	48 c1 e0 05          	shl    $0x5,%rax
    14f0:	48 01 d0             	add    %rdx,%rax
    14f3:	48 c1 e0 03          	shl    $0x3,%rax
    14f7:	48 89 c1             	mov    %rax,%rcx
    14fa:	48 8d 15 3f 3b 00 00 	lea    0x3b3f(%rip),%rdx        # 5040 <database>
    1501:	8b 45 ec             	mov    -0x14(%rbp),%eax
    1504:	89 04 11             	mov    %eax,(%rcx,%rdx,1)
    1507:	8b 45 fc             	mov    -0x4(%rbp),%eax
    150a:	48 63 d0             	movslq %eax,%rdx
    150d:	48 89 d0             	mov    %rdx,%rax
    1510:	48 c1 e0 05          	shl    $0x5,%rax
    1514:	48 01 d0             	add    %rdx,%rax
    1517:	48 c1 e0 03          	shl    $0x3,%rax
    151b:	48 8d 15 1e 3b 00 00 	lea    0x3b1e(%rip),%rdx        # 5040 <database>
    1522:	48 01 d0             	add    %rdx,%rax
    1525:	48 8d 48 04          	lea    0x4(%rax),%rcx
    1529:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    152d:	ba ff 00 00 00       	mov    $0xff,%edx
    1532:	48 89 c6             	mov    %rax,%rsi
    1535:	48 89 cf             	mov    %rcx,%rdi
    1538:	e8 63 fd ff ff       	call   12a0 <strncpy@plt>
    153d:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1540:	48 63 d0             	movslq %eax,%rdx
    1543:	48 89 d0             	mov    %rdx,%rax
    1546:	48 c1 e0 05          	shl    $0x5,%rax
    154a:	48 01 d0             	add    %rdx,%rax
    154d:	48 c1 e0 03          	shl    $0x3,%rax
    1551:	48 89 c2             	mov    %rax,%rdx
    1554:	48 8d 05 e8 3b 00 00 	lea    0x3be8(%rip),%rax        # 5143 <database+0x103>
    155b:	c6 04 02 00          	movb   $0x0,(%rdx,%rax,1)
    155f:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1562:	48 63 d0             	movslq %eax,%rdx
    1565:	48 89 d0             	mov    %rdx,%rax
    1568:	48 c1 e0 05          	shl    $0x5,%rax
    156c:	48 01 d0             	add    %rdx,%rax
    156f:	48 c1 e0 03          	shl    $0x3,%rax
    1573:	48 89 c2             	mov    %rax,%rdx
    1576:	48 8d 05 c7 3b 00 00 	lea    0x3bc7(%rip),%rax        # 5144 <database+0x104>
    157d:	c7 04 02 01 00 00 00 	movl   $0x1,(%rdx,%rax,1)
    1584:	b8 00 00 00 00       	mov    $0x0,%eax
    1589:	eb 13                	jmp    159e <insert_record+0x11c>
    158b:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
    158f:	83 7d fc 09          	cmpl   $0x9,-0x4(%rbp)
    1593:	0f 8e 21 ff ff ff    	jle    14ba <insert_record+0x38>
    1599:	b8 fe ff ff ff       	mov    $0xfffffffe,%eax
    159e:	c9                   	leave  
    159f:	c3                   	ret    

00000000000015a0 <fetch_record_content>:
    15a0:	f3 0f 1e fa          	endbr64 
    15a4:	55                   	push   %rbp
    15a5:	48 89 e5             	mov    %rsp,%rbp
    15a8:	48 83 ec 18          	sub    $0x18,%rsp
    15ac:	89 7d ec             	mov    %edi,-0x14(%rbp)
    15af:	8b 45 ec             	mov    -0x14(%rbp),%eax
    15b2:	89 c7                	mov    %eax,%edi
    15b4:	e8 54 fe ff ff       	call   140d <locate_record>
    15b9:	89 45 fc             	mov    %eax,-0x4(%rbp)
    15bc:	83 7d fc ff          	cmpl   $0xffffffff,-0x4(%rbp)
    15c0:	74 24                	je     15e6 <fetch_record_content+0x46>
    15c2:	8b 45 fc             	mov    -0x4(%rbp),%eax
    15c5:	48 63 d0             	movslq %eax,%rdx
    15c8:	48 89 d0             	mov    %rdx,%rax
    15cb:	48 c1 e0 05          	shl    $0x5,%rax
    15cf:	48 01 d0             	add    %rdx,%rax
    15d2:	48 c1 e0 03          	shl    $0x3,%rax
    15d6:	48 8d 15 63 3a 00 00 	lea    0x3a63(%rip),%rdx        # 5040 <database>
    15dd:	48 01 d0             	add    %rdx,%rax
    15e0:	48 83 c0 04          	add    $0x4,%rax
    15e4:	eb 05                	jmp    15eb <fetch_record_content+0x4b>
    15e6:	b8 00 00 00 00       	mov    $0x0,%eax
    15eb:	c9                   	leave  
    15ec:	c3                   	ret    

00000000000015ed <modify_record>:
    15ed:	f3 0f 1e fa          	endbr64 
    15f1:	55                   	push   %rbp
    15f2:	48 89 e5             	mov    %rsp,%rbp
    15f5:	48 83 ec 20          	sub    $0x20,%rsp
    15f9:	89 7d ec             	mov    %edi,-0x14(%rbp)
    15fc:	48 89 75 e0          	mov    %rsi,-0x20(%rbp)
    1600:	8b 45 ec             	mov    -0x14(%rbp),%eax
    1603:	89 c7                	mov    %eax,%edi
    1605:	e8 03 fe ff ff       	call   140d <locate_record>
    160a:	89 45 fc             	mov    %eax,-0x4(%rbp)
    160d:	83 7d fc ff          	cmpl   $0xffffffff,-0x4(%rbp)
    1611:	75 07                	jne    161a <modify_record+0x2d>
    1613:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    1618:	eb 5d                	jmp    1677 <modify_record+0x8a>
    161a:	8b 45 fc             	mov    -0x4(%rbp),%eax
    161d:	48 63 d0             	movslq %eax,%rdx
    1620:	48 89 d0             	mov    %rdx,%rax
    1623:	48 c1 e0 05          	shl    $0x5,%rax
    1627:	48 01 d0             	add    %rdx,%rax
    162a:	48 c1 e0 03          	shl    $0x3,%rax
    162e:	48 8d 15 0b 3a 00 00 	lea    0x3a0b(%rip),%rdx        # 5040 <database>
    1635:	48 01 d0             	add    %rdx,%rax
    1638:	48 8d 48 04          	lea    0x4(%rax),%rcx
    163c:	48 8b 45 e0          	mov    -0x20(%rbp),%rax
    1640:	ba ff 00 00 00       	mov    $0xff,%edx
    1645:	48 89 c6             	mov    %rax,%rsi
    1648:	48 89 cf             	mov    %rcx,%rdi
    164b:	e8 50 fc ff ff       	call   12a0 <strncpy@plt>
    1650:	8b 45 fc             	mov    -0x4(%rbp),%eax
    1653:	48 63 d0             	movslq %eax,%rdx
    1656:	48 89 d0             	mov    %rdx,%rax
    1659:	48 c1 e0 05          	shl    $0x5,%rax
    165d:	48 01 d0             	add    %rdx,%rax
    1660:	48 c1 e0 03          	shl    $0x3,%rax
    1664:	48 89 c2             	mov    %rax,%rdx
    1667:	48 8d 05 d5 3a 00 00 	lea    0x3ad5(%rip),%rax        # 5143 <database+0x103>
    166e:	c6 04 02 00          	movb   $0x0,(%rdx,%rax,1)
    1672:	b8 00 00 00 00       	mov    $0x0,%eax
    1677:	c9                   	leave  
    1678:	c3                   	ret    

0000000000001679 <erase_record>:
    1679:	f3 0f 1e fa          	endbr64 
    167d:	55                   	push   %rbp
    167e:	48 89 e5             	mov    %rsp,%rbp
    1681:	48 83 ec 18          	sub    $0x18,%rsp
    1685:	89 7d ec             	mov    %edi,-0x14(%rbp)
    1688:	8b 45 ec             	mov    -0x14(%rbp),%eax
    168b:	89 c7                	mov    %eax,%edi
    168d:	e8 7b fd ff ff       	call   140d <locate_record>
    1692:	89 45 fc             	mov    %eax,-0x4(%rbp)
    1695:	83 7d fc ff          	cmpl   $0xffffffff,-0x4(%rbp)
    1699:	75 07                	jne    16a2 <erase_record+0x29>
    169b:	b8 ff ff ff ff       	mov    $0xffffffff,%eax
    16a0:	eb 2a                	jmp    16cc <erase_record+0x53>
    16a2:	8b 45 fc             	mov    -0x4(%rbp),%eax
    16a5:	48 63 d0             	movslq %eax,%rdx
    16a8:	48 89 d0             	mov    %rdx,%rax
    16ab:	48 c1 e0 05          	shl    $0x5,%rax
    16af:	48 01 d0             	add    %rdx,%rax
    16b2:	48 c1 e0 03          	shl    $0x3,%rax
    16b6:	48 89 c2             	mov    %rax,%rdx
    16b9:	48 8d 05 84 3a 00 00 	lea    0x3a84(%rip),%rax        # 5144 <database+0x104>
    16c0:	c7 04 02 00 00 00 00 	movl   $0x0,(%rdx,%rax,1)
    16c7:	b8 00 00 00 00       	mov    $0x0,%eax
    16cc:	c9                   	leave  
    16cd:	c3                   	ret    

00000000000016ce <format_records>:
    16ce:	f3 0f 1e fa          	endbr64 
    16d2:	55                   	push   %rbp
    16d3:	48 89 e5             	mov    %rsp,%rbp
    16d6:	48 81 ec 30 01 00 00 	sub    $0x130,%rsp
    16dd:	48 89 bd d8 fe ff ff 	mov    %rdi,-0x128(%rbp)
    16e4:	48 89 b5 d0 fe ff ff 	mov    %rsi,-0x130(%rbp)
    16eb:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    16f2:	00 00 
    16f4:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    16f8:	31 c0                	xor    %eax,%eax
    16fa:	48 8b 8d d0 fe ff ff 	mov    -0x130(%rbp),%rcx
    1701:	48 8b 85 d8 fe ff ff 	mov    -0x128(%rbp),%rax
    1708:	48 8d 15 f5 18 00 00 	lea    0x18f5(%rip),%rdx        # 3004 <_IO_stdin_used+0x4>
    170f:	48 89 ce             	mov    %rcx,%rsi
    1712:	48 89 c7             	mov    %rax,%rdi
    1715:	b8 00 00 00 00       	mov    $0x0,%eax
    171a:	e8 a1 fa ff ff       	call   11c0 <snprintf@plt>
    171f:	c7 85 ec fe ff ff 00 	movl   $0x0,-0x114(%rbp)
    1726:	00 00 00 
    1729:	e9 da 00 00 00       	jmp    1808 <format_records+0x13a>
    172e:	8b 85 ec fe ff ff    	mov    -0x114(%rbp),%eax
    1734:	48 63 d0             	movslq %eax,%rdx
    1737:	48 89 d0             	mov    %rdx,%rax
    173a:	48 c1 e0 05          	shl    $0x5,%rax
    173e:	48 01 d0             	add    %rdx,%rax
    1741:	48 c1 e0 03          	shl    $0x3,%rax
    1745:	48 89 c2             	mov    %rax,%rdx
    1748:	48 8d 05 f5 39 00 00 	lea    0x39f5(%rip),%rax        # 5144 <database+0x104>
    174f:	8b 04 02             	mov    (%rdx,%rax,1),%eax
    1752:	85 c0                	test   %eax,%eax
    1754:	0f 84 a7 00 00 00    	je     1801 <format_records+0x133>
    175a:	8b 85 ec fe ff ff    	mov    -0x114(%rbp),%eax
    1760:	48 63 d0             	movslq %eax,%rdx
    1763:	48 89 d0             	mov    %rdx,%rax
    1766:	48 c1 e0 05          	shl    $0x5,%rax
    176a:	48 01 d0             	add    %rdx,%rax
    176d:	48 c1 e0 03          	shl    $0x3,%rax
    1771:	48 8d 15 c8 38 00 00 	lea    0x38c8(%rip),%rdx        # 5040 <database>
    1778:	48 01 d0             	add    %rdx,%rax
    177b:	48 8d 48 04          	lea    0x4(%rax),%rcx
    177f:	8b 85 ec fe ff ff    	mov    -0x114(%rbp),%eax
    1785:	48 63 d0             	movslq %eax,%rdx
    1788:	48 89 d0             	mov    %rdx,%rax
    178b:	48 c1 e0 05          	shl    $0x5,%rax
    178f:	48 01 d0             	add    %rdx,%rax
    1792:	48 c1 e0 03          	shl    $0x3,%rax
    1796:	48 89 c2             	mov    %rax,%rdx
    1799:	48 8d 05 a0 38 00 00 	lea    0x38a0(%rip),%rax        # 5040 <database>
    17a0:	8b 14 02             	mov    (%rdx,%rax,1),%edx
    17a3:	48 8d 85 f0 fe ff ff 	lea    -0x110(%rbp),%rax
    17aa:	49 89 c8             	mov    %rcx,%r8
    17ad:	89 d1                	mov    %edx,%ecx
    17af:	48 8d 15 58 18 00 00 	lea    0x1858(%rip),%rdx        # 300e <_IO_stdin_used+0xe>
    17b6:	be 00 01 00 00       	mov    $0x100,%esi
    17bb:	48 89 c7             	mov    %rax,%rdi
    17be:	b8 00 00 00 00       	mov    $0x0,%eax
    17c3:	e8 f8 f9 ff ff       	call   11c0 <snprintf@plt>
    17c8:	48 8b 85 d8 fe ff ff 	mov    -0x128(%rbp),%rax
    17cf:	48 89 c7             	mov    %rax,%rdi
    17d2:	e8 49 fa ff ff       	call   1220 <strlen@plt>
    17d7:	48 89 c2             	mov    %rax,%rdx
    17da:	48 8b 85 d0 fe ff ff 	mov    -0x130(%rbp),%rax
    17e1:	48 29 d0             	sub    %rdx,%rax
    17e4:	48 8d 50 ff          	lea    -0x1(%rax),%rdx
    17e8:	48 8d 8d f0 fe ff ff 	lea    -0x110(%rbp),%rcx
    17ef:	48 8b 85 d8 fe ff ff 	mov    -0x128(%rbp),%rax
    17f6:	48 89 ce             	mov    %rcx,%rsi
    17f9:	48 89 c7             	mov    %rax,%rdi
    17fc:	e8 cf f9 ff ff       	call   11d0 <strncat@plt>
    1801:	83 85 ec fe ff ff 01 	addl   $0x1,-0x114(%rbp)
    1808:	83 bd ec fe ff ff 09 	cmpl   $0x9,-0x114(%rbp)
    180f:	0f 8e 19 ff ff ff    	jle    172e <format_records+0x60>
    1815:	90                   	nop
    1816:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    181a:	64 48 2b 04 25 28 00 	sub    %fs:0x28,%rax
    1821:	00 00 
    1823:	74 05                	je     182a <format_records+0x15c>
    1825:	e8 46 fa ff ff       	call   1270 <__stack_chk_fail@plt>
    182a:	c9                   	leave  
    182b:	c3                   	ret    

000000000000182c <process_request>:
    182c:	f3 0f 1e fa          	endbr64 
    1830:	55                   	push   %rbp
    1831:	48 89 e5             	mov    %rsp,%rbp
    1834:	48 81 ec c0 04 00 00 	sub    $0x4c0,%rsp
    183b:	48 89 bd 78 fb ff ff 	mov    %rdi,-0x488(%rbp)
    1842:	48 89 b5 70 fb ff ff 	mov    %rsi,-0x490(%rbp)
    1849:	48 89 95 68 fb ff ff 	mov    %rdx,-0x498(%rbp)
    1850:	48 89 8d 60 fb ff ff 	mov    %rcx,-0x4a0(%rbp)
    1857:	4c 89 85 58 fb ff ff 	mov    %r8,-0x4a8(%rbp)
    185e:	4c 89 8d 50 fb ff ff 	mov    %r9,-0x4b0(%rbp)
    1865:	48 8b 45 10          	mov    0x10(%rbp),%rax
    1869:	48 89 85 48 fb ff ff 	mov    %rax,-0x4b8(%rbp)
    1870:	48 8b 45 18          	mov    0x18(%rbp),%rax
    1874:	48 89 85 40 fb ff ff 	mov    %rax,-0x4c0(%rbp)
    187b:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    1882:	00 00 
    1884:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    1888:	31 c0                	xor    %eax,%eax
    188a:	48 8b 85 40 fb ff ff 	mov    -0x4c0(%rbp),%rax
    1891:	48 8b 00             	mov    (%rax),%rax
    1894:	48 85 c0             	test   %rax,%rax
    1897:	75 5d                	jne    18f6 <process_request+0xca>
    1899:	bf 10 00 00 00       	mov    $0x10,%edi
    189e:	e8 5d f9 ff ff       	call   1200 <malloc@plt>
    18a3:	48 89 85 e8 fb ff ff 	mov    %rax,-0x418(%rbp)
    18aa:	48 83 bd e8 fb ff ff 	cmpq   $0x0,-0x418(%rbp)
    18b1:	00 
    18b2:	75 0a                	jne    18be <process_request+0x92>
    18b4:	b8 00 00 00 00       	mov    $0x0,%eax
    18b9:	e9 a5 07 00 00       	jmp    2063 <process_request+0x837>
    18be:	48 8b 85 e8 fb ff ff 	mov    -0x418(%rbp),%rax
    18c5:	48 c7 00 00 00 00 00 	movq   $0x0,(%rax)
    18cc:	48 8b 85 e8 fb ff ff 	mov    -0x418(%rbp),%rax
    18d3:	48 c7 40 08 00 00 00 	movq   $0x0,0x8(%rax)
    18da:	00 
    18db:	48 8b 85 40 fb ff ff 	mov    -0x4c0(%rbp),%rax
    18e2:	48 8b 95 e8 fb ff ff 	mov    -0x418(%rbp),%rdx
    18e9:	48 89 10             	mov    %rdx,(%rax)
    18ec:	b8 01 00 00 00       	mov    $0x1,%eax
    18f1:	e9 6d 07 00 00       	jmp    2063 <process_request+0x837>
    18f6:	48 8b 85 40 fb ff ff 	mov    -0x4c0(%rbp),%rax
    18fd:	48 8b 00             	mov    (%rax),%rax
    1900:	48 89 85 a8 fb ff ff 	mov    %rax,-0x458(%rbp)
    1907:	48 8b 85 48 fb ff ff 	mov    -0x4b8(%rbp),%rax
    190e:	48 8b 00             	mov    (%rax),%rax
    1911:	48 85 c0             	test   %rax,%rax
    1914:	0f 84 09 01 00 00    	je     1a23 <process_request+0x1f7>
    191a:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1921:	48 8b 50 08          	mov    0x8(%rax),%rdx
    1925:	48 8b 85 48 fb ff ff 	mov    -0x4b8(%rbp),%rax
    192c:	48 8b 00             	mov    (%rax),%rax
    192f:	48 01 d0             	add    %rdx,%rax
    1932:	48 89 85 d8 fb ff ff 	mov    %rax,-0x428(%rbp)
    1939:	48 8b 85 d8 fb ff ff 	mov    -0x428(%rbp),%rax
    1940:	48 8d 50 01          	lea    0x1(%rax),%rdx
    1944:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    194b:	48 8b 00             	mov    (%rax),%rax
    194e:	48 89 d6             	mov    %rdx,%rsi
    1951:	48 89 c7             	mov    %rax,%rdi
    1954:	e8 77 f9 ff ff       	call   12d0 <realloc@plt>
    1959:	48 89 85 e0 fb ff ff 	mov    %rax,-0x420(%rbp)
    1960:	48 83 bd e0 fb ff ff 	cmpq   $0x0,-0x420(%rbp)
    1967:	00 
    1968:	75 39                	jne    19a3 <process_request+0x177>
    196a:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1971:	48 8b 00             	mov    (%rax),%rax
    1974:	48 89 c7             	mov    %rax,%rdi
    1977:	e8 94 f8 ff ff       	call   1210 <free@plt>
    197c:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1983:	48 89 c7             	mov    %rax,%rdi
    1986:	e8 85 f8 ff ff       	call   1210 <free@plt>
    198b:	48 8b 85 40 fb ff ff 	mov    -0x4c0(%rbp),%rax
    1992:	48 c7 00 00 00 00 00 	movq   $0x0,(%rax)
    1999:	b8 00 00 00 00       	mov    $0x0,%eax
    199e:	e9 c0 06 00 00       	jmp    2063 <process_request+0x837>
    19a3:	48 8b 85 48 fb ff ff 	mov    -0x4b8(%rbp),%rax
    19aa:	48 8b 10             	mov    (%rax),%rdx
    19ad:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    19b4:	48 8b 48 08          	mov    0x8(%rax),%rcx
    19b8:	48 8b 85 e0 fb ff ff 	mov    -0x420(%rbp),%rax
    19bf:	48 01 c1             	add    %rax,%rcx
    19c2:	48 8b 85 50 fb ff ff 	mov    -0x4b0(%rbp),%rax
    19c9:	48 89 c6             	mov    %rax,%rsi
    19cc:	48 89 cf             	mov    %rcx,%rdi
    19cf:	e8 1c f9 ff ff       	call   12f0 <memcpy@plt>
    19d4:	48 8b 95 e0 fb ff ff 	mov    -0x420(%rbp),%rdx
    19db:	48 8b 85 d8 fb ff ff 	mov    -0x428(%rbp),%rax
    19e2:	48 01 d0             	add    %rdx,%rax
    19e5:	c6 00 00             	movb   $0x0,(%rax)
    19e8:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    19ef:	48 8b 95 e0 fb ff ff 	mov    -0x420(%rbp),%rdx
    19f6:	48 89 10             	mov    %rdx,(%rax)
    19f9:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1a00:	48 8b 95 d8 fb ff ff 	mov    -0x428(%rbp),%rdx
    1a07:	48 89 50 08          	mov    %rdx,0x8(%rax)
    1a0b:	48 8b 85 48 fb ff ff 	mov    -0x4b8(%rbp),%rax
    1a12:	48 c7 00 00 00 00 00 	movq   $0x0,(%rax)
    1a19:	b8 01 00 00 00       	mov    $0x1,%eax
    1a1e:	e9 40 06 00 00       	jmp    2063 <process_request+0x837>
    1a23:	48 c7 85 f0 fb ff ff 	movq   $0x0,-0x410(%rbp)
    1a2a:	00 00 00 00 
    1a2e:	48 c7 85 f8 fb ff ff 	movq   $0x0,-0x408(%rbp)
    1a35:	00 00 00 00 
    1a39:	48 8d 95 00 fc ff ff 	lea    -0x400(%rbp),%rdx
    1a40:	b8 00 00 00 00       	mov    $0x0,%eax
    1a45:	b9 7e 00 00 00       	mov    $0x7e,%ecx
    1a4a:	48 89 d7             	mov    %rdx,%rdi
    1a4d:	f3 48 ab             	rep stos %rax,%es:(%rdi)
    1a50:	c7 85 84 fb ff ff c8 	movl   $0xc8,-0x47c(%rbp)
    1a57:	00 00 00 
    1a5a:	48 8b 85 60 fb ff ff 	mov    -0x4a0(%rbp),%rax
    1a61:	48 8d 15 b8 15 00 00 	lea    0x15b8(%rip),%rdx        # 3020 <_IO_stdin_used+0x20>
    1a68:	48 89 d6             	mov    %rdx,%rsi
    1a6b:	48 89 c7             	mov    %rax,%rdi
    1a6e:	e8 0d f8 ff ff       	call   1280 <strcmp@plt>
    1a73:	85 c0                	test   %eax,%eax
    1a75:	0f 85 28 01 00 00    	jne    1ba3 <process_request+0x377>
    1a7b:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1a82:	48 8d 15 9b 15 00 00 	lea    0x159b(%rip),%rdx        # 3024 <_IO_stdin_used+0x24>
    1a89:	48 89 d6             	mov    %rdx,%rsi
    1a8c:	48 89 c7             	mov    %rax,%rdi
    1a8f:	e8 ec f7 ff ff       	call   1280 <strcmp@plt>
    1a94:	85 c0                	test   %eax,%eax
    1a96:	75 19                	jne    1ab1 <process_request+0x285>
    1a98:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1a9f:	be 00 04 00 00       	mov    $0x400,%esi
    1aa4:	48 89 c7             	mov    %rax,%rdi
    1aa7:	e8 22 fc ff ff       	call   16ce <format_records>
    1aac:	e9 0b 05 00 00       	jmp    1fbc <process_request+0x790>
    1ab1:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1ab8:	ba 07 00 00 00       	mov    $0x7,%edx
    1abd:	48 8d 0d 67 15 00 00 	lea    0x1567(%rip),%rcx        # 302b <_IO_stdin_used+0x2b>
    1ac4:	48 89 ce             	mov    %rcx,%rsi
    1ac7:	48 89 c7             	mov    %rax,%rdi
    1aca:	e8 21 f7 ff ff       	call   11f0 <strncmp@plt>
    1acf:	85 c0                	test   %eax,%eax
    1ad1:	0f 85 9d 00 00 00    	jne    1b74 <process_request+0x348>
    1ad7:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1ade:	48 83 c0 07          	add    $0x7,%rax
    1ae2:	48 89 c7             	mov    %rax,%rdi
    1ae5:	e8 56 f7 ff ff       	call   1240 <atoi@plt>
    1aea:	89 85 a0 fb ff ff    	mov    %eax,-0x460(%rbp)
    1af0:	8b 85 a0 fb ff ff    	mov    -0x460(%rbp),%eax
    1af6:	89 c7                	mov    %eax,%edi
    1af8:	e8 a3 fa ff ff       	call   15a0 <fetch_record_content>
    1afd:	48 89 85 c8 fb ff ff 	mov    %rax,-0x438(%rbp)
    1b04:	48 83 bd c8 fb ff ff 	cmpq   $0x0,-0x438(%rbp)
    1b0b:	00 
    1b0c:	74 37                	je     1b45 <process_request+0x319>
    1b0e:	48 8b 8d c8 fb ff ff 	mov    -0x438(%rbp),%rcx
    1b15:	8b 95 a0 fb ff ff    	mov    -0x460(%rbp),%edx
    1b1b:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1b22:	49 89 c8             	mov    %rcx,%r8
    1b25:	89 d1                	mov    %edx,%ecx
    1b27:	48 8d 15 05 15 00 00 	lea    0x1505(%rip),%rdx        # 3033 <_IO_stdin_used+0x33>
    1b2e:	be 00 04 00 00       	mov    $0x400,%esi
    1b33:	48 89 c7             	mov    %rax,%rdi
    1b36:	b8 00 00 00 00       	mov    $0x0,%eax
    1b3b:	e8 80 f6 ff ff       	call   11c0 <snprintf@plt>
    1b40:	e9 77 04 00 00       	jmp    1fbc <process_request+0x790>
    1b45:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1b4c:	48 8d 15 f1 14 00 00 	lea    0x14f1(%rip),%rdx        # 3044 <_IO_stdin_used+0x44>
    1b53:	be 00 04 00 00       	mov    $0x400,%esi
    1b58:	48 89 c7             	mov    %rax,%rdi
    1b5b:	b8 00 00 00 00       	mov    $0x0,%eax
    1b60:	e8 5b f6 ff ff       	call   11c0 <snprintf@plt>
    1b65:	c7 85 84 fb ff ff 94 	movl   $0x194,-0x47c(%rbp)
    1b6c:	01 00 00 
    1b6f:	e9 48 04 00 00       	jmp    1fbc <process_request+0x790>
    1b74:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1b7b:	48 8d 15 cc 14 00 00 	lea    0x14cc(%rip),%rdx        # 304e <_IO_stdin_used+0x4e>
    1b82:	be 00 04 00 00       	mov    $0x400,%esi
    1b87:	48 89 c7             	mov    %rax,%rdi
    1b8a:	b8 00 00 00 00       	mov    $0x0,%eax
    1b8f:	e8 2c f6 ff ff       	call   11c0 <snprintf@plt>
    1b94:	c7 85 84 fb ff ff 94 	movl   $0x194,-0x47c(%rbp)
    1b9b:	01 00 00 
    1b9e:	e9 19 04 00 00       	jmp    1fbc <process_request+0x790>
    1ba3:	48 8b 85 60 fb ff ff 	mov    -0x4a0(%rbp),%rax
    1baa:	48 8d 15 ad 14 00 00 	lea    0x14ad(%rip),%rdx        # 305e <_IO_stdin_used+0x5e>
    1bb1:	48 89 d6             	mov    %rdx,%rsi
    1bb4:	48 89 c7             	mov    %rax,%rdi
    1bb7:	e8 c4 f6 ff ff       	call   1280 <strcmp@plt>
    1bbc:	85 c0                	test   %eax,%eax
    1bbe:	0f 85 95 01 00 00    	jne    1d59 <process_request+0x52d>
    1bc4:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1bcb:	48 8d 15 52 14 00 00 	lea    0x1452(%rip),%rdx        # 3024 <_IO_stdin_used+0x24>
    1bd2:	48 89 d6             	mov    %rdx,%rsi
    1bd5:	48 89 c7             	mov    %rax,%rdi
    1bd8:	e8 a3 f6 ff ff       	call   1280 <strcmp@plt>
    1bdd:	85 c0                	test   %eax,%eax
    1bdf:	0f 85 d7 03 00 00    	jne    1fbc <process_request+0x790>
    1be5:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1bec:	48 8b 00             	mov    (%rax),%rax
    1bef:	48 85 c0             	test   %rax,%rax
    1bf2:	75 2f                	jne    1c23 <process_request+0x3f7>
    1bf4:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1bfb:	48 8d 15 4c 14 00 00 	lea    0x144c(%rip),%rdx        # 304e <_IO_stdin_used+0x4e>
    1c02:	be 00 04 00 00       	mov    $0x400,%esi
    1c07:	48 89 c7             	mov    %rax,%rdi
    1c0a:	b8 00 00 00 00       	mov    $0x0,%eax
    1c0f:	e8 ac f5 ff ff       	call   11c0 <snprintf@plt>
    1c14:	c7 85 84 fb ff ff 90 	movl   $0x190,-0x47c(%rbp)
    1c1b:	01 00 00 
    1c1e:	e9 99 03 00 00       	jmp    1fbc <process_request+0x790>
    1c23:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1c2a:	48 8b 00             	mov    (%rax),%rax
    1c2d:	48 8d 15 2f 14 00 00 	lea    0x142f(%rip),%rdx        # 3063 <_IO_stdin_used+0x63>
    1c34:	48 89 d6             	mov    %rdx,%rsi
    1c37:	48 89 c7             	mov    %rax,%rdi
    1c3a:	e8 f1 f5 ff ff       	call   1230 <strstr@plt>
    1c3f:	48 89 85 b8 fb ff ff 	mov    %rax,-0x448(%rbp)
    1c46:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1c4d:	48 8b 00             	mov    (%rax),%rax
    1c50:	48 8d 15 10 14 00 00 	lea    0x1410(%rip),%rdx        # 3067 <_IO_stdin_used+0x67>
    1c57:	48 89 d6             	mov    %rdx,%rsi
    1c5a:	48 89 c7             	mov    %rax,%rdi
    1c5d:	e8 ce f5 ff ff       	call   1230 <strstr@plt>
    1c62:	48 89 85 c0 fb ff ff 	mov    %rax,-0x440(%rbp)
    1c69:	48 83 bd b8 fb ff ff 	cmpq   $0x0,-0x448(%rbp)
    1c70:	00 
    1c71:	0f 84 b3 00 00 00    	je     1d2a <process_request+0x4fe>
    1c77:	48 83 bd c0 fb ff ff 	cmpq   $0x0,-0x440(%rbp)
    1c7e:	00 
    1c7f:	0f 84 a5 00 00 00    	je     1d2a <process_request+0x4fe>
    1c85:	48 8b 85 b8 fb ff ff 	mov    -0x448(%rbp),%rax
    1c8c:	48 83 c0 03          	add    $0x3,%rax
    1c90:	48 89 c7             	mov    %rax,%rdi
    1c93:	e8 a8 f5 ff ff       	call   1240 <atoi@plt>
    1c98:	89 85 98 fb ff ff    	mov    %eax,-0x468(%rbp)
    1c9e:	48 83 85 c0 fb ff ff 	addq   $0x5,-0x440(%rbp)
    1ca5:	05 
    1ca6:	48 8b 95 c0 fb ff ff 	mov    -0x440(%rbp),%rdx
    1cad:	8b 85 98 fb ff ff    	mov    -0x468(%rbp),%eax
    1cb3:	48 89 d6             	mov    %rdx,%rsi
    1cb6:	89 c7                	mov    %eax,%edi
    1cb8:	e8 c5 f7 ff ff       	call   1482 <insert_record>
    1cbd:	89 85 9c fb ff ff    	mov    %eax,-0x464(%rbp)
    1cc3:	83 bd 9c fb ff ff 00 	cmpl   $0x0,-0x464(%rbp)
    1cca:	74 1b                	je     1ce7 <process_request+0x4bb>
    1ccc:	83 bd 9c fb ff ff ff 	cmpl   $0xffffffff,-0x464(%rbp)
    1cd3:	75 09                	jne    1cde <process_request+0x4b2>
    1cd5:	48 8d 05 91 13 00 00 	lea    0x1391(%rip),%rax        # 306d <_IO_stdin_used+0x6d>
    1cdc:	eb 10                	jmp    1cee <process_request+0x4c2>
    1cde:	48 8d 05 8f 13 00 00 	lea    0x138f(%rip),%rax        # 3074 <_IO_stdin_used+0x74>
    1ce5:	eb 07                	jmp    1cee <process_request+0x4c2>
    1ce7:	48 8d 05 8b 13 00 00 	lea    0x138b(%rip),%rax        # 3079 <_IO_stdin_used+0x79>
    1cee:	48 8d 8d f0 fb ff ff 	lea    -0x410(%rbp),%rcx
    1cf5:	48 89 c2             	mov    %rax,%rdx
    1cf8:	be 00 04 00 00       	mov    $0x400,%esi
    1cfd:	48 89 cf             	mov    %rcx,%rdi
    1d00:	b8 00 00 00 00       	mov    $0x0,%eax
    1d05:	e8 b6 f4 ff ff       	call   11c0 <snprintf@plt>
    1d0a:	83 bd 9c fb ff ff 00 	cmpl   $0x0,-0x464(%rbp)
    1d11:	75 07                	jne    1d1a <process_request+0x4ee>
    1d13:	b8 c8 00 00 00       	mov    $0xc8,%eax
    1d18:	eb 05                	jmp    1d1f <process_request+0x4f3>
    1d1a:	b8 90 01 00 00       	mov    $0x190,%eax
    1d1f:	89 85 84 fb ff ff    	mov    %eax,-0x47c(%rbp)
    1d25:	e9 92 02 00 00       	jmp    1fbc <process_request+0x790>
    1d2a:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1d31:	48 8d 15 47 13 00 00 	lea    0x1347(%rip),%rdx        # 307f <_IO_stdin_used+0x7f>
    1d38:	be 00 04 00 00       	mov    $0x400,%esi
    1d3d:	48 89 c7             	mov    %rax,%rdi
    1d40:	b8 00 00 00 00       	mov    $0x0,%eax
    1d45:	e8 76 f4 ff ff       	call   11c0 <snprintf@plt>
    1d4a:	c7 85 84 fb ff ff 90 	movl   $0x190,-0x47c(%rbp)
    1d51:	01 00 00 
    1d54:	e9 63 02 00 00       	jmp    1fbc <process_request+0x790>
    1d59:	48 8b 85 60 fb ff ff 	mov    -0x4a0(%rbp),%rax
    1d60:	48 8d 15 27 13 00 00 	lea    0x1327(%rip),%rdx        # 308e <_IO_stdin_used+0x8e>
    1d67:	48 89 d6             	mov    %rdx,%rsi
    1d6a:	48 89 c7             	mov    %rax,%rdi
    1d6d:	e8 0e f5 ff ff       	call   1280 <strcmp@plt>
    1d72:	85 c0                	test   %eax,%eax
    1d74:	0f 85 53 01 00 00    	jne    1ecd <process_request+0x6a1>
    1d7a:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1d81:	ba 07 00 00 00       	mov    $0x7,%edx
    1d86:	48 8d 0d 9e 12 00 00 	lea    0x129e(%rip),%rcx        # 302b <_IO_stdin_used+0x2b>
    1d8d:	48 89 ce             	mov    %rcx,%rsi
    1d90:	48 89 c7             	mov    %rax,%rdi
    1d93:	e8 58 f4 ff ff       	call   11f0 <strncmp@plt>
    1d98:	85 c0                	test   %eax,%eax
    1d9a:	0f 85 1c 02 00 00    	jne    1fbc <process_request+0x790>
    1da0:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1da7:	48 83 c0 07          	add    $0x7,%rax
    1dab:	48 89 c7             	mov    %rax,%rdi
    1dae:	e8 8d f4 ff ff       	call   1240 <atoi@plt>
    1db3:	89 85 90 fb ff ff    	mov    %eax,-0x470(%rbp)
    1db9:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1dc0:	48 8b 00             	mov    (%rax),%rax
    1dc3:	48 85 c0             	test   %rax,%rax
    1dc6:	75 2f                	jne    1df7 <process_request+0x5cb>
    1dc8:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1dcf:	48 8d 15 78 12 00 00 	lea    0x1278(%rip),%rdx        # 304e <_IO_stdin_used+0x4e>
    1dd6:	be 00 04 00 00       	mov    $0x400,%esi
    1ddb:	48 89 c7             	mov    %rax,%rdi
    1dde:	b8 00 00 00 00       	mov    $0x0,%eax
    1de3:	e8 d8 f3 ff ff       	call   11c0 <snprintf@plt>
    1de8:	c7 85 84 fb ff ff 90 	movl   $0x190,-0x47c(%rbp)
    1def:	01 00 00 
    1df2:	e9 c5 01 00 00       	jmp    1fbc <process_request+0x790>
    1df7:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    1dfe:	48 8b 00             	mov    (%rax),%rax
    1e01:	48 8d 15 5f 12 00 00 	lea    0x125f(%rip),%rdx        # 3067 <_IO_stdin_used+0x67>
    1e08:	48 89 d6             	mov    %rdx,%rsi
    1e0b:	48 89 c7             	mov    %rax,%rdi
    1e0e:	e8 1d f4 ff ff       	call   1230 <strstr@plt>
    1e13:	48 89 85 b0 fb ff ff 	mov    %rax,-0x450(%rbp)
    1e1a:	48 83 bd b0 fb ff ff 	cmpq   $0x0,-0x450(%rbp)
    1e21:	00 
    1e22:	74 7a                	je     1e9e <process_request+0x672>
    1e24:	48 83 85 b0 fb ff ff 	addq   $0x5,-0x450(%rbp)
    1e2b:	05 
    1e2c:	48 8b 95 b0 fb ff ff 	mov    -0x450(%rbp),%rdx
    1e33:	8b 85 90 fb ff ff    	mov    -0x470(%rbp),%eax
    1e39:	48 89 d6             	mov    %rdx,%rsi
    1e3c:	89 c7                	mov    %eax,%edi
    1e3e:	e8 aa f7 ff ff       	call   15ed <modify_record>
    1e43:	89 85 94 fb ff ff    	mov    %eax,-0x46c(%rbp)
    1e49:	83 bd 94 fb ff ff 00 	cmpl   $0x0,-0x46c(%rbp)
    1e50:	75 09                	jne    1e5b <process_request+0x62f>
    1e52:	48 8d 05 39 12 00 00 	lea    0x1239(%rip),%rax        # 3092 <_IO_stdin_used+0x92>
    1e59:	eb 07                	jmp    1e62 <process_request+0x636>
    1e5b:	48 8d 05 e2 11 00 00 	lea    0x11e2(%rip),%rax        # 3044 <_IO_stdin_used+0x44>
    1e62:	48 8d 8d f0 fb ff ff 	lea    -0x410(%rbp),%rcx
    1e69:	48 89 c2             	mov    %rax,%rdx
    1e6c:	be 00 04 00 00       	mov    $0x400,%esi
    1e71:	48 89 cf             	mov    %rcx,%rdi
    1e74:	b8 00 00 00 00       	mov    $0x0,%eax
    1e79:	e8 42 f3 ff ff       	call   11c0 <snprintf@plt>
    1e7e:	83 bd 94 fb ff ff 00 	cmpl   $0x0,-0x46c(%rbp)
    1e85:	75 07                	jne    1e8e <process_request+0x662>
    1e87:	b8 c8 00 00 00       	mov    $0xc8,%eax
    1e8c:	eb 05                	jmp    1e93 <process_request+0x667>
    1e8e:	b8 94 01 00 00       	mov    $0x194,%eax
    1e93:	89 85 84 fb ff ff    	mov    %eax,-0x47c(%rbp)
    1e99:	e9 1e 01 00 00       	jmp    1fbc <process_request+0x790>
    1e9e:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1ea5:	48 8d 15 d3 11 00 00 	lea    0x11d3(%rip),%rdx        # 307f <_IO_stdin_used+0x7f>
    1eac:	be 00 04 00 00       	mov    $0x400,%esi
    1eb1:	48 89 c7             	mov    %rax,%rdi
    1eb4:	b8 00 00 00 00       	mov    $0x0,%eax
    1eb9:	e8 02 f3 ff ff       	call   11c0 <snprintf@plt>
    1ebe:	c7 85 84 fb ff ff 90 	movl   $0x190,-0x47c(%rbp)
    1ec5:	01 00 00 
    1ec8:	e9 ef 00 00 00       	jmp    1fbc <process_request+0x790>
    1ecd:	48 8b 85 60 fb ff ff 	mov    -0x4a0(%rbp),%rax
    1ed4:	48 8d 15 bf 11 00 00 	lea    0x11bf(%rip),%rdx        # 309a <_IO_stdin_used+0x9a>
    1edb:	48 89 d6             	mov    %rdx,%rsi
    1ede:	48 89 c7             	mov    %rax,%rdi
    1ee1:	e8 9a f3 ff ff       	call   1280 <strcmp@plt>
    1ee6:	85 c0                	test   %eax,%eax
    1ee8:	0f 85 a4 00 00 00    	jne    1f92 <process_request+0x766>
    1eee:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1ef5:	ba 07 00 00 00       	mov    $0x7,%edx
    1efa:	48 8d 0d 2a 11 00 00 	lea    0x112a(%rip),%rcx        # 302b <_IO_stdin_used+0x2b>
    1f01:	48 89 ce             	mov    %rcx,%rsi
    1f04:	48 89 c7             	mov    %rax,%rdi
    1f07:	e8 e4 f2 ff ff       	call   11f0 <strncmp@plt>
    1f0c:	85 c0                	test   %eax,%eax
    1f0e:	0f 85 a8 00 00 00    	jne    1fbc <process_request+0x790>
    1f14:	48 8b 85 68 fb ff ff 	mov    -0x498(%rbp),%rax
    1f1b:	48 83 c0 07          	add    $0x7,%rax
    1f1f:	48 89 c7             	mov    %rax,%rdi
    1f22:	e8 19 f3 ff ff       	call   1240 <atoi@plt>
    1f27:	89 85 88 fb ff ff    	mov    %eax,-0x478(%rbp)
    1f2d:	8b 85 88 fb ff ff    	mov    -0x478(%rbp),%eax
    1f33:	89 c7                	mov    %eax,%edi
    1f35:	e8 3f f7 ff ff       	call   1679 <erase_record>
    1f3a:	89 85 8c fb ff ff    	mov    %eax,-0x474(%rbp)
    1f40:	83 bd 8c fb ff ff 00 	cmpl   $0x0,-0x474(%rbp)
    1f47:	75 09                	jne    1f52 <process_request+0x726>
    1f49:	48 8d 05 51 11 00 00 	lea    0x1151(%rip),%rax        # 30a1 <_IO_stdin_used+0xa1>
    1f50:	eb 07                	jmp    1f59 <process_request+0x72d>
    1f52:	48 8d 05 eb 10 00 00 	lea    0x10eb(%rip),%rax        # 3044 <_IO_stdin_used+0x44>
    1f59:	48 8d 8d f0 fb ff ff 	lea    -0x410(%rbp),%rcx
    1f60:	48 89 c2             	mov    %rax,%rdx
    1f63:	be 00 04 00 00       	mov    $0x400,%esi
    1f68:	48 89 cf             	mov    %rcx,%rdi
    1f6b:	b8 00 00 00 00       	mov    $0x0,%eax
    1f70:	e8 4b f2 ff ff       	call   11c0 <snprintf@plt>
    1f75:	83 bd 8c fb ff ff 00 	cmpl   $0x0,-0x474(%rbp)
    1f7c:	75 07                	jne    1f85 <process_request+0x759>
    1f7e:	b8 c8 00 00 00       	mov    $0xc8,%eax
    1f83:	eb 05                	jmp    1f8a <process_request+0x75e>
    1f85:	b8 94 01 00 00       	mov    $0x194,%eax
    1f8a:	89 85 84 fb ff ff    	mov    %eax,-0x47c(%rbp)
    1f90:	eb 2a                	jmp    1fbc <process_request+0x790>
    1f92:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1f99:	48 8d 15 09 11 00 00 	lea    0x1109(%rip),%rdx        # 30a9 <_IO_stdin_used+0xa9>
    1fa0:	be 00 04 00 00       	mov    $0x400,%esi
    1fa5:	48 89 c7             	mov    %rax,%rdi
    1fa8:	b8 00 00 00 00       	mov    $0x0,%eax
    1fad:	e8 0e f2 ff ff       	call   11c0 <snprintf@plt>
    1fb2:	c7 85 84 fb ff ff 95 	movl   $0x195,-0x47c(%rbp)
    1fb9:	01 00 00 
    1fbc:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1fc3:	48 89 c7             	mov    %rax,%rdi
    1fc6:	e8 55 f2 ff ff       	call   1220 <strlen@plt>
    1fcb:	48 89 c1             	mov    %rax,%rcx
    1fce:	48 8d 85 f0 fb ff ff 	lea    -0x410(%rbp),%rax
    1fd5:	ba 02 00 00 00       	mov    $0x2,%edx
    1fda:	48 89 c6             	mov    %rax,%rsi
    1fdd:	48 89 cf             	mov    %rcx,%rdi
    1fe0:	e8 ab f2 ff ff       	call   1290 <MHD_create_response_from_buffer@plt>
    1fe5:	48 89 85 d0 fb ff ff 	mov    %rax,-0x430(%rbp)
    1fec:	8b 8d 84 fb ff ff    	mov    -0x47c(%rbp),%ecx
    1ff2:	48 8b 95 d0 fb ff ff 	mov    -0x430(%rbp),%rdx
    1ff9:	48 8b 85 70 fb ff ff 	mov    -0x490(%rbp),%rax
    2000:	89 ce                	mov    %ecx,%esi
    2002:	48 89 c7             	mov    %rax,%rdi
    2005:	e8 d6 f1 ff ff       	call   11e0 <MHD_queue_response@plt>
    200a:	89 85 a4 fb ff ff    	mov    %eax,-0x45c(%rbp)
    2010:	48 8b 85 d0 fb ff ff 	mov    -0x430(%rbp),%rax
    2017:	48 89 c7             	mov    %rax,%rdi
    201a:	e8 91 f2 ff ff       	call   12b0 <MHD_destroy_response@plt>
    201f:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    2026:	48 8b 00             	mov    (%rax),%rax
    2029:	48 85 c0             	test   %rax,%rax
    202c:	74 12                	je     2040 <process_request+0x814>
    202e:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    2035:	48 8b 00             	mov    (%rax),%rax
    2038:	48 89 c7             	mov    %rax,%rdi
    203b:	e8 d0 f1 ff ff       	call   1210 <free@plt>
    2040:	48 8b 85 a8 fb ff ff 	mov    -0x458(%rbp),%rax
    2047:	48 89 c7             	mov    %rax,%rdi
    204a:	e8 c1 f1 ff ff       	call   1210 <free@plt>
    204f:	48 8b 85 40 fb ff ff 	mov    -0x4c0(%rbp),%rax
    2056:	48 c7 00 00 00 00 00 	movq   $0x0,(%rax)
    205d:	8b 85 a4 fb ff ff    	mov    -0x45c(%rbp),%eax
    2063:	48 8b 55 f8          	mov    -0x8(%rbp),%rdx
    2067:	64 48 2b 14 25 28 00 	sub    %fs:0x28,%rdx
    206e:	00 00 
    2070:	74 05                	je     2077 <process_request+0x84b>
    2072:	e8 f9 f1 ff ff       	call   1270 <__stack_chk_fail@plt>
    2077:	c9                   	leave  
    2078:	c3                   	ret    

0000000000002079 <main>:
    2079:	f3 0f 1e fa          	endbr64 
    207d:	55                   	push   %rbp
    207e:	48 89 e5             	mov    %rsp,%rbp
    2081:	48 83 ec 10          	sub    $0x10,%rsp
    2085:	b8 00 00 00 00       	mov    $0x0,%eax
    208a:	e8 5a f3 ff ff       	call   13e9 <initialize_database>
    208f:	48 83 ec 08          	sub    $0x8,%rsp
    2093:	6a 00                	push   $0x0
    2095:	41 b9 00 00 00 00    	mov    $0x0,%r9d
    209b:	4c 8d 05 8a f7 ff ff 	lea    -0x876(%rip),%r8        # 182c <process_request>
    20a2:	b9 00 00 00 00       	mov    $0x0,%ecx
    20a7:	ba 00 00 00 00       	mov    $0x0,%edx
    20ac:	be b8 22 00 00       	mov    $0x22b8,%esi
    20b1:	bf 08 00 00 00       	mov    $0x8,%edi
    20b6:	b8 00 00 00 00       	mov    $0x0,%eax
    20bb:	e8 90 f1 ff ff       	call   1250 <MHD_start_daemon@plt>
    20c0:	48 83 c4 10          	add    $0x10,%rsp
    20c4:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    20c8:	48 83 7d f8 00       	cmpq   $0x0,-0x8(%rbp)
    20cd:	75 2a                	jne    20f9 <main+0x80>
    20cf:	48 8b 05 4a 2f 00 00 	mov    0x2f4a(%rip),%rax        # 5020 <stderr@GLIBC_2.2.5>
    20d6:	48 89 c1             	mov    %rax,%rcx
    20d9:	ba 17 00 00 00       	mov    $0x17,%edx
    20de:	be 01 00 00 00       	mov    $0x1,%esi
    20e3:	48 8d 05 cb 0f 00 00 	lea    0xfcb(%rip),%rax        # 30b5 <_IO_stdin_used+0xb5>
    20ea:	48 89 c7             	mov    %rax,%rdi
    20ed:	e8 ce f1 ff ff       	call   12c0 <fwrite@plt>
    20f2:	b8 01 00 00 00       	mov    $0x1,%eax
    20f7:	eb 2f                	jmp    2128 <main+0xaf>
    20f9:	be b8 22 00 00       	mov    $0x22b8,%esi
    20fe:	48 8d 05 c8 0f 00 00 	lea    0xfc8(%rip),%rax        # 30cd <_IO_stdin_used+0xcd>
    2105:	48 89 c7             	mov    %rax,%rdi
    2108:	b8 00 00 00 00       	mov    $0x0,%eax
    210d:	e8 8e f0 ff ff       	call   11a0 <printf@plt>
    2112:	e8 49 f1 ff ff       	call   1260 <getchar@plt>
    2117:	48 8b 45 f8          	mov    -0x8(%rbp),%rax
    211b:	48 89 c7             	mov    %rax,%rdi
    211e:	e8 bd f1 ff ff       	call   12e0 <MHD_stop_daemon@plt>
    2123:	b8 00 00 00 00       	mov    $0x0,%eax
    2128:	c9                   	leave  
    2129:	c3                   	ret    

Disassembly of section .fini:

000000000000212c <_fini>:
    212c:	f3 0f 1e fa          	endbr64 
    2130:	48 83 ec 08          	sub    $0x8,%rsp
    2134:	48 83 c4 08          	add    $0x8,%rsp
    2138:	c3                   	ret    
