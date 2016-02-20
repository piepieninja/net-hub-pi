# sudo dd if=path_of_your_image.img of=/dev/rdiskn bs=1m
echo '==============================================================='
diskutil list
echo '==============================================================='
echo 'try to unmount your disk. For me: diskutil unmount /dev/disk3s1'
#diskutil unmount /dev/disk3s1
echo 'try: dd if=path_of_your_image.img of=/dev/rdiskn bs=1m'
echo 'for me it was: sudo dd if=~/Downloads/raspberry_35_inch_ts/rpi_35_B_B+_PI2.img of=/Volumes/UNTITLED bs=1m'