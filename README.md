# Analysis of Facebook recommended (related) pages

This repo provides a code for scraping the data (both relations between the pages and posts), 
processing them and simple analysis of the recommended pages by Facebook algorithm.

![related pages](img/related-pages.png "Related Pages")



## Repository description:
<ul>
    <li><i>data</i></li>
        <ul>
            <li><i>links1</i>: 
            List of unique initial pages (their url link)</li>
            <li><i>links2-uniq</i>: 
            List of unique recommended pages for the initial pages (their url link)</li>
            <li><i>data1.csv</i>: 
            Initial pages and their related (recommended) pages. 
            The first column are initial pages and the rest of the columns are recommended.</li>
            <li><i>data2-uniq.csv</i>: 
            Recommended pages for initial pages and recommended for that recommended pages.
            The first column are recommended for initial pages and the rest of the columns are recommended of recommended.
            For better understaing see the image Sber dat below.</li>
            <li><i>labeled_posts.csv</i>: 
            Posts for relevant pages downloaded using CrowdTangle and labeled by their stance to climate change.</li>
        </ul>
    <li><i>src</i></li>
        <ul>
            <li><i>notebooks</i>: directory with various experiments and calculations</li>
            <ul>
                <li><i>crowdtangle-posts.ipynb</i>:
                experimental notebook - looking at the data downdloaded from CrowdTangle</li>
                <li><i>text-analysis.ipynb</i>:
                experimental notebook - text analysis playground (not used at the end)</li>
                <li><i>page-classification.ipynb</i>:
                calculation of relevancy scores and choosing only the climate change relevant pages</li>
                <li><i>visualize.ipynb</i>:
                plotly graph visualizations initial attempts</li>
                <li><i>visualize-labeled-pages*.ipynb</i>:
                plotly graph visualizations final</li>
                <li><i>data-wrangling-analysis.ipynb</i>:
                various data wrangling, simple analysis and csv files preparation</li>
            </ul>
            <li><i>pages_content.py</i>: script for scraping the posts for given pages</li>
            <li><i>related_pages.py</i>: script for scraping the relations (recommendations) between the pages</li>
        </ul>
    <li><i>text</i>: directory with text and figures of diploma thesis</li>
    <li><i>interactive_graph_labeled.html</i>: 
    several versions of interactive plotly graph visualization of pages relations</li>
</ul>


![sber dat](text/obrazky/sber_dat.jpg "Sber dat")
