from address_seacher import AddressSeacher


def main():
    # ユーザーからの郵便番号を受け取る

    # 郵便番号を使って地名を取ってくる

    # 地名をprintする
    postal_code = str(input("郵便番号(7ケタ):"))

    address_searcher = AddressSeacher()

    address_info = address_searcher.search(postal_code)

    print(address_info)


if __name__ == "__main__":
    main()
