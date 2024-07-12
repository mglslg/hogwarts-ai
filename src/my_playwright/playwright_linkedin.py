from playwright.sync_api import sync_playwright


def scrape_linkedin_debug():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()

    # 设置全局超时时间
    context.set_default_timeout(60000)

    try:
        page = context.new_page()
        page.goto("https://www.linkedin.com/login/zh-cn")
        page.get_by_label("邮箱或手机").click()
        page.get_by_label("邮箱或手机").fill("mglslg1988@gmail.com")
        page.get_by_label("密码").click()
        page.get_by_label("密码").fill("slg***")
        page.get_by_label("登录", exact=True).click()

        page.pause()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        context.close()
        browser.close()


def scrape_linkedin():
    pw = sync_playwright().start()
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

    # 设置全局超时时间
    context.set_default_timeout(60000)

    try:
        page = context.new_page()
        page.goto("https://www.linkedin.com/login/zh-cn")
        page.get_by_label("邮箱或手机").click()
        page.get_by_label("邮箱或手机").fill("mglslg1988@gmail.com")
        page.get_by_label("密码").click()
        page.get_by_label("密码").fill("slg***")
        page.get_by_label("登录", exact=True).click()

        page.goto(
            'https://www.linkedin.com/jobs/view/3955330944/?alternateChannel=search&refId=5yJ7vqtabSnL4XiCWu5HUA%3D%3D&trackingId=zDQ7lWzwkpVDNZcRUtiG3A%3D%3D')

        location_restrict = page.query_selector("h2.how-you-match-card-title")

        print(location_restrict.inner_text())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        context.close()
        browser.close()


if __name__ == '__main__':
    scrape_linkedin()
    # scrape_linkedin_debug()
