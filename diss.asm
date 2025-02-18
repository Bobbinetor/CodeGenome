
rest_api:	file format mach-o arm64

Disassembly of section __TEXT,__text:

0000000100002f18 <_init_store>:
100002f18: d10043ff    	sub	sp, sp, #0x10
100002f1c: b9000fff    	str	wzr, [sp, #0xc]
100002f20: 14000001    	b	0x100002f24 <_init_store+0xc>
100002f24: b9400fe8    	ldr	w8, [sp, #0xc]
100002f28: 71002908    	subs	w8, w8, #0xa
100002f2c: 1a9fb7e8    	cset	w8, ge
100002f30: 370001c8    	tbnz	w8, #0x0, 0x100002f68 <_init_store+0x50>
100002f34: 14000001    	b	0x100002f38 <_init_store+0x20>
100002f38: b9800fe8    	ldrsw	x8, [sp, #0xc]
100002f3c: d2802109    	mov	x9, #0x108              ; =264
100002f40: 9b097d09    	mul	x9, x8, x9
100002f44: d0000028    	adrp	x8, 0x100008000 <_store>
100002f48: 91000108    	add	x8, x8, #0x0
100002f4c: 8b090108    	add	x8, x8, x9
100002f50: b901051f    	str	wzr, [x8, #0x104]
100002f54: 14000001    	b	0x100002f58 <_init_store+0x40>
100002f58: b9400fe8    	ldr	w8, [sp, #0xc]
100002f5c: 11000508    	add	w8, w8, #0x1
100002f60: b9000fe8    	str	w8, [sp, #0xc]
100002f64: 17fffff0    	b	0x100002f24 <_init_store+0xc>
100002f68: 910043ff    	add	sp, sp, #0x10
100002f6c: d65f03c0    	ret

0000000100002f70 <_find_index>:
100002f70: d10043ff    	sub	sp, sp, #0x10
100002f74: b9000be0    	str	w0, [sp, #0x8]
100002f78: b90007ff    	str	wzr, [sp, #0x4]
100002f7c: 14000001    	b	0x100002f80 <_find_index+0x10>
100002f80: b94007e8    	ldr	w8, [sp, #0x4]
100002f84: 71002908    	subs	w8, w8, #0xa
100002f88: 1a9fb7e8    	cset	w8, ge
100002f8c: 37000408    	tbnz	w8, #0x0, 0x10000300c <_find_index+0x9c>
100002f90: 14000001    	b	0x100002f94 <_find_index+0x24>
100002f94: b98007e8    	ldrsw	x8, [sp, #0x4]
100002f98: d2802109    	mov	x9, #0x108              ; =264
100002f9c: 9b097d09    	mul	x9, x8, x9
100002fa0: d0000028    	adrp	x8, 0x100008000 <_store>
100002fa4: 91000108    	add	x8, x8, #0x0
100002fa8: 8b090108    	add	x8, x8, x9
100002fac: b9410508    	ldr	w8, [x8, #0x104]
100002fb0: 71000108    	subs	w8, w8, #0x0
100002fb4: 1a9f17e8    	cset	w8, eq
100002fb8: 37000208    	tbnz	w8, #0x0, 0x100002ff8 <_find_index+0x88>
100002fbc: 14000001    	b	0x100002fc0 <_find_index+0x50>
100002fc0: b98007e8    	ldrsw	x8, [sp, #0x4]
100002fc4: d2802109    	mov	x9, #0x108              ; =264
100002fc8: 9b097d09    	mul	x9, x8, x9
100002fcc: d0000028    	adrp	x8, 0x100008000 <_store>
100002fd0: 91000108    	add	x8, x8, #0x0
100002fd4: b8696908    	ldr	w8, [x8, x9]
100002fd8: b9400be9    	ldr	w9, [sp, #0x8]
100002fdc: 6b090108    	subs	w8, w8, w9
100002fe0: 1a9f07e8    	cset	w8, ne
100002fe4: 370000a8    	tbnz	w8, #0x0, 0x100002ff8 <_find_index+0x88>
100002fe8: 14000001    	b	0x100002fec <_find_index+0x7c>
100002fec: b94007e8    	ldr	w8, [sp, #0x4]
100002ff0: b9000fe8    	str	w8, [sp, #0xc]
100002ff4: 14000009    	b	0x100003018 <_find_index+0xa8>
100002ff8: 14000001    	b	0x100002ffc <_find_index+0x8c>
100002ffc: b94007e8    	ldr	w8, [sp, #0x4]
100003000: 11000508    	add	w8, w8, #0x1
100003004: b90007e8    	str	w8, [sp, #0x4]
100003008: 17ffffde    	b	0x100002f80 <_find_index+0x10>
10000300c: 12800008    	mov	w8, #-0x1               ; =-1
100003010: b9000fe8    	str	w8, [sp, #0xc]
100003014: 14000001    	b	0x100003018 <_find_index+0xa8>
100003018: b9400fe0    	ldr	w0, [sp, #0xc]
10000301c: 910043ff    	add	sp, sp, #0x10
100003020: d65f03c0    	ret

0000000100003024 <_add_item>:
100003024: d10103ff    	sub	sp, sp, #0x40
100003028: a9037bfd    	stp	x29, x30, [sp, #0x30]
10000302c: 9100c3fd    	add	x29, sp, #0x30
100003030: b81f83a0    	stur	w0, [x29, #-0x8]
100003034: f81f03a1    	stur	x1, [x29, #-0x10]
100003038: b85f83a0    	ldur	w0, [x29, #-0x8]
10000303c: 97ffffcd    	bl	0x100002f70 <_find_index>
100003040: 31000408    	adds	w8, w0, #0x1
100003044: 1a9f17e8    	cset	w8, eq
100003048: 370000a8    	tbnz	w8, #0x0, 0x10000305c <_add_item+0x38>
10000304c: 14000001    	b	0x100003050 <_add_item+0x2c>
100003050: 12800008    	mov	w8, #-0x1               ; =-1
100003054: b81fc3a8    	stur	w8, [x29, #-0x4]
100003058: 1400003a    	b	0x100003140 <_add_item+0x11c>
10000305c: b81ec3bf    	stur	wzr, [x29, #-0x14]
100003060: 14000001    	b	0x100003064 <_add_item+0x40>
100003064: b85ec3a8    	ldur	w8, [x29, #-0x14]
100003068: 71002908    	subs	w8, w8, #0xa
10000306c: 1a9fb7e8    	cset	w8, ge
100003070: 37000628    	tbnz	w8, #0x0, 0x100003134 <_add_item+0x110>
100003074: 14000001    	b	0x100003078 <_add_item+0x54>
100003078: b89ec3a8    	ldursw	x8, [x29, #-0x14]
10000307c: d2802109    	mov	x9, #0x108              ; =264
100003080: 9b097d09    	mul	x9, x8, x9
100003084: b0000028    	adrp	x8, 0x100008000 <_store>
100003088: 91000108    	add	x8, x8, #0x0
10000308c: 8b090108    	add	x8, x8, x9
100003090: b9410508    	ldr	w8, [x8, #0x104]
100003094: 71000108    	subs	w8, w8, #0x0
100003098: 1a9f07e8    	cset	w8, ne
10000309c: 37000428    	tbnz	w8, #0x0, 0x100003120 <_add_item+0xfc>
1000030a0: 14000001    	b	0x1000030a4 <_add_item+0x80>
1000030a4: b85f83a9    	ldur	w9, [x29, #-0x8]
1000030a8: b89ec3a8    	ldursw	x8, [x29, #-0x14]
1000030ac: d280210a    	mov	x10, #0x108             ; =264
1000030b0: f90007ea    	str	x10, [sp, #0x8]
1000030b4: 9b0a7d0b    	mul	x11, x8, x10
1000030b8: b0000028    	adrp	x8, 0x100008000 <_store>
1000030bc: 91000108    	add	x8, x8, #0x0
1000030c0: f9000be8    	str	x8, [sp, #0x10]
1000030c4: b82b6909    	str	w9, [x8, x11]
1000030c8: b89ec3a9    	ldursw	x9, [x29, #-0x14]
1000030cc: 9b0a7d29    	mul	x9, x9, x10
1000030d0: 8b090108    	add	x8, x8, x9
1000030d4: 91001100    	add	x0, x8, #0x4
1000030d8: f85f03a1    	ldur	x1, [x29, #-0x10]
1000030dc: d2801fe2    	mov	x2, #0xff               ; =255
1000030e0: d2802003    	mov	x3, #0x100              ; =256
1000030e4: 94000342    	bl	0x100003dec <_strstr+0x100003dec>
1000030e8: f94007ea    	ldr	x10, [sp, #0x8]
1000030ec: f9400be8    	ldr	x8, [sp, #0x10]
1000030f0: b89ec3a9    	ldursw	x9, [x29, #-0x14]
1000030f4: 9b0a7d2b    	mul	x11, x9, x10
1000030f8: aa0803e9    	mov	x9, x8
1000030fc: 8b0b0129    	add	x9, x9, x11
100003100: 39040d3f    	strb	wzr, [x9, #0x103]
100003104: b89ec3a9    	ldursw	x9, [x29, #-0x14]
100003108: 9b0a7d29    	mul	x9, x9, x10
10000310c: 8b090109    	add	x9, x8, x9
100003110: 52800028    	mov	w8, #0x1                ; =1
100003114: b9010528    	str	w8, [x9, #0x104]
100003118: b81fc3bf    	stur	wzr, [x29, #-0x4]
10000311c: 14000009    	b	0x100003140 <_add_item+0x11c>
100003120: 14000001    	b	0x100003124 <_add_item+0x100>
100003124: b85ec3a8    	ldur	w8, [x29, #-0x14]
100003128: 11000508    	add	w8, w8, #0x1
10000312c: b81ec3a8    	stur	w8, [x29, #-0x14]
100003130: 17ffffcd    	b	0x100003064 <_add_item+0x40>
100003134: 12800028    	mov	w8, #-0x2               ; =-2
100003138: b81fc3a8    	stur	w8, [x29, #-0x4]
10000313c: 14000001    	b	0x100003140 <_add_item+0x11c>
100003140: b85fc3a0    	ldur	w0, [x29, #-0x4]
100003144: a9437bfd    	ldp	x29, x30, [sp, #0x30]
100003148: 910103ff    	add	sp, sp, #0x40
10000314c: d65f03c0    	ret

0000000100003150 <_get_item_data>:
100003150: d10083ff    	sub	sp, sp, #0x20
100003154: a9017bfd    	stp	x29, x30, [sp, #0x10]
100003158: 910043fd    	add	x29, sp, #0x10
10000315c: b90007e0    	str	w0, [sp, #0x4]
100003160: b94007e0    	ldr	w0, [sp, #0x4]
100003164: 97ffff83    	bl	0x100002f70 <_find_index>
100003168: b90003e0    	str	w0, [sp]
10000316c: b94003e8    	ldr	w8, [sp]
100003170: 31000508    	adds	w8, w8, #0x1
100003174: 1a9f17e8    	cset	w8, eq
100003178: 37000168    	tbnz	w8, #0x0, 0x1000031a4 <_get_item_data+0x54>
10000317c: 14000001    	b	0x100003180 <_get_item_data+0x30>
100003180: b98003e8    	ldrsw	x8, [sp]
100003184: d2802109    	mov	x9, #0x108              ; =264
100003188: 9b097d09    	mul	x9, x8, x9
10000318c: b0000028    	adrp	x8, 0x100008000 <_store>
100003190: 91000108    	add	x8, x8, #0x0
100003194: 8b090108    	add	x8, x8, x9
100003198: 91001108    	add	x8, x8, #0x4
10000319c: f90007e8    	str	x8, [sp, #0x8]
1000031a0: 14000003    	b	0x1000031ac <_get_item_data+0x5c>
1000031a4: f90007ff    	str	xzr, [sp, #0x8]
1000031a8: 14000001    	b	0x1000031ac <_get_item_data+0x5c>
1000031ac: f94007e0    	ldr	x0, [sp, #0x8]
1000031b0: a9417bfd    	ldp	x29, x30, [sp, #0x10]
1000031b4: 910083ff    	add	sp, sp, #0x20
1000031b8: d65f03c0    	ret

00000001000031bc <_update_item>:
1000031bc: d10103ff    	sub	sp, sp, #0x40
1000031c0: a9037bfd    	stp	x29, x30, [sp, #0x30]
1000031c4: 9100c3fd    	add	x29, sp, #0x30
1000031c8: b81f83a0    	stur	w0, [x29, #-0x8]
1000031cc: f81f03a1    	stur	x1, [x29, #-0x10]
1000031d0: b85f83a0    	ldur	w0, [x29, #-0x8]
1000031d4: 97ffff67    	bl	0x100002f70 <_find_index>
1000031d8: b81ec3a0    	stur	w0, [x29, #-0x14]
1000031dc: b85ec3a8    	ldur	w8, [x29, #-0x14]
1000031e0: 31000508    	adds	w8, w8, #0x1
1000031e4: 1a9f07e8    	cset	w8, ne
1000031e8: 370000a8    	tbnz	w8, #0x0, 0x1000031fc <_update_item+0x40>
1000031ec: 14000001    	b	0x1000031f0 <_update_item+0x34>
1000031f0: 12800008    	mov	w8, #-0x1               ; =-1
1000031f4: b81fc3a8    	stur	w8, [x29, #-0x4]
1000031f8: 14000016    	b	0x100003250 <_update_item+0x94>
1000031fc: b89ec3a8    	ldursw	x8, [x29, #-0x14]
100003200: d2802109    	mov	x9, #0x108              ; =264
100003204: f90007e9    	str	x9, [sp, #0x8]
100003208: 9b097d09    	mul	x9, x8, x9
10000320c: b0000028    	adrp	x8, 0x100008000 <_store>
100003210: 91000108    	add	x8, x8, #0x0
100003214: f9000be8    	str	x8, [sp, #0x10]
100003218: 8b090108    	add	x8, x8, x9
10000321c: 91001100    	add	x0, x8, #0x4
100003220: f85f03a1    	ldur	x1, [x29, #-0x10]
100003224: d2801fe2    	mov	x2, #0xff               ; =255
100003228: d2802003    	mov	x3, #0x100              ; =256
10000322c: 940002f0    	bl	0x100003dec <_strstr+0x100003dec>
100003230: f94007ea    	ldr	x10, [sp, #0x8]
100003234: f9400be8    	ldr	x8, [sp, #0x10]
100003238: b89ec3a9    	ldursw	x9, [x29, #-0x14]
10000323c: 9b0a7d29    	mul	x9, x9, x10
100003240: 8b090108    	add	x8, x8, x9
100003244: 39040d1f    	strb	wzr, [x8, #0x103]
100003248: b81fc3bf    	stur	wzr, [x29, #-0x4]
10000324c: 14000001    	b	0x100003250 <_update_item+0x94>
100003250: b85fc3a0    	ldur	w0, [x29, #-0x4]
100003254: a9437bfd    	ldp	x29, x30, [sp, #0x30]
100003258: 910103ff    	add	sp, sp, #0x40
10000325c: d65f03c0    	ret

0000000100003260 <_delete_item>:
100003260: d10083ff    	sub	sp, sp, #0x20
100003264: a9017bfd    	stp	x29, x30, [sp, #0x10]
100003268: 910043fd    	add	x29, sp, #0x10
10000326c: b9000be0    	str	w0, [sp, #0x8]
100003270: b9400be0    	ldr	w0, [sp, #0x8]
100003274: 97ffff3f    	bl	0x100002f70 <_find_index>
100003278: b90007e0    	str	w0, [sp, #0x4]
10000327c: b94007e8    	ldr	w8, [sp, #0x4]
100003280: 31000508    	adds	w8, w8, #0x1
100003284: 1a9f07e8    	cset	w8, ne
100003288: 370000a8    	tbnz	w8, #0x0, 0x10000329c <_delete_item+0x3c>
10000328c: 14000001    	b	0x100003290 <_delete_item+0x30>
100003290: 12800008    	mov	w8, #-0x1               ; =-1
100003294: b81fc3a8    	stur	w8, [x29, #-0x4]
100003298: 1400000a    	b	0x1000032c0 <_delete_item+0x60>
10000329c: b98007e8    	ldrsw	x8, [sp, #0x4]
1000032a0: d2802109    	mov	x9, #0x108              ; =264
1000032a4: 9b097d09    	mul	x9, x8, x9
1000032a8: b0000028    	adrp	x8, 0x100008000 <_store>
1000032ac: 91000108    	add	x8, x8, #0x0
1000032b0: 8b090108    	add	x8, x8, x9
1000032b4: b901051f    	str	wzr, [x8, #0x104]
1000032b8: b81fc3bf    	stur	wzr, [x29, #-0x4]
1000032bc: 14000001    	b	0x1000032c0 <_delete_item+0x60>
1000032c0: b85fc3a0    	ldur	w0, [x29, #-0x4]
1000032c4: a9417bfd    	ldp	x29, x30, [sp, #0x10]
1000032c8: 910083ff    	add	sp, sp, #0x20
1000032cc: d65f03c0    	ret

00000001000032d0 <_list_items_str>:
1000032d0: d10683ff    	sub	sp, sp, #0x1a0
1000032d4: a9186ffc    	stp	x28, x27, [sp, #0x180]
1000032d8: a9197bfd    	stp	x29, x30, [sp, #0x190]
1000032dc: 910643fd    	add	x29, sp, #0x190
1000032e0: b0000008    	adrp	x8, 0x100004000 <_strstr+0x100004000>
1000032e4: f9402108    	ldr	x8, [x8, #0x40]
1000032e8: f9400108    	ldr	x8, [x8]
1000032ec: f81e83a8    	stur	x8, [x29, #-0x18]
1000032f0: f90023e0    	str	x0, [sp, #0x40]
1000032f4: f9001fe1    	str	x1, [sp, #0x38]
1000032f8: f94023e0    	ldr	x0, [sp, #0x40]
1000032fc: f9401fe1    	ldr	x1, [sp, #0x38]
100003300: 52800002    	mov	w2, #0x0                ; =0
100003304: 92800003    	mov	x3, #-0x1               ; =-1
100003308: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
10000330c: 913a2084    	add	x4, x4, #0xe88
100003310: 940002ae    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003314: b90037ff    	str	wzr, [sp, #0x34]
100003318: 14000001    	b	0x10000331c <_list_items_str+0x4c>
10000331c: b94037e8    	ldr	w8, [sp, #0x34]
100003320: 71002908    	subs	w8, w8, #0xa
100003324: 1a9fb7e8    	cset	w8, ge
100003328: 370006e8    	tbnz	w8, #0x0, 0x100003404 <_list_items_str+0x134>
10000332c: 14000001    	b	0x100003330 <_list_items_str+0x60>
100003330: b98037e8    	ldrsw	x8, [sp, #0x34]
100003334: d2802109    	mov	x9, #0x108              ; =264
100003338: 9b097d09    	mul	x9, x8, x9
10000333c: b0000028    	adrp	x8, 0x100008000 <_store>
100003340: 91000108    	add	x8, x8, #0x0
100003344: 8b090108    	add	x8, x8, x9
100003348: b9410508    	ldr	w8, [x8, #0x104]
10000334c: 71000108    	subs	w8, w8, #0x0
100003350: 1a9f17e8    	cset	w8, eq
100003354: 370004e8    	tbnz	w8, #0x0, 0x1000033f0 <_list_items_str+0x120>
100003358: 14000001    	b	0x10000335c <_list_items_str+0x8c>
10000335c: b98037e8    	ldrsw	x8, [sp, #0x34]
100003360: d280210b    	mov	x11, #0x108             ; =264
100003364: 9b0b7d09    	mul	x9, x8, x11
100003368: b0000028    	adrp	x8, 0x100008000 <_store>
10000336c: 91000108    	add	x8, x8, #0x0
100003370: b8696909    	ldr	w9, [x8, x9]
100003374: aa0903ea    	mov	x10, x9
100003378: b98037e9    	ldrsw	x9, [sp, #0x34]
10000337c: 9b0b7d29    	mul	x9, x9, x11
100003380: 8b090108    	add	x8, x8, x9
100003384: 91001108    	add	x8, x8, #0x4
100003388: 910003e9    	mov	x9, sp
10000338c: f900012a    	str	x10, [x9]
100003390: f9000528    	str	x8, [x9, #0x8]
100003394: 910133e0    	add	x0, sp, #0x4c
100003398: f90013e0    	str	x0, [sp, #0x20]
10000339c: d2802583    	mov	x3, #0x12c              ; =300
1000033a0: aa0303e1    	mov	x1, x3
1000033a4: 52800002    	mov	w2, #0x0                ; =0
1000033a8: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
1000033ac: 913a4084    	add	x4, x4, #0xe90
1000033b0: 94000286    	bl	0x100003dc8 <_strstr+0x100003dc8>
1000033b4: f94023e8    	ldr	x8, [sp, #0x40]
1000033b8: f90017e8    	str	x8, [sp, #0x28]
1000033bc: f9401fe8    	ldr	x8, [sp, #0x38]
1000033c0: f9000fe8    	str	x8, [sp, #0x18]
1000033c4: f94023e0    	ldr	x0, [sp, #0x40]
1000033c8: 940002a7    	bl	0x100003e64 <_strstr+0x100003e64>
1000033cc: f9400fe8    	ldr	x8, [sp, #0x18]
1000033d0: f94013e1    	ldr	x1, [sp, #0x20]
1000033d4: aa0003e9    	mov	x9, x0
1000033d8: f94017e0    	ldr	x0, [sp, #0x28]
1000033dc: eb090108    	subs	x8, x8, x9
1000033e0: f1000502    	subs	x2, x8, #0x1
1000033e4: 92800003    	mov	x3, #-0x1               ; =-1
1000033e8: 9400027e    	bl	0x100003de0 <_strstr+0x100003de0>
1000033ec: 14000001    	b	0x1000033f0 <_list_items_str+0x120>
1000033f0: 14000001    	b	0x1000033f4 <_list_items_str+0x124>
1000033f4: b94037e8    	ldr	w8, [sp, #0x34]
1000033f8: 11000508    	add	w8, w8, #0x1
1000033fc: b90037e8    	str	w8, [sp, #0x34]
100003400: 17ffffc7    	b	0x10000331c <_list_items_str+0x4c>
100003404: f85e83a9    	ldur	x9, [x29, #-0x18]
100003408: b0000008    	adrp	x8, 0x100004000 <_strstr+0x100004000>
10000340c: f9402108    	ldr	x8, [x8, #0x40]
100003410: f9400108    	ldr	x8, [x8]
100003414: eb090108    	subs	x8, x8, x9
100003418: 1a9f17e8    	cset	w8, eq
10000341c: 37000068    	tbnz	w8, #0x0, 0x100003428 <_list_items_str+0x158>
100003420: 14000001    	b	0x100003424 <_list_items_str+0x154>
100003424: 9400026c    	bl	0x100003dd4 <_strstr+0x100003dd4>
100003428: a9597bfd    	ldp	x29, x30, [sp, #0x190]
10000342c: a9586ffc    	ldp	x28, x27, [sp, #0x180]
100003430: 910683ff    	add	sp, sp, #0x1a0
100003434: d65f03c0    	ret

0000000100003438 <_main>:
100003438: d100c3ff    	sub	sp, sp, #0x30
10000343c: a9027bfd    	stp	x29, x30, [sp, #0x20]
100003440: 910083fd    	add	x29, sp, #0x20
100003444: b81fc3bf    	stur	wzr, [x29, #-0x4]
100003448: 97fffeb4    	bl	0x100002f18 <_init_store>
10000344c: 910003e8    	mov	x8, sp
100003450: f900011f    	str	xzr, [x8]
100003454: 52800100    	mov	w0, #0x8                ; =8
100003458: 52845701    	mov	w1, #0x22b8             ; =8888
10000345c: d2800005    	mov	x5, #0x0                ; =0
100003460: aa0503e2    	mov	x2, x5
100003464: aa0503e3    	mov	x3, x5
100003468: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
10000346c: 9113b084    	add	x4, x4, #0x4ec
100003470: 9400024d    	bl	0x100003da4 <_strstr+0x100003da4>
100003474: f9000be0    	str	x0, [sp, #0x10]
100003478: f9400be8    	ldr	x8, [sp, #0x10]
10000347c: f1000108    	subs	x8, x8, #0x0
100003480: 1a9f07e8    	cset	w8, ne
100003484: 37000168    	tbnz	w8, #0x0, 0x1000034b0 <_main+0x78>
100003488: 14000001    	b	0x10000348c <_main+0x54>
10000348c: b0000008    	adrp	x8, 0x100004000 <_strstr+0x100004000>
100003490: f9402508    	ldr	x8, [x8, #0x48]
100003494: f9400100    	ldr	x0, [x8]
100003498: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
10000349c: 913a8821    	add	x1, x1, #0xea2
1000034a0: 9400025c    	bl	0x100003e10 <_strstr+0x100003e10>
1000034a4: 52800028    	mov	w8, #0x1                ; =1
1000034a8: b81fc3a8    	stur	w8, [x29, #-0x4]
1000034ac: 1400000c    	b	0x1000034dc <_main+0xa4>
1000034b0: 910003e9    	mov	x9, sp
1000034b4: d2845708    	mov	x8, #0x22b8             ; =8888
1000034b8: f9000128    	str	x8, [x9]
1000034bc: 90000000    	adrp	x0, 0x100003000 <_find_index+0x90>
1000034c0: 913ae800    	add	x0, x0, #0xeba
1000034c4: 9400025f    	bl	0x100003e40 <_strstr+0x100003e40>
1000034c8: 94000258    	bl	0x100003e28 <_strstr+0x100003e28>
1000034cc: f9400be0    	ldr	x0, [sp, #0x10]
1000034d0: 94000238    	bl	0x100003db0 <_strstr+0x100003db0>
1000034d4: b81fc3bf    	stur	wzr, [x29, #-0x4]
1000034d8: 14000001    	b	0x1000034dc <_main+0xa4>
1000034dc: b85fc3a0    	ldur	w0, [x29, #-0x4]
1000034e0: a9427bfd    	ldp	x29, x30, [sp, #0x20]
1000034e4: 9100c3ff    	add	sp, sp, #0x30
1000034e8: d65f03c0    	ret

00000001000034ec <_request_handler>:
1000034ec: a9be6ffc    	stp	x28, x27, [sp, #-0x20]!
1000034f0: a9017bfd    	stp	x29, x30, [sp, #0x10]
1000034f4: 910043fd    	add	x29, sp, #0x10
1000034f8: d113c3ff    	sub	sp, sp, #0x4f0
1000034fc: 9102c3e8    	add	x8, sp, #0xb0
100003500: f90013e8    	str	x8, [sp, #0x20]
100003504: b0000009    	adrp	x9, 0x100004000 <_strstr+0x100004000>
100003508: f9402129    	ldr	x9, [x9, #0x40]
10000350c: f9400129    	ldr	x9, [x9]
100003510: f81e83a9    	stur	x9, [x29, #-0x18]
100003514: f9001500    	str	x0, [x8, #0x28]
100003518: f9001101    	str	x1, [x8, #0x20]
10000351c: f9000d02    	str	x2, [x8, #0x18]
100003520: f9000903    	str	x3, [x8, #0x10]
100003524: f9000504    	str	x4, [x8, #0x8]
100003528: f9000105    	str	x5, [x8]
10000352c: f90057e6    	str	x6, [sp, #0xa8]
100003530: f90053e7    	str	x7, [sp, #0xa0]
100003534: f94053e8    	ldr	x8, [sp, #0xa0]
100003538: f9400108    	ldr	x8, [x8]
10000353c: f1000108    	subs	x8, x8, #0x0
100003540: 1a9f07e8    	cset	w8, ne
100003544: 370002c8    	tbnz	w8, #0x0, 0x10000359c <_request_handler+0xb0>
100003548: 14000001    	b	0x10000354c <_request_handler+0x60>
10000354c: d2800200    	mov	x0, #0x10               ; =16
100003550: 94000239    	bl	0x100003e34 <_strstr+0x100003e34>
100003554: f9004fe0    	str	x0, [sp, #0x98]
100003558: f9404fe8    	ldr	x8, [sp, #0x98]
10000355c: f1000108    	subs	x8, x8, #0x0
100003560: 1a9f07e8    	cset	w8, ne
100003564: 37000088    	tbnz	w8, #0x0, 0x100003574 <_request_handler+0x88>
100003568: 14000001    	b	0x10000356c <_request_handler+0x80>
10000356c: b900e7ff    	str	wzr, [sp, #0xe4]
100003570: 140001f4    	b	0x100003d40 <_request_handler+0x854>
100003574: f9404fe8    	ldr	x8, [sp, #0x98]
100003578: f900011f    	str	xzr, [x8]
10000357c: f9404fe8    	ldr	x8, [sp, #0x98]
100003580: f900051f    	str	xzr, [x8, #0x8]
100003584: f9404fe8    	ldr	x8, [sp, #0x98]
100003588: f94053e9    	ldr	x9, [sp, #0xa0]
10000358c: f9000128    	str	x8, [x9]
100003590: 52800028    	mov	w8, #0x1                ; =1
100003594: b900e7e8    	str	w8, [sp, #0xe4]
100003598: 140001ea    	b	0x100003d40 <_request_handler+0x854>
10000359c: f94053e8    	ldr	x8, [sp, #0xa0]
1000035a0: f9400108    	ldr	x8, [x8]
1000035a4: f9004be8    	str	x8, [sp, #0x90]
1000035a8: f94057e8    	ldr	x8, [sp, #0xa8]
1000035ac: f9400108    	ldr	x8, [x8]
1000035b0: f1000108    	subs	x8, x8, #0x0
1000035b4: 1a9f17e8    	cset	w8, eq
1000035b8: 370006a8    	tbnz	w8, #0x0, 0x10000368c <_request_handler+0x1a0>
1000035bc: 14000001    	b	0x1000035c0 <_request_handler+0xd4>
1000035c0: f9404be8    	ldr	x8, [sp, #0x90]
1000035c4: f9400508    	ldr	x8, [x8, #0x8]
1000035c8: f94057e9    	ldr	x9, [sp, #0xa8]
1000035cc: f9400129    	ldr	x9, [x9]
1000035d0: 8b090108    	add	x8, x8, x9
1000035d4: f90047e8    	str	x8, [sp, #0x88]
1000035d8: f9404be8    	ldr	x8, [sp, #0x90]
1000035dc: f9400100    	ldr	x0, [x8]
1000035e0: f94047e8    	ldr	x8, [sp, #0x88]
1000035e4: 91000501    	add	x1, x8, #0x1
1000035e8: 94000219    	bl	0x100003e4c <_strstr+0x100003e4c>
1000035ec: f90043e0    	str	x0, [sp, #0x80]
1000035f0: f94043e8    	ldr	x8, [sp, #0x80]
1000035f4: f1000108    	subs	x8, x8, #0x0
1000035f8: 1a9f07e8    	cset	w8, ne
1000035fc: 37000168    	tbnz	w8, #0x0, 0x100003628 <_request_handler+0x13c>
100003600: 14000001    	b	0x100003604 <_request_handler+0x118>
100003604: f9404be8    	ldr	x8, [sp, #0x90]
100003608: f9400100    	ldr	x0, [x8]
10000360c: 94000204    	bl	0x100003e1c <_strstr+0x100003e1c>
100003610: f9404be0    	ldr	x0, [sp, #0x90]
100003614: 94000202    	bl	0x100003e1c <_strstr+0x100003e1c>
100003618: f94053e8    	ldr	x8, [sp, #0xa0]
10000361c: f900011f    	str	xzr, [x8]
100003620: b900e7ff    	str	wzr, [sp, #0xe4]
100003624: 140001c7    	b	0x100003d40 <_request_handler+0x854>
100003628: f94013e8    	ldr	x8, [sp, #0x20]
10000362c: f94043e9    	ldr	x9, [sp, #0x80]
100003630: f9404bea    	ldr	x10, [sp, #0x90]
100003634: f940054a    	ldr	x10, [x10, #0x8]
100003638: 8b0a0120    	add	x0, x9, x10
10000363c: f9400101    	ldr	x1, [x8]
100003640: f94057e8    	ldr	x8, [sp, #0xa8]
100003644: f9400102    	ldr	x2, [x8]
100003648: 92800003    	mov	x3, #-0x1               ; =-1
10000364c: 940001dc    	bl	0x100003dbc <_strstr+0x100003dbc>
100003650: f94043e8    	ldr	x8, [sp, #0x80]
100003654: f94047e9    	ldr	x9, [sp, #0x88]
100003658: 8b090108    	add	x8, x8, x9
10000365c: 3900011f    	strb	wzr, [x8]
100003660: f94043e8    	ldr	x8, [sp, #0x80]
100003664: f9404be9    	ldr	x9, [sp, #0x90]
100003668: f9000128    	str	x8, [x9]
10000366c: f94047e8    	ldr	x8, [sp, #0x88]
100003670: f9404be9    	ldr	x9, [sp, #0x90]
100003674: f9000528    	str	x8, [x9, #0x8]
100003678: f94057e8    	ldr	x8, [sp, #0xa8]
10000367c: f900011f    	str	xzr, [x8]
100003680: 52800028    	mov	w8, #0x1                ; =1
100003684: b900e7e8    	str	w8, [sp, #0xe4]
100003688: 140001ae    	b	0x100003d40 <_request_handler+0x854>
10000368c: 9103a3e0    	add	x0, sp, #0xe8
100003690: d2808001    	mov	x1, #0x400              ; =1024
100003694: 940001dc    	bl	0x100003e04 <_strstr+0x100003e04>
100003698: f94013e8    	ldr	x8, [sp, #0x20]
10000369c: 52801909    	mov	w9, #0xc8               ; =200
1000036a0: b9007fe9    	str	w9, [sp, #0x7c]
1000036a4: f9400900    	ldr	x0, [x8, #0x10]
1000036a8: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
1000036ac: 913b5421    	add	x1, x1, #0xed5
1000036b0: 940001ea    	bl	0x100003e58 <_strstr+0x100003e58>
1000036b4: 71000008    	subs	w8, w0, #0x0
1000036b8: 1a9f07e8    	cset	w8, ne
1000036bc: 37000968    	tbnz	w8, #0x0, 0x1000037e8 <_request_handler+0x2fc>
1000036c0: 14000001    	b	0x1000036c4 <_request_handler+0x1d8>
1000036c4: f94013e8    	ldr	x8, [sp, #0x20]
1000036c8: f9400d00    	ldr	x0, [x8, #0x18]
1000036cc: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
1000036d0: 913b6421    	add	x1, x1, #0xed9
1000036d4: 940001e1    	bl	0x100003e58 <_strstr+0x100003e58>
1000036d8: 71000008    	subs	w8, w0, #0x0
1000036dc: 1a9f07e8    	cset	w8, ne
1000036e0: 370000c8    	tbnz	w8, #0x0, 0x1000036f8 <_request_handler+0x20c>
1000036e4: 14000001    	b	0x1000036e8 <_request_handler+0x1fc>
1000036e8: 9103a3e0    	add	x0, sp, #0xe8
1000036ec: d2808001    	mov	x1, #0x400              ; =1024
1000036f0: 97fffef8    	bl	0x1000032d0 <_list_items_str>
1000036f4: 1400003c    	b	0x1000037e4 <_request_handler+0x2f8>
1000036f8: f94013e8    	ldr	x8, [sp, #0x20]
1000036fc: f9400d00    	ldr	x0, [x8, #0x18]
100003700: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
100003704: 913b8021    	add	x1, x1, #0xee0
100003708: d28000e2    	mov	x2, #0x7                ; =7
10000370c: 940001d9    	bl	0x100003e70 <_strstr+0x100003e70>
100003710: 71000008    	subs	w8, w0, #0x0
100003714: 1a9f07e8    	cset	w8, ne
100003718: 37000508    	tbnz	w8, #0x0, 0x1000037b8 <_request_handler+0x2cc>
10000371c: 14000001    	b	0x100003720 <_request_handler+0x234>
100003720: f94013e8    	ldr	x8, [sp, #0x20]
100003724: f9400d08    	ldr	x8, [x8, #0x18]
100003728: 91001d00    	add	x0, x8, #0x7
10000372c: 940001b3    	bl	0x100003df8 <_strstr+0x100003df8>
100003730: b9007be0    	str	w0, [sp, #0x78]
100003734: b9407be0    	ldr	w0, [sp, #0x78]
100003738: 97fffe86    	bl	0x100003150 <_get_item_data>
10000373c: f9003be0    	str	x0, [sp, #0x70]
100003740: f9403be8    	ldr	x8, [sp, #0x70]
100003744: f1000108    	subs	x8, x8, #0x0
100003748: 1a9f17e8    	cset	w8, eq
10000374c: 37000208    	tbnz	w8, #0x0, 0x10000378c <_request_handler+0x2a0>
100003750: 14000001    	b	0x100003754 <_request_handler+0x268>
100003754: b9407be8    	ldr	w8, [sp, #0x78]
100003758: aa0803ea    	mov	x10, x8
10000375c: f9403be8    	ldr	x8, [sp, #0x70]
100003760: 910003e9    	mov	x9, sp
100003764: f900012a    	str	x10, [x9]
100003768: f9000528    	str	x8, [x9, #0x8]
10000376c: 9103a3e0    	add	x0, sp, #0xe8
100003770: d2808003    	mov	x3, #0x400              ; =1024
100003774: aa0303e1    	mov	x1, x3
100003778: 52800002    	mov	w2, #0x0                ; =0
10000377c: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003780: 913ba084    	add	x4, x4, #0xee8
100003784: 94000191    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003788: 1400000b    	b	0x1000037b4 <_request_handler+0x2c8>
10000378c: 9103a3e0    	add	x0, sp, #0xe8
100003790: d2808003    	mov	x3, #0x400              ; =1024
100003794: aa0303e1    	mov	x1, x3
100003798: 52800002    	mov	w2, #0x0                ; =0
10000379c: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
1000037a0: 913be484    	add	x4, x4, #0xef9
1000037a4: 94000189    	bl	0x100003dc8 <_strstr+0x100003dc8>
1000037a8: 52803288    	mov	w8, #0x194              ; =404
1000037ac: b9007fe8    	str	w8, [sp, #0x7c]
1000037b0: 14000001    	b	0x1000037b4 <_request_handler+0x2c8>
1000037b4: 1400000b    	b	0x1000037e0 <_request_handler+0x2f4>
1000037b8: 9103a3e0    	add	x0, sp, #0xe8
1000037bc: d2808003    	mov	x3, #0x400              ; =1024
1000037c0: aa0303e1    	mov	x1, x3
1000037c4: 52800002    	mov	w2, #0x0                ; =0
1000037c8: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
1000037cc: 913c2084    	add	x4, x4, #0xf08
1000037d0: 9400017e    	bl	0x100003dc8 <_strstr+0x100003dc8>
1000037d4: 52803288    	mov	w8, #0x194              ; =404
1000037d8: b9007fe8    	str	w8, [sp, #0x7c]
1000037dc: 14000001    	b	0x1000037e0 <_request_handler+0x2f4>
1000037e0: 14000001    	b	0x1000037e4 <_request_handler+0x2f8>
1000037e4: 14000137    	b	0x100003cc0 <_request_handler+0x7d4>
1000037e8: f94013e8    	ldr	x8, [sp, #0x20]
1000037ec: f9400900    	ldr	x0, [x8, #0x10]
1000037f0: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
1000037f4: 913c4821    	add	x1, x1, #0xf12
1000037f8: 94000198    	bl	0x100003e58 <_strstr+0x100003e58>
1000037fc: 71000008    	subs	w8, w0, #0x0
100003800: 1a9f07e8    	cset	w8, ne
100003804: 37000f68    	tbnz	w8, #0x0, 0x1000039f0 <_request_handler+0x504>
100003808: 14000001    	b	0x10000380c <_request_handler+0x320>
10000380c: f94013e8    	ldr	x8, [sp, #0x20]
100003810: f9400d00    	ldr	x0, [x8, #0x18]
100003814: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
100003818: 913b6421    	add	x1, x1, #0xed9
10000381c: 9400018f    	bl	0x100003e58 <_strstr+0x100003e58>
100003820: 71000008    	subs	w8, w0, #0x0
100003824: 1a9f07e8    	cset	w8, ne
100003828: 37000ce8    	tbnz	w8, #0x0, 0x1000039c4 <_request_handler+0x4d8>
10000382c: 14000001    	b	0x100003830 <_request_handler+0x344>
100003830: f9404be8    	ldr	x8, [sp, #0x90]
100003834: f9400108    	ldr	x8, [x8]
100003838: f1000108    	subs	x8, x8, #0x0
10000383c: 1a9f07e8    	cset	w8, ne
100003840: 37000188    	tbnz	w8, #0x0, 0x100003870 <_request_handler+0x384>
100003844: 14000001    	b	0x100003848 <_request_handler+0x35c>
100003848: 9103a3e0    	add	x0, sp, #0xe8
10000384c: d2808003    	mov	x3, #0x400              ; =1024
100003850: aa0303e1    	mov	x1, x3
100003854: 52800002    	mov	w2, #0x0                ; =0
100003858: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
10000385c: 913c5c84    	add	x4, x4, #0xf17
100003860: 9400015a    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003864: 52803208    	mov	w8, #0x190              ; =400
100003868: b9007fe8    	str	w8, [sp, #0x7c]
10000386c: 14000055    	b	0x1000039c0 <_request_handler+0x4d4>
100003870: f9404be8    	ldr	x8, [sp, #0x90]
100003874: f9400100    	ldr	x0, [x8]
100003878: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
10000387c: 913c9021    	add	x1, x1, #0xf24
100003880: 9400017f    	bl	0x100003e7c <_strstr+0x100003e7c>
100003884: f90037e0    	str	x0, [sp, #0x68]
100003888: f9404be8    	ldr	x8, [sp, #0x90]
10000388c: f9400100    	ldr	x0, [x8]
100003890: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
100003894: 913ca021    	add	x1, x1, #0xf28
100003898: 94000179    	bl	0x100003e7c <_strstr+0x100003e7c>
10000389c: f90033e0    	str	x0, [sp, #0x60]
1000038a0: f94037e8    	ldr	x8, [sp, #0x68]
1000038a4: f1000108    	subs	x8, x8, #0x0
1000038a8: 1a9f17e8    	cset	w8, eq
1000038ac: 37000748    	tbnz	w8, #0x0, 0x100003994 <_request_handler+0x4a8>
1000038b0: 14000001    	b	0x1000038b4 <_request_handler+0x3c8>
1000038b4: f94033e8    	ldr	x8, [sp, #0x60]
1000038b8: f1000108    	subs	x8, x8, #0x0
1000038bc: 1a9f17e8    	cset	w8, eq
1000038c0: 370006a8    	tbnz	w8, #0x0, 0x100003994 <_request_handler+0x4a8>
1000038c4: 14000001    	b	0x1000038c8 <_request_handler+0x3dc>
1000038c8: f94037e8    	ldr	x8, [sp, #0x68]
1000038cc: 91000d00    	add	x0, x8, #0x3
1000038d0: 9400014a    	bl	0x100003df8 <_strstr+0x100003df8>
1000038d4: b9005fe0    	str	w0, [sp, #0x5c]
1000038d8: f94033e8    	ldr	x8, [sp, #0x60]
1000038dc: 91001508    	add	x8, x8, #0x5
1000038e0: f90033e8    	str	x8, [sp, #0x60]
1000038e4: b9405fe0    	ldr	w0, [sp, #0x5c]
1000038e8: f94033e1    	ldr	x1, [sp, #0x60]
1000038ec: 97fffdce    	bl	0x100003024 <_add_item>
1000038f0: b9005be0    	str	w0, [sp, #0x58]
1000038f4: b9405be8    	ldr	w8, [sp, #0x58]
1000038f8: 71000108    	subs	w8, w8, #0x0
1000038fc: 1a9f07e8    	cset	w8, ne
100003900: 37000148    	tbnz	w8, #0x0, 0x100003928 <_request_handler+0x43c>
100003904: 14000001    	b	0x100003908 <_request_handler+0x41c>
100003908: 9103a3e0    	add	x0, sp, #0xe8
10000390c: d2808003    	mov	x3, #0x400              ; =1024
100003910: aa0303e1    	mov	x1, x3
100003914: 52800002    	mov	w2, #0x0                ; =0
100003918: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
10000391c: 913cb884    	add	x4, x4, #0xf2e
100003920: 9400012a    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003924: 1400001b    	b	0x100003990 <_request_handler+0x4a4>
100003928: b9405be8    	ldr	w8, [sp, #0x58]
10000392c: 31000508    	adds	w8, w8, #0x1
100003930: 1a9f07e8    	cset	w8, ne
100003934: 37000188    	tbnz	w8, #0x0, 0x100003964 <_request_handler+0x478>
100003938: 14000001    	b	0x10000393c <_request_handler+0x450>
10000393c: 9103a3e0    	add	x0, sp, #0xe8
100003940: d2808003    	mov	x3, #0x400              ; =1024
100003944: aa0303e1    	mov	x1, x3
100003948: 52800002    	mov	w2, #0x0                ; =0
10000394c: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003950: 913ce484    	add	x4, x4, #0xf39
100003954: 9400011d    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003958: 52803208    	mov	w8, #0x190              ; =400
10000395c: b9007fe8    	str	w8, [sp, #0x7c]
100003960: 1400000b    	b	0x10000398c <_request_handler+0x4a0>
100003964: 9103a3e0    	add	x0, sp, #0xe8
100003968: d2808003    	mov	x3, #0x400              ; =1024
10000396c: aa0303e1    	mov	x1, x3
100003970: 52800002    	mov	w2, #0x0                ; =0
100003974: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003978: 913d3484    	add	x4, x4, #0xf4d
10000397c: 94000113    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003980: 52803ee8    	mov	w8, #0x1f7              ; =503
100003984: b9007fe8    	str	w8, [sp, #0x7c]
100003988: 14000001    	b	0x10000398c <_request_handler+0x4a0>
10000398c: 14000001    	b	0x100003990 <_request_handler+0x4a4>
100003990: 1400000b    	b	0x1000039bc <_request_handler+0x4d0>
100003994: 9103a3e0    	add	x0, sp, #0xe8
100003998: d2808003    	mov	x3, #0x400              ; =1024
10000399c: aa0303e1    	mov	x1, x3
1000039a0: 52800002    	mov	w2, #0x0                ; =0
1000039a4: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
1000039a8: 913c5c84    	add	x4, x4, #0xf17
1000039ac: 94000107    	bl	0x100003dc8 <_strstr+0x100003dc8>
1000039b0: 52803208    	mov	w8, #0x190              ; =400
1000039b4: b9007fe8    	str	w8, [sp, #0x7c]
1000039b8: 14000001    	b	0x1000039bc <_request_handler+0x4d0>
1000039bc: 14000001    	b	0x1000039c0 <_request_handler+0x4d4>
1000039c0: 1400000b    	b	0x1000039ec <_request_handler+0x500>
1000039c4: 9103a3e0    	add	x0, sp, #0xe8
1000039c8: d2808003    	mov	x3, #0x400              ; =1024
1000039cc: aa0303e1    	mov	x1, x3
1000039d0: 52800002    	mov	w2, #0x0                ; =0
1000039d4: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
1000039d8: 913c2084    	add	x4, x4, #0xf08
1000039dc: 940000fb    	bl	0x100003dc8 <_strstr+0x100003dc8>
1000039e0: 52803288    	mov	w8, #0x194              ; =404
1000039e4: b9007fe8    	str	w8, [sp, #0x7c]
1000039e8: 14000001    	b	0x1000039ec <_request_handler+0x500>
1000039ec: 140000b4    	b	0x100003cbc <_request_handler+0x7d0>
1000039f0: f94013e8    	ldr	x8, [sp, #0x20]
1000039f4: f9400900    	ldr	x0, [x8, #0x10]
1000039f8: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
1000039fc: 913d6021    	add	x1, x1, #0xf58
100003a00: 94000116    	bl	0x100003e58 <_strstr+0x100003e58>
100003a04: 71000008    	subs	w8, w0, #0x0
100003a08: 1a9f07e8    	cset	w8, ne
100003a0c: 37000c48    	tbnz	w8, #0x0, 0x100003b94 <_request_handler+0x6a8>
100003a10: 14000001    	b	0x100003a14 <_request_handler+0x528>
100003a14: f94013e8    	ldr	x8, [sp, #0x20]
100003a18: f9400d00    	ldr	x0, [x8, #0x18]
100003a1c: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
100003a20: 913b8021    	add	x1, x1, #0xee0
100003a24: d28000e2    	mov	x2, #0x7                ; =7
100003a28: 94000112    	bl	0x100003e70 <_strstr+0x100003e70>
100003a2c: 71000008    	subs	w8, w0, #0x0
100003a30: 1a9f07e8    	cset	w8, ne
100003a34: 370009a8    	tbnz	w8, #0x0, 0x100003b68 <_request_handler+0x67c>
100003a38: 14000001    	b	0x100003a3c <_request_handler+0x550>
100003a3c: f94013e8    	ldr	x8, [sp, #0x20]
100003a40: f9400d08    	ldr	x8, [x8, #0x18]
100003a44: 91001d00    	add	x0, x8, #0x7
100003a48: 940000ec    	bl	0x100003df8 <_strstr+0x100003df8>
100003a4c: b90057e0    	str	w0, [sp, #0x54]
100003a50: f9404be8    	ldr	x8, [sp, #0x90]
100003a54: f9400108    	ldr	x8, [x8]
100003a58: f1000108    	subs	x8, x8, #0x0
100003a5c: 1a9f07e8    	cset	w8, ne
100003a60: 37000188    	tbnz	w8, #0x0, 0x100003a90 <_request_handler+0x5a4>
100003a64: 14000001    	b	0x100003a68 <_request_handler+0x57c>
100003a68: 9103a3e0    	add	x0, sp, #0xe8
100003a6c: d2808003    	mov	x3, #0x400              ; =1024
100003a70: aa0303e1    	mov	x1, x3
100003a74: 52800002    	mov	w2, #0x0                ; =0
100003a78: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003a7c: 913c5c84    	add	x4, x4, #0xf17
100003a80: 940000d2    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003a84: 52803208    	mov	w8, #0x190              ; =400
100003a88: b9007fe8    	str	w8, [sp, #0x7c]
100003a8c: 14000036    	b	0x100003b64 <_request_handler+0x678>
100003a90: f9404be8    	ldr	x8, [sp, #0x90]
100003a94: f9400100    	ldr	x0, [x8]
100003a98: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
100003a9c: 913ca021    	add	x1, x1, #0xf28
100003aa0: 940000f7    	bl	0x100003e7c <_strstr+0x100003e7c>
100003aa4: f90027e0    	str	x0, [sp, #0x48]
100003aa8: f94027e8    	ldr	x8, [sp, #0x48]
100003aac: f1000108    	subs	x8, x8, #0x0
100003ab0: 1a9f17e8    	cset	w8, eq
100003ab4: 37000428    	tbnz	w8, #0x0, 0x100003b38 <_request_handler+0x64c>
100003ab8: 14000001    	b	0x100003abc <_request_handler+0x5d0>
100003abc: f94027e8    	ldr	x8, [sp, #0x48]
100003ac0: 91001508    	add	x8, x8, #0x5
100003ac4: f90027e8    	str	x8, [sp, #0x48]
100003ac8: b94057e0    	ldr	w0, [sp, #0x54]
100003acc: f94027e1    	ldr	x1, [sp, #0x48]
100003ad0: 97fffdbb    	bl	0x1000031bc <_update_item>
100003ad4: b90047e0    	str	w0, [sp, #0x44]
100003ad8: b94047e8    	ldr	w8, [sp, #0x44]
100003adc: 71000108    	subs	w8, w8, #0x0
100003ae0: 1a9f07e8    	cset	w8, ne
100003ae4: 37000148    	tbnz	w8, #0x0, 0x100003b0c <_request_handler+0x620>
100003ae8: 14000001    	b	0x100003aec <_request_handler+0x600>
100003aec: 9103a3e0    	add	x0, sp, #0xe8
100003af0: d2808003    	mov	x3, #0x400              ; =1024
100003af4: aa0303e1    	mov	x1, x3
100003af8: 52800002    	mov	w2, #0x0                ; =0
100003afc: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003b00: 913d7084    	add	x4, x4, #0xf5c
100003b04: 940000b1    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003b08: 1400000b    	b	0x100003b34 <_request_handler+0x648>
100003b0c: 9103a3e0    	add	x0, sp, #0xe8
100003b10: d2808003    	mov	x3, #0x400              ; =1024
100003b14: aa0303e1    	mov	x1, x3
100003b18: 52800002    	mov	w2, #0x0                ; =0
100003b1c: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003b20: 913be484    	add	x4, x4, #0xef9
100003b24: 940000a9    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003b28: 52803288    	mov	w8, #0x194              ; =404
100003b2c: b9007fe8    	str	w8, [sp, #0x7c]
100003b30: 14000001    	b	0x100003b34 <_request_handler+0x648>
100003b34: 1400000b    	b	0x100003b60 <_request_handler+0x674>
100003b38: 9103a3e0    	add	x0, sp, #0xe8
100003b3c: d2808003    	mov	x3, #0x400              ; =1024
100003b40: aa0303e1    	mov	x1, x3
100003b44: 52800002    	mov	w2, #0x0                ; =0
100003b48: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003b4c: 913c5c84    	add	x4, x4, #0xf17
100003b50: 9400009e    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003b54: 52803208    	mov	w8, #0x190              ; =400
100003b58: b9007fe8    	str	w8, [sp, #0x7c]
100003b5c: 14000001    	b	0x100003b60 <_request_handler+0x674>
100003b60: 14000001    	b	0x100003b64 <_request_handler+0x678>
100003b64: 1400000b    	b	0x100003b90 <_request_handler+0x6a4>
100003b68: 9103a3e0    	add	x0, sp, #0xe8
100003b6c: d2808003    	mov	x3, #0x400              ; =1024
100003b70: aa0303e1    	mov	x1, x3
100003b74: 52800002    	mov	w2, #0x0                ; =0
100003b78: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003b7c: 913c2084    	add	x4, x4, #0xf08
100003b80: 94000092    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003b84: 52803288    	mov	w8, #0x194              ; =404
100003b88: b9007fe8    	str	w8, [sp, #0x7c]
100003b8c: 14000001    	b	0x100003b90 <_request_handler+0x6a4>
100003b90: 1400004a    	b	0x100003cb8 <_request_handler+0x7cc>
100003b94: f94013e8    	ldr	x8, [sp, #0x20]
100003b98: f9400900    	ldr	x0, [x8, #0x10]
100003b9c: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
100003ba0: 913da421    	add	x1, x1, #0xf69
100003ba4: 940000ad    	bl	0x100003e58 <_strstr+0x100003e58>
100003ba8: 71000008    	subs	w8, w0, #0x0
100003bac: 1a9f07e8    	cset	w8, ne
100003bb0: 370006e8    	tbnz	w8, #0x0, 0x100003c8c <_request_handler+0x7a0>
100003bb4: 14000001    	b	0x100003bb8 <_request_handler+0x6cc>
100003bb8: f94013e8    	ldr	x8, [sp, #0x20]
100003bbc: f9400d00    	ldr	x0, [x8, #0x18]
100003bc0: 90000001    	adrp	x1, 0x100003000 <_find_index+0x90>
100003bc4: 913b8021    	add	x1, x1, #0xee0
100003bc8: d28000e2    	mov	x2, #0x7                ; =7
100003bcc: 940000a9    	bl	0x100003e70 <_strstr+0x100003e70>
100003bd0: 71000008    	subs	w8, w0, #0x0
100003bd4: 1a9f07e8    	cset	w8, ne
100003bd8: 37000448    	tbnz	w8, #0x0, 0x100003c60 <_request_handler+0x774>
100003bdc: 14000001    	b	0x100003be0 <_request_handler+0x6f4>
100003be0: f94013e8    	ldr	x8, [sp, #0x20]
100003be4: f9400d08    	ldr	x8, [x8, #0x18]
100003be8: 91001d00    	add	x0, x8, #0x7
100003bec: 94000083    	bl	0x100003df8 <_strstr+0x100003df8>
100003bf0: b90043e0    	str	w0, [sp, #0x40]
100003bf4: b94043e0    	ldr	w0, [sp, #0x40]
100003bf8: 97fffd9a    	bl	0x100003260 <_delete_item>
100003bfc: b9003fe0    	str	w0, [sp, #0x3c]
100003c00: b9403fe8    	ldr	w8, [sp, #0x3c]
100003c04: 71000108    	subs	w8, w8, #0x0
100003c08: 1a9f07e8    	cset	w8, ne
100003c0c: 37000148    	tbnz	w8, #0x0, 0x100003c34 <_request_handler+0x748>
100003c10: 14000001    	b	0x100003c14 <_request_handler+0x728>
100003c14: 9103a3e0    	add	x0, sp, #0xe8
100003c18: d2808003    	mov	x3, #0x400              ; =1024
100003c1c: aa0303e1    	mov	x1, x3
100003c20: 52800002    	mov	w2, #0x0                ; =0
100003c24: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003c28: 913dc084    	add	x4, x4, #0xf70
100003c2c: 94000067    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003c30: 1400000b    	b	0x100003c5c <_request_handler+0x770>
100003c34: 9103a3e0    	add	x0, sp, #0xe8
100003c38: d2808003    	mov	x3, #0x400              ; =1024
100003c3c: aa0303e1    	mov	x1, x3
100003c40: 52800002    	mov	w2, #0x0                ; =0
100003c44: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003c48: 913be484    	add	x4, x4, #0xef9
100003c4c: 9400005f    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003c50: 52803288    	mov	w8, #0x194              ; =404
100003c54: b9007fe8    	str	w8, [sp, #0x7c]
100003c58: 14000001    	b	0x100003c5c <_request_handler+0x770>
100003c5c: 1400000b    	b	0x100003c88 <_request_handler+0x79c>
100003c60: 9103a3e0    	add	x0, sp, #0xe8
100003c64: d2808003    	mov	x3, #0x400              ; =1024
100003c68: aa0303e1    	mov	x1, x3
100003c6c: 52800002    	mov	w2, #0x0                ; =0
100003c70: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003c74: 913c2084    	add	x4, x4, #0xf08
100003c78: 94000054    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003c7c: 52803288    	mov	w8, #0x194              ; =404
100003c80: b9007fe8    	str	w8, [sp, #0x7c]
100003c84: 14000001    	b	0x100003c88 <_request_handler+0x79c>
100003c88: 1400000b    	b	0x100003cb4 <_request_handler+0x7c8>
100003c8c: 9103a3e0    	add	x0, sp, #0xe8
100003c90: d2808003    	mov	x3, #0x400              ; =1024
100003c94: aa0303e1    	mov	x1, x3
100003c98: 52800002    	mov	w2, #0x0                ; =0
100003c9c: 90000004    	adrp	x4, 0x100003000 <_find_index+0x90>
100003ca0: 913df484    	add	x4, x4, #0xf7d
100003ca4: 94000049    	bl	0x100003dc8 <_strstr+0x100003dc8>
100003ca8: 528032a8    	mov	w8, #0x195              ; =405
100003cac: b9007fe8    	str	w8, [sp, #0x7c]
100003cb0: 14000001    	b	0x100003cb4 <_request_handler+0x7c8>
100003cb4: 14000001    	b	0x100003cb8 <_request_handler+0x7cc>
100003cb8: 14000001    	b	0x100003cbc <_request_handler+0x7d0>
100003cbc: 14000001    	b	0x100003cc0 <_request_handler+0x7d4>
100003cc0: 9103a3e0    	add	x0, sp, #0xe8
100003cc4: f9000fe0    	str	x0, [sp, #0x18]
100003cc8: 94000067    	bl	0x100003e64 <_strstr+0x100003e64>
100003ccc: f9400fe1    	ldr	x1, [sp, #0x18]
100003cd0: 52800042    	mov	w2, #0x2                ; =2
100003cd4: 9400002b    	bl	0x100003d80 <_strstr+0x100003d80>
100003cd8: f94013e8    	ldr	x8, [sp, #0x20]
100003cdc: f9001be0    	str	x0, [sp, #0x30]
100003ce0: f9401100    	ldr	x0, [x8, #0x20]
100003ce4: b9407fe1    	ldr	w1, [sp, #0x7c]
100003ce8: f9401be2    	ldr	x2, [sp, #0x30]
100003cec: 9400002b    	bl	0x100003d98 <_strstr+0x100003d98>
100003cf0: b9002fe0    	str	w0, [sp, #0x2c]
100003cf4: f9401be0    	ldr	x0, [sp, #0x30]
100003cf8: 94000025    	bl	0x100003d8c <_strstr+0x100003d8c>
100003cfc: f9404be8    	ldr	x8, [sp, #0x90]
100003d00: f9400108    	ldr	x8, [x8]
100003d04: f1000108    	subs	x8, x8, #0x0
100003d08: 1a9f17e8    	cset	w8, eq
100003d0c: 370000c8    	tbnz	w8, #0x0, 0x100003d24 <_request_handler+0x838>
100003d10: 14000001    	b	0x100003d14 <_request_handler+0x828>
100003d14: f9404be8    	ldr	x8, [sp, #0x90]
100003d18: f9400100    	ldr	x0, [x8]
100003d1c: 94000040    	bl	0x100003e1c <_strstr+0x100003e1c>
100003d20: 14000001    	b	0x100003d24 <_request_handler+0x838>
100003d24: f9404be0    	ldr	x0, [sp, #0x90]
100003d28: 9400003d    	bl	0x100003e1c <_strstr+0x100003e1c>
100003d2c: f94053e8    	ldr	x8, [sp, #0xa0]
100003d30: f900011f    	str	xzr, [x8]
100003d34: b9402fe8    	ldr	w8, [sp, #0x2c]
100003d38: b900e7e8    	str	w8, [sp, #0xe4]
100003d3c: 14000001    	b	0x100003d40 <_request_handler+0x854>
100003d40: b940e7e8    	ldr	w8, [sp, #0xe4]
100003d44: b90017e8    	str	w8, [sp, #0x14]
100003d48: f85e83a9    	ldur	x9, [x29, #-0x18]
100003d4c: b0000008    	adrp	x8, 0x100004000 <_strstr+0x100004000>
100003d50: f9402108    	ldr	x8, [x8, #0x40]
100003d54: f9400108    	ldr	x8, [x8]
100003d58: eb090108    	subs	x8, x8, x9
100003d5c: 1a9f17e8    	cset	w8, eq
100003d60: 37000068    	tbnz	w8, #0x0, 0x100003d6c <_request_handler+0x880>
100003d64: 14000001    	b	0x100003d68 <_request_handler+0x87c>
100003d68: 9400001b    	bl	0x100003dd4 <_strstr+0x100003dd4>
100003d6c: b94017e0    	ldr	w0, [sp, #0x14]
100003d70: 9113c3ff    	add	sp, sp, #0x4f0
100003d74: a9417bfd    	ldp	x29, x30, [sp, #0x10]
100003d78: a8c26ffc    	ldp	x28, x27, [sp], #0x20
100003d7c: d65f03c0    	ret

Disassembly of section __TEXT,__stubs:

0000000100003d80 <__stubs>:
100003d80: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003d84: f9400210    	ldr	x16, [x16]
100003d88: d61f0200    	br	x16
100003d8c: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003d90: f9400610    	ldr	x16, [x16, #0x8]
100003d94: d61f0200    	br	x16
100003d98: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003d9c: f9400a10    	ldr	x16, [x16, #0x10]
100003da0: d61f0200    	br	x16
100003da4: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003da8: f9400e10    	ldr	x16, [x16, #0x18]
100003dac: d61f0200    	br	x16
100003db0: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003db4: f9401210    	ldr	x16, [x16, #0x20]
100003db8: d61f0200    	br	x16
100003dbc: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003dc0: f9401610    	ldr	x16, [x16, #0x28]
100003dc4: d61f0200    	br	x16
100003dc8: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003dcc: f9401a10    	ldr	x16, [x16, #0x30]
100003dd0: d61f0200    	br	x16
100003dd4: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003dd8: f9401e10    	ldr	x16, [x16, #0x38]
100003ddc: d61f0200    	br	x16
100003de0: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003de4: f9402a10    	ldr	x16, [x16, #0x50]
100003de8: d61f0200    	br	x16
100003dec: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003df0: f9402e10    	ldr	x16, [x16, #0x58]
100003df4: d61f0200    	br	x16
100003df8: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003dfc: f9403210    	ldr	x16, [x16, #0x60]
100003e00: d61f0200    	br	x16
100003e04: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e08: f9403610    	ldr	x16, [x16, #0x68]
100003e0c: d61f0200    	br	x16
100003e10: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e14: f9403a10    	ldr	x16, [x16, #0x70]
100003e18: d61f0200    	br	x16
100003e1c: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e20: f9403e10    	ldr	x16, [x16, #0x78]
100003e24: d61f0200    	br	x16
100003e28: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e2c: f9404210    	ldr	x16, [x16, #0x80]
100003e30: d61f0200    	br	x16
100003e34: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e38: f9404610    	ldr	x16, [x16, #0x88]
100003e3c: d61f0200    	br	x16
100003e40: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e44: f9404a10    	ldr	x16, [x16, #0x90]
100003e48: d61f0200    	br	x16
100003e4c: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e50: f9404e10    	ldr	x16, [x16, #0x98]
100003e54: d61f0200    	br	x16
100003e58: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e5c: f9405210    	ldr	x16, [x16, #0xa0]
100003e60: d61f0200    	br	x16
100003e64: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e68: f9405610    	ldr	x16, [x16, #0xa8]
100003e6c: d61f0200    	br	x16
100003e70: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e74: f9405a10    	ldr	x16, [x16, #0xb0]
100003e78: d61f0200    	br	x16
100003e7c: b0000010    	adrp	x16, 0x100004000 <_strstr+0x100004000>
100003e80: f9405e10    	ldr	x16, [x16, #0xb8]
100003e84: d61f0200    	br	x16

Disassembly of section __TEXT,__cstring:

0000000100003e88 <__cstring>:
100003e88: 6d657449    	ldp	d9, d29, [x2, #-0x1b0]
100003e8c: 000a3a73    	<unknown>
100003e90: 203a4449    	<unknown>
100003e94: 202c6425    	<unknown>
100003e98: 61746144    	<unknown>
100003e9c: 7325203a    	<unknown>
100003ea0: 6146000a    	<unknown>
100003ea4: 64656c69    	<unknown>
100003ea8: 206f7420    	<unknown>
100003eac: 72617473    	<unknown>
100003eb0: 65732074    	fmls	z20.h, p0/m, z3.h, z19.h
100003eb4: 72657672    	<unknown>
100003eb8: 6553000a    	fadd	z10.h, z0.h, z19.h
100003ebc: 72657672    	<unknown>
100003ec0: 6e757220    	uabdl2.4s	v0, v17, v21
100003ec4: 676e696e    	<unknown>
100003ec8: 206e6f20    	<unknown>
100003ecc: 74726f70    	<unknown>
100003ed0: 0a642520    	bic	w0, w9, w4, lsr #9
100003ed4: 54454700    	b.eq	0x10008e7b4 <_store+0x867b4>
100003ed8: 74692f00    	<unknown>
100003edc: 00736d65    	<unknown>
100003ee0: 6574692f    	fnmls	z15.h, p2/m, z9.h, z20.h
100003ee4: 002f736d    	<unknown>
100003ee8: 203a4449    	<unknown>
100003eec: 202c6425    	<unknown>
100003ef0: 61746144    	<unknown>
100003ef4: 7325203a    	<unknown>
100003ef8: 65744900    	fnmla	z0.h, p2/m, z8.h, z20.h
100003efc: 6f6e206d    	umlal2.4s	v13, v3, v14[2]
100003f00: 6f662074    	umlal2.4s	v20, v3, v6[2]
100003f04: 00646e75    	<unknown>
100003f08: 20746f4e    	<unknown>
100003f0c: 6e756f66    	umin.8h	v6, v27, v21
100003f10: 4f500064    	fdot.8h	v4, v3, v0[1]
100003f14: 49005453    	<unknown>
100003f18: 6c61766e    	ldnp	d14, d29, [x19, #-0x1f0]
100003f1c: 64206469    	<unknown>
100003f20: 00617461    	<unknown>
100003f24: 003d6469    	<unknown>
100003f28: 61746164    	<unknown>
100003f2c: 7449003d    	<unknown>
100003f30: 61206d65    	<unknown>
100003f34: 64656464    	<unknown>
100003f38: 65744900    	fnmla	z0.h, p2/m, z8.h, z20.h
100003f3c: 6c61206d    	ldnp	d13, d8, [x3, #-0x1f0]
100003f40: 64616572    	<unknown>
100003f44: 78652079    	ldeorlh	w5, w25, [x3]
100003f48: 73747369    	<unknown>
100003f4c: 6f745300    	fcmla.8h	v0, v24, v20[1], #180
100003f50: 66206572    	<unknown>
100003f54: 006c6c75    	<unknown>
100003f58: 00545550    	<unknown>
100003f5c: 6d657449    	ldp	d9, d29, [x2, #-0x1b0]
100003f60: 64707520    	<unknown>
100003f64: 64657461    	<unknown>
100003f68: 4c454400    	<unknown>
100003f6c: 00455445    	<unknown>
100003f70: 6d657449    	ldp	d9, d29, [x2, #-0x1b0]
100003f74: 6c656420    	ldnp	d0, d25, [x1, #-0x1b0]
100003f78: 64657465    	<unknown>
100003f7c: 74654d00    	<unknown>
100003f80: 20646f68    	<unknown>
100003f84: 20746f6e    	<unknown>
100003f88: 6f6c6c61    	<unknown>
100003f8c: 00646577    	<unknown>

Disassembly of section __TEXT,__unwind_info:

0000000100003f90 <__unwind_info>:
100003f90: 00000001    	udf	#0x1
100003f94: 0000001c    	udf	#0x1c
100003f98: 00000002    	udf	#0x2
100003f9c: 00000024    	udf	#0x24
100003fa0: 00000000    	udf	#0x0
100003fa4: 00000024    	udf	#0x24
100003fa8: 00000002    	udf	#0x2
100003fac: 04000000    	add	z0.b, p0/m, z0.b, z0.b
100003fb0: 04000010    	add	z16.b, p0/m, z16.b, z0.b
100003fb4: 00002f18    	udf	#0x2f18
100003fb8: 00000048    	udf	#0x48
100003fbc: 00000048    	udf	#0x48
100003fc0: 00003d80    	udf	#0x3d80
100003fc4: 00000000    	udf	#0x0
100003fc8: 00000048    	udf	#0x48
		...
100003fd8: 00000003    	udf	#0x3
100003fdc: 0005000c    	<unknown>
100003fe0: 00010020    	<unknown>
100003fe4: 02000000    	<unknown>
100003fe8: 0000010c    	udf	#0x10c
100003fec: 010003b8    	<unknown>
100003ff0: 00000520    	udf	#0x520
100003ff4: 010005d4    	<unknown>
100003ff8: 02001000    	<unknown>
100003ffc: 00000000    	udf	#0x0

Disassembly of section __DATA_CONST,__got:

0000000100004000 <__got>:
100004000: 00000000    	udf	#0x0
100004004: 80100000    	<unknown>
100004008: 00000001    	udf	#0x1
10000400c: 80100000    	<unknown>
100004010: 00000002    	udf	#0x2
100004014: 80100000    	<unknown>
100004018: 00000003    	udf	#0x3
10000401c: 80100000    	<unknown>
100004020: 00000004    	udf	#0x4
100004024: 80100000    	<unknown>
100004028: 00000005    	udf	#0x5
10000402c: 80100000    	<unknown>
100004030: 00000006    	udf	#0x6
100004034: 80100000    	<unknown>
100004038: 00000007    	udf	#0x7
10000403c: 80100000    	<unknown>
100004040: 00000008    	udf	#0x8
100004044: 80100000    	<unknown>
100004048: 00000009    	udf	#0x9
10000404c: 80100000    	<unknown>
100004050: 0000000a    	udf	#0xa
100004054: 80100000    	<unknown>
100004058: 0000000b    	udf	#0xb
10000405c: 80100000    	<unknown>
100004060: 0000000c    	udf	#0xc
100004064: 80100000    	<unknown>
100004068: 0000000d    	udf	#0xd
10000406c: 80100000    	<unknown>
100004070: 0000000e    	udf	#0xe
100004074: 80100000    	<unknown>
100004078: 0000000f    	udf	#0xf
10000407c: 80100000    	<unknown>
100004080: 00000010    	udf	#0x10
100004084: 80100000    	<unknown>
100004088: 00000011    	udf	#0x11
10000408c: 80100000    	<unknown>
100004090: 00000012    	udf	#0x12
100004094: 80100000    	<unknown>
100004098: 00000013    	udf	#0x13
10000409c: 80100000    	<unknown>
1000040a0: 00000014    	udf	#0x14
1000040a4: 80100000    	<unknown>
1000040a8: 00000015    	udf	#0x15
1000040ac: 80100000    	<unknown>
1000040b0: 00000016    	udf	#0x16
1000040b4: 80100000    	<unknown>
1000040b8: 00000017    	udf	#0x17
1000040bc: 80000000    	<unknown>

Disassembly of section __DATA,__common:

0000000100008000 <_store>:
...
