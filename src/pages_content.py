#!/usr/bin/env python3
import logging
import datetime
import argparse
import os, sys
import json

from facebook_scraper import get_posts

### TBD
### https://github.com/kevinzg/facebook-scraper/tree/c3ccc1e4241ed6fd3c09ad1c7aa22c7f536418a2


# Save crawled data into file
def save(file: str, data: dict):
    logging.info(f'Saving...{[k for k,_ in data.items()]}')
    for pagename, posts in data.items():
        if not posts:
            logging.info(f"No posts were scraped for {pagename}")
    
    if not os.path.exists(file):
        with open(file, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
    else:
        with open(file, 'r+', encoding='utf8') as f:
            tmp = json.load(f)
            tmp.update(data)
            f.seek(0)
            json.dump(tmp, f, ensure_ascii=False)


if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('--pagenames', type=str, help='path to the file with the page names')
    parser.add_argument('--pages', default=10, type=int, help='how many pages of posts to request, usually the first page has 2 posts and the rest 4. Default is 10.')
    parser.add_argument('--outputfile', default=None, type=str, help='output file')
    args = parser.parse_args()

    # Logging
    logging.basicConfig(filename='log-content', level=logging.INFO)
    start = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    outfile = args.outputfile if args.outputfile else'data-content-' + start + '.json'
    logging.info(f"Started at {start}")

    # Read the file with FB page names
    PAGES = []
    if os.path.exists(args.pagenames):
        with open(args.pagenames, 'r') as f:
            for page in f.readlines():
                PAGES.append(page.strip())
    else:
        print("File with FB page names does not exist!")
        sys.exit(0)

    # Crawl the FB posts and save them
    page2posts = {}
    for c, page in enumerate(PAGES):
        sys.stdout.write('\r{}/{}  {}'.format(c, len(PAGES), page))

        if page not in page2posts:
            page2posts[page] = []
            try:
                for post in get_posts(page, pages=args.pages):
                    # print(f"all: {post}\n\n")
                    
                    if post['text']:
                        page2posts[page].append(post['text'])
            except:
                logging.error(f"Error in getting posts for {page}")

            # each n-th pagename save the data
            N = 5
            if (c > 0 and (c + 1) % N == 0) or (c + 1) == len(PAGES):
                save(outfile, page2posts)
                page2posts = {}
        else:
            logging.info(f"{page} already present in the data!")
    logging.info('Finished')