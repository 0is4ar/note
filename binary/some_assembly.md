```asm
; Conditional Jump
test cl, cl   ; set ZF to 1 if cl == 0
je 0x804f430  ; jump if ZF == 1

; or
test eax, eax  ; set SF to 1 if eax < 0 (negative)
js error ; jump if SF == 1
```
