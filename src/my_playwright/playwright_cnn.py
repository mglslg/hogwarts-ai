import re
from datetime import datetime, timedelta

from playwright.sync_api import sync_playwright


def date_test():
    link = "https://edition.cnn.com/2024/07/10/travel/snake-smuggler-trousers-scli-intl/index.html"
    today_date = datetime.now().strftime("%Y/%m/%d")
    date_pattern = re.compile(r'\d{4}/\d{2}/\d{2}')
    match = date_pattern.search(link)
    if match:
        link_date = match.group()
        print(link_date)
        print(today_date)


def scrape_cnn():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=True)  # 如果不需要显示浏览器界面，可以设置为headless=True
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

        context.set_default_timeout(60000)

        page = context.new_page()

        # 访问目标网站
        page.goto('https://edition.cnn.com/world/china')  # 将此处的URL替换为你要爬取的网站URL

        # 等待页面加载完成（可选）
        # page.wait_for_load_state('networkidle')

        headlines = page.query_selector_all('span.container__headline-text')
        for h in headlines:
            parent_a = h.eval_on_selector('xpath=ancestor::a[1]',
                                          'element => element ? element.getAttribute("href") : null')
            if parent_a:
                link = "https://edition.cnn.com" + parent_a
                yesterday_date = (datetime.now() - timedelta(1)).strftime("%Y/%m/%d")
                date_pattern = re.compile(r'\d{4}/\d{2}/\d{2}')
                match = date_pattern.search(link)
                if match:
                    link_date = match.group()
                    # 只要最新的新闻(前一天)
                    if link_date == yesterday_date:
                        print(h.inner_text(), "-->", link)

        # 关闭浏览器
        browser.close()


if __name__ == '__main__':
    scrape_cnn()
    # date_test()
