import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python pagerank.py corpus")
    dir = "corpus2"
    corpus = crawl(dir)
    #{'1.html': {'2.html'}, '2.html': {'3.html', '1.html'}, '3.html': {'2.html', '4.html'}, '4.html': {'2.html'}}
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus : dict, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result_dict = {}
    page_num = len(corpus.keys())
    for key in corpus.keys():
        #每个页面都有1-damping_factor的概率被选中
        result_dict[key] = (1-damping_factor)/page_num
    out_set = corpus[page]
    for out in out_set:
        result_dict[out]+= damping_factor/len(out_set)
    return result_dict
    raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    page_rank = {}
    pages = list(corpus.keys())
    #从页面里随机选择一个作为初始页面
    for page in pages:
        page_rank[page] = 0
    chosen_page = random.choice(pages)
    page_rank[chosen_page]=1
    for i in range(1,n):
        #计算该网页转移到其他网页的概率分布
        transform_probablity = transition_model(corpus,chosen_page,damping_factor)
        sum = 0
        randon_float = random.random()
        #模拟根据概率分布进行抽样的过程
        for page,probablity in transform_probablity.items():
            sum+=probablity
            if randon_float<sum:
                chosen_page=page
                #统计每个网页被选中的次数
                page_rank[chosen_page]+=1
                break
    #执行归一化操作
    for page,value in page_rank.items():
        page_rank[page] = value/n
    return page_rank



    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    raise NotImplementedError

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    initial_rank = 1.0 / num_pages
    current_rank = {page: initial_rank for page in corpus}
    new_rank = {page: 0 for page in corpus}

    # 定义一个函数来计算给定页面的PageRank值
    def calculate_pagerank(page):
        #初始值为（1-阻尼因子）/页面数量
        rank = (1 - damping_factor) / num_pages
        #阻尼因子，通过指向这个页面的其他页面的page_rank值来计算这个页面的page_rank值
        rank += damping_factor * sum(current_rank[link] / len(corpus[link]) for link in corpus if page in corpus[link])
        return rank

    # 开始迭代计算PageRank值，直到收敛
    while True:
        # 遍历每个页面，计算新的PageRank值
        for page in corpus:
            new_rank[page] = calculate_pagerank(page)

        # 检查是否收敛，如果所有页面的PageRank值变化都小于0.001，则退出循环
        convergence = all(abs(new_rank[page] - current_rank[page]) < 0.001 for page in corpus)
        if convergence:
            break

        # 将新的PageRank值复制到current_rank以进行下一轮迭代
        current_rank = new_rank.copy()

    # 归一化PageRank值，使其总和为1
    total_rank = sum(new_rank.values())
    normalized_rank = {page: rank / total_rank for page, rank in new_rank.items()}

    return normalized_rank

#
# def iterate_pagerank(corpus, damping_factor):
#
#     """
#     Return PageRank values for each page by iteratively updating
#     PageRank values until convergence.
#
#     Return a dictionary where keys are page names, and values are
#     their estimated PageRank value (a value between 0 and 1). All
#     PageRank values should sum to 1.
#     """
#     raise NotImplementedError
#

if __name__ == "__main__":
    main()
