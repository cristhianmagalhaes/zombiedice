from time import localtime

print(localtime().tm_mday)
print(localtime().tm_wday)
print(localtime().tm_yday)
print(localtime().tm_isdst)