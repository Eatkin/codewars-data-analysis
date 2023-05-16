# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7
# 2023-03-09T07:23:30.695+0000
def pick_peaks(arr):
    pos = []
    peaks = []
    nums = len(arr)
    # Short circuit
    if nums > 0:
        for i in range(1, nums - 1):
            num = arr[i]
            # Simple logic to check either side
            if num > arr[i - 1] and num > arr[i + 1]:
                pos.append(i)
                peaks.append(num)
                continue
            
            # Plateau check
            if num > arr[i - 1] and num == arr[i + 1]:
                # Now we need to check for plateaus - first we will assume we are NOT plateau until we can validate
                # Assuming not will mean it doesn't matter if we hit the end of the array
                # A plateau is 3 numbers in a row with lower numbers either side
                # Make sure the checks we're doing are in range
                in_range = i > 1
                if in_range:
                    # Now we need to find a number to the right smaller than our own
                    for j in range(i + 1, nums):
                        if arr[j] < num:
                            pos.append(i)
                            peaks.append(num)
                            break
                        elif arr[j] > num:
                            break
    
    return {"pos": pos, "peaks": peaks}