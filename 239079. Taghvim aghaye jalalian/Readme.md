[تقویم آقای جلالیان](https://quera.org/problemset/239079)
----------

+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------
آقای جلالیان یک تقویم جلالی عجیب روی میز کارش دارد. تقویم او از دو تاس مکعبی با ۶ وجه تشکیل شده است. اما روی این تاس‌ها لزوما اعداد `1`، `2`، ...، `6` نوشته نشده است بلکه ممکن است روی هر وجه یک رقم از `0`، `1`، ...، `9` نوشته شده باشد.

آقای جلالیان از روز اولی که وارد شرکت شد، با تاس‌هایش روزشماری می‌کند تا بداند تا امروز چند روز از اولین روز کاری‌اش در شرکت می‌گذرد.

![تقویم آقای جلالیان](https://quera.org/qbox/view/dSpZf0Qw7w/B1.png)

روش استفاده آقای جلالیان از تاس‌هایش برای نشان دادن شماره روز به این صورت است که با **یک تاس** اعداد یک رقمی و با کنارهم گذاشتن دوتاس اعداد دو رقمی ساخته می‌شوند. مثلاً اگر تاس سمت چپ رقم `3` و تاس سمت راست رقم `2` را نشان دهد یعنی در روز `32`ام هستیم.

آقای جلالیان می‌داند که قرار است دقیقاً تا روز $n$ام در شرکت بماند که $n$ عددی حداکثر دو رقمی است. او تصمیم دارد دو تاس خام بگیرد و روی وجه‌های تاس اول ارقام $a_1, a_2, \dots, a_6\,$ و روی وجه‌های تاس دوم ارقام $b_1, b_2, \dots, b_6\,$ را بنویسد به طوری که بتواند در همه‌ی روزهای ۱ تا $n$ شماره‌ی روز را روی میزش نمایش دهد.

به آقای جلالیان کمک کنید تا مقدارهای مناسب برای $a_1, a_2, \dots, a_6\,$ و $b_1, b_2, \dots, b_6\,$ را پیدا کند یا به او بگویید هیچ روشی برای انجام این کار وجود ندارد.

# ورودی
در تنها سطر ورودی، یک عدد طبیعی $n$ داده می‌شود که نشان‌دهنده شماره روز آخرین روز کاری آقای جلالیان است.
$$1\leq n \leq 99$$

# خروجی
در صورتی که این کار امکان پذیر نبود `-1` چاپ کنید. و در غیر این صورت خروجی شامل دو سطر خواهد بود.

در سطر اول خروجی ۶ رقم $a_1, a_2, \dots, a_6\,$ با فاصله از هم چاپ کنید که هر رقم نشان‌دهنده یک رقم روی یکی از وجه‌های تاس اول است و به همین شکل در سطر دوم خروجی ۶ رقم $b_1, b_2, \dots, b_6\,$ با فاصله از هم چاپ کنید که هر رقم نشان‌دهنده یک رقم روی یکی از وجه‌های تاس دوم است.

**اگر چند جواب برای این مسئله وجود دارد، یکی را به دلخواه چاپ کنید.**

# مثال‌ها
## ورودی نمونه ۱

```
10
```
## خروجی نمونه ۱

```
0 0 5 3 2 4
1 1 6 7 8 9
```
در اینجا آقای جلالیان روی وجه‌های تاس اول ارقام `0`، `0`، `5`، `3`، `2` و `4` و روی وجه‌های تاس دوم ارقام `1`، `1`، `6`، `7`، `8` و `9` را نوشته است.

چون همه‌ی ارقام `1` تا `9` حداقل یکبار ظاهر شده‌اند، پس برای نشان‌دادن روزهای ۱ تا ۹ مشکلی نیست. 
برای روز ‍‍‍۱۰ام، می‌تواند `1` را از تاس دوم و `0` را از تاس اول بردارد. 


## ورودی نمونه ۲
```
99
```

## خروجی نمونه ۲
```
-1
```
آقای جلالیان هیچ روشی ندارد که طوری ارقام ۰ تا ۹ را روی وجه‌های دو تاس طوری قرار دهد که همه‌ی اعداد ۱ تا ۹۹ قابل نمایش باشند. بنابراین پاسخ `-1` است.
