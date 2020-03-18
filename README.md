# script/conv.py 

## Run it like this

> chip@chip:/opt/cnc$ sudo python3 script/conv.py files/fuchs.nc
>
> Loading file: files/fuchs.nc
>
> Output file: files/fuchs_conv.nc
>
> 1631372 Lines converted

### Info

Convertes a file with different Z heights to a _conv version of the file
that will add M3 Commands whenever the Height changes.

So everything with G0/G1 XY[Z>0] will result in a Pen UP, M3S0 followed
by a break.

Everything with G0/G1 XY[Z<=0] will result in Pen DOWN, M3S200 followed
as well by a break of 200ms.

All Lines but G0/G1 will be removed from the file


# run.sh
## Run it like this
	chip@chip:/opt/cnc$ ./run.sh files/fuchs_conv.nc
	This will open a screen running the streamer, the screen is called draw_screen so you can connect remotely if needed.
	This streamer will run on /dev/ttyUSB0
