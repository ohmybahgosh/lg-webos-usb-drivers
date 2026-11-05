# r8152_oot.ko for kernel 5.4.96-307 (experimental)

**Not tested on a TV yet.**  `get-driver` doesn't offer it.  If your TV runs this kernel, please try it and report back: see [Testing one](https://github.com/ohmybahgosh/LG-USB-2-ETH0/blob/main/docs/driver-build.md#testing-one).

- **Built by:** [OhMyBahGosh](https://github.com/ohmybahgosh), with [LG-USB-2-ETH0's scripts/driver-build/build.sh](https://github.com/ohmybahgosh/LG-USB-2-ETH0/tree/main/scripts/driver-build), the way [DonZoomik](https://github.com/DonZoomik/webos-r8152) built his
- **SHA-256:** `8cbc4e1472de11d3720c36180e717a6dd95ca5d7875fb813febde6af44d927da`
- **Driver:** Realtek's r8152 v2.22.1 as DonZoomik patched it, renamed `r8152_oot` so it can sit beside an old built-in `r8152`.  The same source as [`drivers/5.4.268-329.ptl4tv.5/source`](../../drivers/5.4.268-329.ptl4tv.5/source), from [DonZoomik/webos-r8152](https://github.com/DonZoomik/webos-r8152) at commit `1ea8e98a24ef7443c590024d48947fee22d29cf1`
- **TVs:** 2022 and 2023 OLEDs with LG's o22-family chips, on firmware 03.31, 03.33 and 13.30
- **Adapters:** Realtek RTL8152, RTL8153, RTL8156 and OEM versions of them
- **Kernel source:** LG Open Source package "webOS 23 O ReNew" for the OLED65C2 (`kdriver/kernel/linux-5.4-lg115x.tgz`)
- **Config:** the one built into the TV's own kernel, from LG firmware for that kernel
- **Checks:** `vermagic=5.4.96-307 SMP preempt mod_unload aarch64`, the kernel has MODVERSIONS and module signing off, and all 128 symbols it imports are exported by the TV's kernel.  USB struct offsets: not checked: DonZoomik's offsets are for 5.4.268, so this one needs a tester.
- **License:** GPL-2.0, like the driver it's built from

`build-modinfo.txt`, `build-imports.txt` and `build-config-differences.txt` are from the build: the module's info, the symbols it imports, and how the build config differs from the TV's (only options the source adds or the TV has from LG's private code).
