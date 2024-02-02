pattern = r"v([\d]+\.[\d]+-[\d]+).tar.gz"


def fetch_versions(self, url):
    return map(lambda x: x.replace("-", "."), self.fetch_versions(url))
