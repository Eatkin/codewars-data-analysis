# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7
2023-03-09T07:29:20.666+0000
def pick_peaks(arr):
    pos = []
    peaks = []
    # Short circuit
    if not arr:
        return {"pos": pos, "peaks": peaks}

    nums = len(arr)
    for i in range(1, nums - 1):
        num = arr[i]
        # Simple logic to check either side
        if num > arr[i - 1] and num > arr[i + 1]:
            pos.append(i)
            peaks.append(num)

        # Plateau check
        elif num > arr[i - 1] and num == arr[i + 1]:
            # Now we need to check for plateaus - first we will assume we are NOT plateau until we can validate
            # Assuming not will mean it doesn't matter if we hit the end of the array
            # Now we need to find a number to the right smaller than our own
            for j in range(i + 1, nums):
                if arr[j] < num:
                    pos.append(i)
                    peaks.append(num)
                    break
                elif arr[j] > num:
                    break
    
    return {"pos": pos, "peaks": peaks}