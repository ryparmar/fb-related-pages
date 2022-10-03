# Analysis of Facebook recommended (related) pages

This project is concerned with extracting data from Facebook pages and mining their divergent attitudes towards climate 
change. 
The project is part of my girlfriend's thesis, where I helped with scraping the data and then processing it.
As the code was not expected to be reused, not much care was given to its cleanliness and readability (tbh, it is ugly). 😥
The thesis is available [here](https://dspace.cuni.cz/handle/20.500.11956/148143?locale-attribute=en), unfortunately 
only in Czech.
The English abstract is available 
[here](https://dspace.cuni.cz/bitstream/handle/20.500.11956/148143/120399369.pdf?sequence=3&isAllowed=y).
In short, the thesis tries to indirectly analyze Facebook's page recommendation algorithm and its effect on the creation 
of information bubbles in relation to the climate crisis.

![related pages](img/related-pages.png "Related Pages")


## Summary of steps

1. For each initially selected site (there were 20 in total), all recommended pages were scraped
2. Step 1. was repeated also for the scraped pages, i.e., two rounds of scraping was done
3. Pages that was not relevant to climate change were removed. We used a custom tf-idf-like score and hand-picked threshold
4. Rest of the climate change-related pages were manually annotated, i.e., their attitude towards climate change
5. A simple analysis of these annotated pages and their relationships was performed to see if FB's recommendation algorithm helps with breaking information bubbles


## Result

It's not that bad. FB is trying to recommend non-climate change denial pages a little more often.


## Future work

There is a plenty of space for improvement. 
Some simplifying assumptions were used in this project, for example, each of the recommended pages is considered to be equivalent.
However, to get to the last recommended page, the user has to click through. 
So, obviously, those are not equivalent and should be reweighted.


## Repository description:

<ul>
    <li><i>data</i></li>
        <ul>
            <li><i>init_page_label.csv</i>: 
            Manually annotated initial 20 pages based on relation to climate change.</li>
            <li><i>labeled_pages.csv</i>: 
            Manually annotated pages (recommended by FB from init_page_label) based on relation to climate change.</li>
            <li><i>labeled_posts.csv</i>: 
            Posts for relevant pages downloaded using CrowdTangle and labeled by their stance to climate change.</li>
            <li><i>uniq_links1.txt</i>: 
            List of unique initial pages (their url link)</li>
            <li><i>uniq_links2.txt</i>: 
            List of unique recommended pages for the uniq_links1 pages (their url link)</li>
            <li><i>uniq_relation_data1.csv</i>: 
            Initial pages and their related (recommended) pages. 
            The first column are initial pages and the rest of the columns are recommended.</li>
            <li><i>uniq_relation_data2.csv</i>: 
            Recommended pages for initial pages and recommended for that recommended pages.
            The first column are recommended for initial pages and the rest of the columns are recommended of recommended.
            For better understaing see the image Sber dat below.</li>
        </ul>
    <li><i>src</i></li>
        <ul>
            <li><i>notebooks</i>: directory with various experiments and calculations</li>
            <ul>
                <li><i>10-data-wrangling-analysis.ipynb</i>:
                various data wrangling, simple analysis and csv files preparation</li>
                <li><i>20-page-classification.ipynb</i>:
                calculation of relevancy scores and choosing only the climate change relevant pages</li>
                <li><i>30-visualize.ipynb</i>:
                plotly graph visualizations initial attempts</li>
                <li><i>3*-visualize-labeled-pages*.ipynb</i>:
                plotly graph visualizations final</li>
                <li><i>experimental-crowdtangle-posts.ipynb</i>:
                experimental notebook - looking at the data downdloaded from CrowdTangle</li>
                <li><i>experimental-text-analysis.ipynb</i>:
                experimental notebook - text analysis playground (not used at the end)</li>
            </ul>
            <li><i>scrapers</i>: directory with scrapers</li>
            <ul>
                <li><i>pages_content.py</i>: script for scraping the posts for given pages</li>
                <li><i>related_pages.py</i>: script for scraping the relations (recommendations) between the pages</li>
            </ul>
        </ul>
    <li><i>text</i>: directory with text and figures of diploma thesis</li>
    <li><i>interactive_graph_labeled.html</i>: 
    several versions of interactive plotly graph visualization of pages relations</li>
</ul>


## Data collection scheme

![sber dat](text/obrazky/sber_dat.jpg "Sber dat")
