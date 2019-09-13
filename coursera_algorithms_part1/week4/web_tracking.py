import unittest
from string import ascii_lowercase as charset
from random import sample, randint


class WebTracking:
    def __init__(self, m_user, n_sites):
        self.users_n_sites = [{} for i in range(m_user+1)]

    def user_visits_site(self, user_id, website):
        current_visits = self.users_n_sites[user_id].get(website, 0)
        self.users_n_sites[user_id][website] = current_visits + 1

    def user_website_visit_count(self, user_id, website):
        return self.users_n_sites[user_id].get(website, 0)


class TestWebTracking(unittest.TestCase):
    def setUp(self):
        self.user_count = 1000
        self.website_count = 1000
        self.user_ids = list(range(self.user_count))
        self.webaddresses = self.random_webaddress(self.website_count, 10)

        self.wt = WebTracking(self.user_count, self.website_count)

    def random_webaddress(self, address_count, addr_len):
        addresses = set()
        while len(addresses) < address_count:
            charsize = len(charset)
            address = ''.join([charset[randint(0, charsize-1)] for x in range(addr_len)])
            addresses.add(address)
        return list(addresses)

    def test_no_count(self):
        test_user = sample(self.user_ids, 1)[0]
        test_address = sample(self.webaddresses, 1)[0]
        self.assertEqual(0, self.wt.user_website_visit_count(test_user, test_address))

    def test_count(self):
        test_user = sample(self.user_ids, 1)[0]
        test_address = sample(self.webaddresses, 1)[0]
        count = 0
        for i in range(self.user_count*self.website_count):
            user_id = sample(self.user_ids, 1)[0]
            webaddress = sample(self.webaddresses, 1)[0]
            self.wt.user_visits_site(user_id, webaddress)
            if test_user == user_id and test_address == webaddress:
                count += 1
        self.assertEqual(self.wt.user_website_visit_count(test_user, test_address), count)


if __name__ == '__main__':
    unittest.main()
