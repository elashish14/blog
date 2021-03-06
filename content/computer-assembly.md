Title: My Experience Assembling a Desktop Computer
Date: 2020-01-14T05:28+00:00
Modified: 2020-01-16T05:26:48+00:00
Category: Computers
Tags: Hardware
Slug: computer-assembly

Over this past weekend, I assembled a desktop computer. This was my first time
ever putting a desktop together and I found it more difficult than I expected.
I want to write about my experiences and what I learned while they are still
fresh.

# The Hardware

Below are the hardware components that went into the build that I made. The
overall cost of the system was around $1000, not including the monitor or
keyboard.

* Processor: AMD Ryzen 5 3600 with stock cooler

* Motherboard: ASRock B450M/AC (Micro ATX)

* Power Supply: EVGA 550 Watt

* Enclosure: Fractal Design Focus Mini G (Micro ATX)

* Memory: 2x16GB DDR4-3200

* Graphics Card: AMD Radeon 580

* Fast Storage: 1 M.2 2280 PCIe SSD

* Large Storage: 1 3.5-inch HDD

# Factors I had not Considered

I did a decent amount of research into the assembly process, but I still ran
into several unforeseen objectives. Though much of what I discuss below are
fairly obvious in hindsight, **there are always several details which are not
immediately apparent to the first-time builder.** These details are the ones
that I am most interested in discussing.

## Connecting Components

There are many connections between components which are obvious, such as
running power from the PSU to the GPU. However, there are always additional
details which can be quite subtle (for instance, how many motherboard
connections does the CPU require?) or easy to overlook (like the fact that the
case must be connected to the motherboard so that the USB ports and power
buttons that it provides actually do something). So below is a comprehensive
list of cabling that was necessary between the different components.

* Case to motherboard: this was the most difficult cabling task and will be
  explained more in the next subsection.

* Motherboard to PSU: obviously, the motherboard requires power from the PSU.
  What was surprising was how large (24 pins!) this cable was. This was easily
  the most bulky cabling component in the case which made it the hardest to fit
  cleanly into the case.

* CPU to PSU: the motherboard provides special pins which provide power to the
  CPU. Unlike the CPU fan, the CPU requires a separate, dedicated cable
  directly to the PSU.

* CPU fan to motherboard: yes, the CPU and the CPU fan require separate cables.
  The CPU fan, however, simply plugs into the motherboard to receive power and
  control.

* GPU to PSU: GPU connects to the motherboard through the PCIe interface, but
  receives power separately from the PSU.

* 3.5-inch HDD to Motherboard: obviously, this is required for disk I/O, but it
  is important to note that power is not provided through the SATA interface.

* 3.5-inch HDD to PSU: since the SATA interface does not provide power, an
  additional cable from the PSU to the HDD is required.

Note that there is no additional cabling required for RAM or the PCIe SSD,
since these are slotted directly into the motherboard. However, a 2.5-inch
SATA3 SSD would require an additional SATA power cable to be connected to the
PSU, just the same way that the 3.5-inch HDD requires.

### Case to Motherboard

This was the most non-trivial cabling, particularly from a knowledge
standpoint. The case in question provides a number of peripheral components:

* 1 USB 3.0 port

* 1 USB 2.0 port

* 2 Chassis fans

* HD audio port

* Power button

* Reset button

* Power LED

The USB ports each required a separate cable to the motherboard. The USB 3.0
port was easy: the connector is so large that it is obvious where it goes on
the motherboard. The USB 2.0 port was harder and it took several minutes of
staring at the manual to determine where to place it (and the fact that there
are several sets of USB 2.0 pins on the motherboard made it just a little more
confusing, but I figure that any of them will work just fine).

The chassis fans were similar to the USB 2.0 port. Read the manual and figure
out where they go. But there was a complication here. The case's cables provide
3-pin plugs, while the motherboard provides one 3-pin socket and one 4-pin
socket. The motherboard manual explained which pins to use when connecting to
the 4-pin socket. I think the shape of the plug/socket might have made it
impossible to connect them in the wrong orientation, but I am not completely
sure of this.

The case provides a separate 3.5mm jack for speakers and a microphone - these
connected simply into a single 9-pin socket on the motherboard. The only
difficulty here was that it was hard to reach if the PSU was already installed.

The remaining plugs were the most complicated. Rather than providing a single
plug, they came in several separate plugs from the case, while the motherboard
provided a single 9-pin socket. It took a great deal of time studying the
manual to figure out exactly which pins to place these connectors into. This is
yet another aspect of assembly which is easy with experience, but rather
daunting on the first build.

The motherboard manual was indispensable for this effort, but also led to
further confusion, because it provides so many pins, and most cases will not
use all of them. For example, the motherboard provides multi-colored LED pins,
but the case does not use them. Leaving these types of pins on the motherboard
unconnected does not pose a problem.

## ATX vs Micro ATX Motherboards/Cases

At purchase time, the main trade-off between these two form factors was the
lower cost of the Micro ATX boards vs. the greater expandability of the full
ATX boards. However, at build time, I realized that I overlooked how cramped a
Micro ATX case can be. There is not a great deal of additional space for
cabling in a Micro ATX case - this is what makes planning the order of assembly
so important.

## Order of Assembly

Ultimately, I had to disassemble and reassemble the components several times.
The first time I installed the motherboard, I realized that I couldn't install
the RAM modules because of the amount of force required to make them snap into
place. Other builders may feel confident that exerting so much force will not
result in breakage, but I didn't want to risk it. So I realized that it is
easiest to install all components which are fastened directly to the
motherboard prior to mounting the motherboard in the case. This means that I
installed the RAM modules, CPU, CPU fan and PCIe SSD first before putting it
back in the case.

Another mistake that I made was not connecting the case to the motherboard
before mounting the motherboard into the case. As explained above, it was
time-consuming enough to figure out how to connect the plugs from the case into
the pins of the motherboard. It was made even more difficult and time-consuming
by the fact that the power pins on the motherboard were very close to the PSU
and internal disk bays. In retrospect, I should have connected these before
installing the motherboard.

I also ended up having to remove and reinstall the GPU and PSU several times.
The instructions for the case recommended installing the PSU first, but after
putting the PSU in, I realized that the side of the PSU where the cables are
connected was very close to the internal drive bays, so it was too difficult to
connect them before inserting and securing the PSU. I also realized late into
the assembly that the HD audio pins on the motherboard are located right next
to the PSU, and that it was nearly impossible to plug into those pins while the
PSU was secured into the case.

# Lessons Learned for Next Time

So using the wisdom that I gained from this experience, here is how I would do
it again next time:

1. Prepare the case with the mounting screws for the motherboard.

2. Install all components which are secured directly onto the motherboard. As
   explained above, that would include the RAM, CPU + fan, and PCIe SSD for
   this build.

3. Connect the wires from the case to the motherboard before mounting the
   motherboard in the case. It is important to study the motherboard manual to
   understand where and how to make these connections. if the case manual does
   not explain the wiring, then just study the wires to figure out what needs
   to be connected. Once this is complete, then mount the motherboard.

4. Install 2.5-inch/3.5-inch disk drives into the internal disk bays.

5. Install all PSU cables into the components and run the cables around the
   back of the case, and then plug them into the PSU. The only exception here
   is the GPU cable, which should be plugged into the PSU, but not into the
   GPU.

7. Secure the PSU into the case.

8. Install the GPU onto the motherboard.

9. Plug the GPU power cord from the PSU.

And that's it. All that's left is to plug it in and press the power button. I
found that the system did not boot properly after disassembling. The culprit
was the fact that the motherboard PSU cable was not in properly, which is
understandable - it is extremely large. Disconnect the power, double-check all
the connections, and then try again.

Overall, while it was difficult, it was a great learning experience. I look
forward to having this computer break so I can go through the process again.
