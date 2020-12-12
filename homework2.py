shop_menus = ["만두", "국밥","떡볶이","김밥", "오뎅","애플파이", "사이다","라면", "콜라","감자튀김"]
shop_orders = ["오뎅", "사이다", "만두"]


def is_available_to_order(menus, orders):
    shop_menus.sort()
    def availability(menus,string):
        start=0
        end=len(menus)-1
        now = (start+end)//2
        counter=0
        while start<=end:
            counter+=1
            if menus[now] == string:
                
                return True
            elif menus[now]<string:
                start = now + 1
            else:
                end = now -1
            now = (start+end)//2
        return False
    for unit in orders:
        if availability(menus,unit)==False:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)

#print(shop_menus)

print(result)
