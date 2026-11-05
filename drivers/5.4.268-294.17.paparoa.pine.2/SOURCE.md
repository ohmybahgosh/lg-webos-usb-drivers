# r8152.ko for kernel 5.4.268-294.17.paparoa.pine.2

- **Built by:** [mbenitez343](https://github.com/mbenitez343)
- **Original:** [mbenitez343/lg-webos-2024-ethernet-fix](https://github.com/mbenitez343/lg-webos-2024-ethernet-fix) at commit `05ad4588bbdf91825567726713650c4f4bf13fdc`
- **SHA-256:** `7c7c32586fabf4a65899362594a130923d01cb90309c209e04c45d91840273ba`
- **Driver:** the Linux kernel's own `r8152` (v1.10.11)
- **TVs:** 2024 QNED and OLED (K25lp / Paparoa) on webOS 25, where LG removed the Realtek driver
- **Adapters:** gigabit Realtek RTL8152 and RTL8153 (not 2.5G RTL8156)
- **Source:** the original repository publishes only the module.  The driver is the Linux kernel's `drivers/net/usb/r8152.c`, which is GPL-2.0.  The exact source and build steps will be added here once the author shares them.
- **License:** GPL-2.0, like the Linux kernel driver it's built from.

The file here is byte for byte the one in mbenitez343's repository.  All credit for it goes to them.
