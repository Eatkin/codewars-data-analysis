# https://www.codewars.com/kata/54dc6f5a224c26032800005c
# 2023-05-17T08:17:43.782+0000
def stock_list(list_of_art, list_of_cat):
    # Create dictionary
    stock = {
        cat: 0 for cat in list_of_cat
    }
    
    total = 0
    for book in list_of_art:
        if book[0] in stock:
            num_books = int(book.split()[1])
            stock[book[0]] += num_books
            total += num_books
            
    if total == 0:
        return ""
                
    # Construct return string
    return_str = ""
    for key, value in stock.items():
        return_str += f"({key} : {value}) - "
    
    return return_str[:-3]