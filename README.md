# net-hub-pi
A raspberry pi with a touchscreen that acts as a visual network hub

I bought my Raspberry pi touch screen for 17$ on amazaon [here](http://www.amazon.com/gp/product/B013E0IJVE?psc=1&redirect=true&ref_=oh_aui_detailpage_o00_s00 here)

## installing the OS
Download the Osoyoo Raspian 7 with special drivers here: [Osoyoo Downloads](http://osoyoo.com/wp-content/uploads/samplecode/ Osoyoo Downloads)

You should download the .rar file titled: <code>raspberry_35_inch_ts.rar</code>

You will need to extract the img file from this .rar 

### Burning to SD
#### MAC OSX
In this directory you will see an <code>example.burn.sh file</code>. This (along with the <code>history.txt</code> file) contains what I did to burn the image to an SD card. Genrally follow:

1. Find the SD card by running <code>diskutil list</code>.
2. Try to unmoun the disk with <code>diskutil unmount /dev/SOME_DISK<code/> (for me this was diskutil unmount /dev/disk2)
3. start burning the image. THIS MAY TAKE A WHILE! <code>dd if=path_of_your_image.img of=/dev/SOME_DISK bs=1m</code>

Once you have done this Raspian should boot on your pi

#### Linux
TDB

### Configuring the Pi
follow your standard pi wifi set ups. I had a wireless dongle so I did what the standard guide says: [Connect Pi to Wifi](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md Connect Pi to Wifi)

I also had to set my keyboard to US settings by editing my <code>/etc/default/keyboard</code>. Just: 

<code>sudo nano /etc/default/keyboard</code>

And change your contry code in <code>XKBLAYOUT</code>. I changed mine to <code>XKBLAYOUT="us"</code>