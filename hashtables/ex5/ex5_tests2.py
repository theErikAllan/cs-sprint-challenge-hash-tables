import unittest

from ex5 import finder


class TestEx2(unittest.TestCase):

    def test_small(self):
        files = [
            '/bin/foo',
            '/bin/bar',
            '/usr/bin/baz'
        ]
        queries = [
            "foo",
            "qux",
            "baz"
        ]
        result = finder(files, queries)
        self.assertTrue(result == ['/bin/foo', '/usr/bin/baz'])

        queries = [
            "qux"
        ]
        result = finder(files, queries)
        self.assertTrue(result == [])

    def test_large(self):
        files = []

        for i in range(1000):
            files.append(f"/dir{i}/file{i}")

        for i in range(1000):
            files.append(f"/dir{i}/dirb{i}/file{i}")

        queries = []

        for i in range(1000):
            queries.append(f"nofile{i}")

        queries += [
            "file340",
            "file256",
            "file9999",
            "file812"
        ]

        result = finder(files, queries)
        result.sort()

        self.assertTrue(result == ['/dir256/dirb256/file256',
            '/dir256/file256', '/dir340/dirb340/file340',
            '/dir340/file340', '/dir812/dirb812/file812',
            '/dir812/file812'])

if __name__ == '__main__':
    unittest.main()
