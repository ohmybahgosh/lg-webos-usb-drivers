# ax88179_178a.ko for kernel 4.4.84-612.jcl4tv.40

- **Built by:** [OCT0PUSCRIME](https://github.com/OCT0PUSCRIME)
- **Original:** [OCT0PUSCRIME/lg-webos-ax88179-driver](https://github.com/OCT0PUSCRIME/lg-webos-ax88179-driver) at commit `734b54c9489034886382a23625b753aab9e661de`
- **SHA-256:** `c9aefe84ee61d7021d739af37d70214a4b82f4b449a5eaf3501cec1f21af1831`
- **Driver:** ASIX's AX88179/178A driver v1.19.0 (as shipped by TP-Link), built against LG's open-source webOS 5.0 kernel (`kernel-1.0.0-612.21`)
- **TVs:** 2020 UN7300 (tested on a 55UN7300PUF) on webOS 5, whose kernel has no ASIX driver
- **Adapters:** ASIX AX88179 and AX88178A, like the TP-Link UE306 and UE300
- **Source:** the original repository publishes only the module.  The driver is ASIX's GPL-2.0 AX88179_178A Linux driver v1.19.0, from TP-Link's Linux driver download (`ax88179_178a.c`), built against LG's kernel source as below.  The author shared these steps in [LG-USB-2-ETH0 discussion #3](https://github.com/ohmybahgosh/LG-USB-2-ETH0/discussions/3).
- **License:** GPL-2.0, see `LICENSE` (copied from the original repository).

## How it was built

As OCT0PUSCRIME described it:

- **Kernel source:** LG's official open-source release for webOS 5.0 (JKHP 2.0), `kernel-1.0.0-612.21.tar.gz`, from [LG Open Source](https://opensource.lge.com/)
- **Driver source:** TP-Link's Linux driver V1.19.0 (`ax88179_178a.c`)
- **Build environment:** a Debian LXC container
- **Toolchain:** `gcc-arm-linux-gnueabihf` (ARMv7-A, 32-bit)

1. Set the kernel's version suffix, so the module's vermagic is exactly `4.4.84-612.jcl4tv.40`.  In the root of the kernel source:

   ```sh
   echo "-612.jcl4tv.40" > localversion
   ```

2. Prepare the kernel headers, with the host compiler flag older kernels need on newer GCC:

   ```sh
   export ARCH=arm
   export CROSS_COMPILE=arm-linux-gnueabihf-
   make prepare
   make HOSTCFLAGS="-fcommon" modules_prepare
   ```

3. In the driver's `Makefile`, point `KDIR` at the prepared kernel tree, for example `KDIR := /root/lg_kernel_build/linux-4.4.3`.

4. Build the module for the TV's ARMv7 CPU:

   ```sh
   make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- KCFLAGS="-march=armv7-a" HOSTCFLAGS="-fcommon"
   ```

The file here is byte for byte the one in OCT0PUSCRIME's repository.  All credit for it goes to them.
