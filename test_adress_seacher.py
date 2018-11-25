import unittest

from address_seacher import AddressSeacher


class TestAddressSeacher(unittest.TestCase):
    def test_岩手県八幡平市大更の地名を郵便番号から取得できる(self):
        address_searcher = AddressSeacher()

        self.assertEqual("岩手県八幡平市大更", address_searcher.search(postal_code="0287111"))

    def test_東京都練馬区豊玉南の地名を郵便番号から取得できる(self):
        address_searcher = AddressSeacher()

        self.assertEqual("東京都練馬区豊玉南", address_searcher.search(postal_code="1760014"))

    def test_存在しない郵便番号が入力されたらエラーメッセージを表示する(self):
        address_searcher = AddressSeacher()

        self.assertEqual("該当するデータが見つかりませんでした。検索データを変えて再検索してください。", address_searcher.search(postal_code="1234567"))

if __name__ == "__main__":
    unittest.main()

