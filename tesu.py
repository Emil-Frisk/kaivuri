def IEG_MODE_bitmask_alternative(number):
        mask = (1 << 7) |(1 << 1) 
        number = number & 0xFFFF
        return number & mask

result = IEG_MODE_bitmask_alternative(65535)
print(result)