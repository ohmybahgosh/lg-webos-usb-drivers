obj-m += ax88179_178a.o

KDIR ?= /home/dd3/LG/build/linux-5.4

all:
	$(MAKE) -C $(KDIR) \
	ARCH=arm64 \
	CHIP_NAME=k24 \
	CROSS_COMPILE=aarch64-linux-gnu- \
	M=$(PWD) modules

clean:
	$(MAKE) -C $(KDIR) \
	ARCH=arm64 \
	CHIP_NAME=k24 \
	M=$(PWD) clean
