from playwright.sync_api import sync_playwright, Playwright


def pw_test():
    # 使用同步的方式启动playwright
    playwright = sync_playwright().start()
    # 启动一个chromium内核的浏览器,headless默认为True表示无头模式，不显示浏览器
    browser = playwright.chromium.launch(headless=False)
    # 新建一个浏览器上下文
    context = browser.new_context()

    context.set_default_timeout(60000)

    # 创建一个新的页面（_blank）
    page = context.new_page()
    # 页面需要进入哪个网址
    page.goto("https://www.linkedin.com")
    # 类似断点，会有一个playwright窗口，让你进行相关操作（如元素定位，录制）
    page.pause()
    # 设置最大等待超时时间（超过该时间则会报错 ）
    page.wait_for_timeout(3000)


if __name__ == '__main__':
    pw_test()
