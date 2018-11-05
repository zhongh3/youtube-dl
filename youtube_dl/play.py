# Playground
from .extractor.common import InfoExtractor

# Test URL:
# https://www.bilibili.com/video/av4082055/?p=44


# http://www.bilibili.tv/video/av1074402/
# http://bangumi.bilibili.com/anime/1869/play#40062
# http://www.bilibili.com/video/av8903802/

# python -m youtube_dl -F https://www.bilibili.com/video/av4082055/?p=44 --no-check-certificate


class BiliBili(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.|bangumi\.|)bilibili\.(?:tv|com)/' \
        r'(?:video/av|anime/(?P<anime_id>\d+)/play#)(?P<id>\d+)\?p=(?P<part_id>\d+)'

    _APP_KEY = '84956560bc028eb7'
    _BILIBILI_KEY = '94aba54af9065f71de72f5508f1cd42e'

    def _real_extract(self, url):
        # mobj = re.match(self._VALID_URL, url)
        # video_id = mobj.group('id')
        # part_id = mobj.group('part_id')

        webpage = self._download_webpage(url, video_id)


def main():
    url = "https://www.bilibili.com/video/av4082055/?p=44"
    ie = BiliBili()
    ie.



if __name__ == "__main__":
    main()