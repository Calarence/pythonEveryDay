from urllib.request import urlopen
from urllib.parse import urlparse
import re
import sys
LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")

class LinksCollector:
	"""collect links for a site"""
	def __init__(self, url):
	    self.url = "http://" + urlparse(url).netloc
	    self.collected_links = set()
	    self.visited_links = set()

	def normalize_url(self,path,link):
		"""make link look like http://..."""
		if link.startswith("http://"):
			return link
		elif link.startswith('/'):
			return self.url + link
		else:
			return self.url + path.rpartition('/')[0]+'/'+link

	def collect_links(self,path='/'):
		full_url = self.url + path
		self.visited_links.add(full_url)
		page = str(urlopen(full_url).read())
		links = LINK_REGEX.findall(page)
		links = {self.normalize_url(path,link) for link in links}
		print(links)
		self.collected_links = links.union(self.collected_links)
		unvisited_links = links.difference(self.visited_links)
		for link in unvisited_links:
			if link.startswith(self.url):
				self.collect_links(urlparse(link).path)
		print(links,self.visited_links,self.collected_links,unvisited_links)
if __name__ == '__main__':
	collector = LinksCollector(sys.argv[1])
	collector.collect_links()
	for link in collector.collected_links:
		print(link)
