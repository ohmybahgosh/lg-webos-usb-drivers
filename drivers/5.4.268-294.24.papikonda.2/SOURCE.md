# ax88179_178a.ko for kernel 5.4.268-294.24.papikonda.2

- **Built by:** [dd3git](https://github.com/dd3git)
- **Original:** [dd3git/lg-webos-ax88179-driver](https://github.com/dd3git/lg-webos-ax88179-driver) at commit `3a871c9ef7b21bdbc6d93dd2ca2bd07d94c08d37`
- **SHA-256:** `f75802cfeca28381c9cf990e589f34bc21129d643408c40ca56b11b9ff1c1987`
- **Driver:** the ASIX AX88179/178A driver from LG's own kernel source, built for the K24 chip (`CHIP_NAME=k24`)
- **TVs:** tested on a 2025 OLED55B56LA (B5) on webOS 25, firmware 33.31.68.  Other 2025 models on the same kernel may work too.
- **Adapters:** ASIX AX88179 and AX88178A, like the UGREEN USB 3.0 gigabit adapter it was tested with
- **Source:** `source/`, copied from the same commit (`ax88179_178a.c` and the `Makefile`)
- **License:** GPL-2.0, see `LICENSE` (copied from the original repository).

Its vermagic says `5.4.268` rather than the TV's full kernel name, and the TV loads it anyway.  LG-USB-2-ETH0 accepts that only because this exact file's SHA-256 is pinned for this exact kernel.

The file here is byte for byte the one in dd3git's repository.  All credit for it goes to them.
