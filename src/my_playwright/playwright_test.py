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
    page.goto("https://edition.cnn.com")
    # 类似断点，会有一个playwright窗口，让你进行相关操作（如元素定位，录制）
    page.pause()
    # 设置最大等待超时时间（超过该时间则会报错 ）
    page.wait_for_timeout(3000)


def go_github():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/mglslg")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_label("Username or email address").click()
    page.get_by_label("Username or email address").fill("mglslg@qq.com")
    page.get_by_label("Username or email address").press("Tab")
    page.get_by_label("Password").fill("slg***")
    page.get_by_role("button", name="Sign in", exact=True).click()
    page.wait_for_timeout(3000)
    page.get_by_label("Open user navigation menu").click()
    page.get_by_label("Your repositories").click()
    page.get_by_role("link", name="slg-sf-demo").click()

    # ---------------------
    context.close()
    browser.close()


def go_dify():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dify.hogwartscoder.com")
    page.get_by_placeholder("输入邮箱地址").click()
    page.get_by_placeholder("输入邮箱地址").fill("mglslg@qq.com")
    page.get_by_placeholder("输入邮箱地址").press("Tab")
    page.get_by_placeholder("输入密码").fill("slg***")
    page.get_by_role("button", name="登录").click()
    page.get_by_role("button", name="S slg").click()
    page.get_by_role("menuitem", name="设置").click()

    context.close()
    browser.close()


def go_dify_headless():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

    # 设置全局超时时间
    context.set_default_timeout(60000)

    try:
        page = context.new_page()
        page.goto("https://dify.hogwartscoder.com", timeout=60000)  # 增加超时时间

        page.get_by_placeholder("输入邮箱地址").click(timeout=60000)
        page.get_by_placeholder("输入邮箱地址").fill("mglslg@qq.com", timeout=60000)
        page.get_by_placeholder("输入邮箱地址").press("Tab", timeout=60000)
        page.get_by_placeholder("输入密码").fill("slg***", timeout=60000)
        page.get_by_role("button", name="登录").click()
        page.get_by_role("button", name="S slg").click()
        page.get_by_role("menuitem", name="设置").click()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        context.close()
        browser.close()


if __name__ == '__main__':
    pw_test()
    # go_github()
    # go_dify()
    # go_dify_headless()
