# r8152.ko and ax88179_178a.ko for the K5Lp chip (kernel 4.4.84)

- **Built by:** [throwaway96](https://github.com/throwaway96)
- **Original:** [throwaway96/webos-kernel-drivers](https://github.com/throwaway96/webos-kernel-drivers) at commit `67cb647be62a0d516fc1e5ead24ce2f967a44bbd`, folder `armv7l-4.4.84-k5lp/drivers/net/usb/`
- **SHA-256:**
  - `r8152.ko`: `4735b94db05247a1b3f2d40a25179abfc4b06c60692e4a8edacc888df16ad9c4`
  - `ax88179_178a.ko`: `dabd33606f30197d1eb58e7c8b02549ebcca3a8015504da6b0d6c2fb97c711fd`
- **Drivers:** the Linux kernel's own `r8152` and `ax88179_178a`, built from LG's open-source kernel for TVs with the Realtek K5Lp chip
- **TVs:** LG TVs whose `nyx-cmd DeviceInfo query device_name` says K5Lp, on kernel 4.4.84.  These modules are built per chip, not per exact kernel, so LG-USB-2-ETH0 checks the chip too.
- **Adapters:** `r8152.ko`: Realtek RTL8152 and RTL8153 (gigabit) and some OEM versions.  `ax88179_178a.ko`: ASIX AX88179 and AX88178A.
- **Source:** the original repository publishes only the modules, built from the kernel source and toolchain on [LG Open Source](https://opensource.lge.com/).  The drivers are the Linux kernel's `drivers/net/usb/r8152.c` and `ax88179_178a.c`, which are GPL-2.0.
- **License:** GPL-2.0, like the Linux kernel drivers they're built from.

The files here are byte for byte the ones in throwaway96's repository.  All credit for them goes to him.
