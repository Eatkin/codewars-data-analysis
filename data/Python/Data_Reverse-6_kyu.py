# https://www.codewars.com/kata/569d488d61b812a0f7000015
# 2023-06-01T13:58:28.110+0000
def data_reverse(data):
    # Group data
    grouped_data = []
    for i in range(int(len(data) / 8)):
        grouped_data.append("".join([str(num) for num in data[i * 8:(i + 1) * 8]]))
    
    print(grouped_data)
    
    grouped_data.reverse()
    return [int(i) for datum in grouped_data for i in datum]