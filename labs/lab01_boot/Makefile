CC = arm-none-eabi-gcc
CFLAGS = -mcpu=cortex-m4 -mthumb -O0 -Wall -g
SRCS = src/main.c src/startup.c
OBJS = $(SRCS:.c=.o)

all: firmware.elf

%.o: %.c
	@echo "CC $<"
	$(CC) $(CFLAGS) -c $< -o $@

firmware.elf: $(OBJS)
	@echo "LINK $@"
	$(CC) $(CFLAGS) -T linker.ld -nostdlib $(OBJS) -o $@
	arm-none-eabi-objdump -d firmware.elf > firmware.asm

clean:
	rm -f src/*.o firmware.elf firmware.asm
