class Codec:
    hash_map = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        hashKey = hash(longUrl)
        self.hash_map[hashKey] = longUrl
        return "http://tinyurl.com/"+str(hashKey)


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        hashKey = shortUrl.replace("http://tinyurl.com/","")
        return self.hash_map[int(hashKey)]

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))